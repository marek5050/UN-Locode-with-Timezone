import csv
from os import mkdir
from os.path import exists
from zipfile import ZipFile

import numpy as np
import pandas as pd
import urllib.request as request
from io import BytesIO
import pymongo

import os

from dotenv import load_dotenv

load_dotenv()

datadir = "data"
if not exists(datadir):
    mkdir(datadir)

if not exists("scripts/tmp"):
    mkdir("scripts/tmp")

unlocodes = "https://github.com/marek5050/UN-LOCODE/raw/master/data/code-list.csv"
cities = "http://download.geonames.org/export/dump/%s.zip"

names_cities = "geonameid,name,asciiname,alternatenames,latitude,longitude,feature class,feature code,country_code,cc2,subdivision,admin2 code,admin3 code,admin4 code,population,elevation,dem,timezone,modification date".split(
    ",")
cities_use_cols = "name,asciiname,alternatenames,latitude,longitude,country_code,subdivision,timezone,modification date".split(
    ",")
names_locodes = "change,country_code,location,name,asciiname,subdivision,status,function,date,iata,coordinates,remarks".split(
    ",")
locodes_use_cols = "country_code,location,name,subdivision,coordinates".split(",")
# name = "allCountries"
name = "cities15000"

global dcities, dunlocodes

dcities = None
dunlocodes = None

list_unlocodes = []


class MongoQuery:
    db = None
    collection = None
    uri = "mongodb://%s@oceans-shard-00-00.iotwb.mongodb.net:27017,oceans-shard-00-01.iotwb.mongodb.net:27017,oceans-shard-00-02.iotwb.mongodb.net:27017/timezones?ssl=true&replicaSet=atlas-10a87j-shard-0&authSource=admin&retryWrites=true&w=majority"

    def __init__(self, u_p):
        client = pymongo.MongoClient(self.uri % (u_p))
        self.db = client.get_database("oceandb")
        self.collection = self.db["timezones"]

    def query(self, unlocode="NONE", name="NONE"):
        items = list(self.collection.find({"unlocode": {'$regex': unlocode} },{"_id":0}  ).limit(10))
        if len(items) == 0:
            items = list(self.collection.find({"city": {'$regex': name ,'$options': 'i'} }, {"_id":0}  ).limit(10))

        return items

    def insert_records(self, records):
        for item in records:
            item["_id"]=item["unlocode"]
            self.collection.replace_one({"_id":item["unlocode"]}, item,upsert=True)


m = MongoQuery(os.environ.get('U_P'))

def retrieve_all_countries():
    z = request.urlopen(cities % name)
    myzip = ZipFile(BytesIO(z.read())).extract('%s.txt' % name)
    d2 = pd.read_csv(myzip, delimiter="\t",
                     names=names_cities,
                     usecols=cities_use_cols,
                     dtype={'name': str, "asciiname": str, "alternatenames": str, "latitude": float,
                            "longitude": float, "country_code": str, "subdivision": str, "timezone": str,
                            "modification date": str})
    d2.drop_duplicates(subset=['name', 'subdivision', 'country_code'], keep="first", inplace=True)
    d2[["latitude", "longitude"]] = d2[["latitude", "longitude"]].applymap(lambda x: '{0:.4f}'.format(x))
    d2.replace(np.nan, '', regex=True, inplace=True)
    d2 = d2.applymap(str)
    d2["location"] = d2["alternatenames"].str.findall(r'[A-Z]{3}')
    d2 = d2.explode("location")
    d2["unlocode"] = d2["country_code"] + d2["location"]
    return d2


def retrieve_unlocodes():
    df = pd.read_csv(unlocodes, names=names_locodes,
                     skiprows=1, usecols=locodes_use_cols,
                     dtype={'country_code': str, "location": str, "name": str,
                            "subdivision": str, "coordinates": str}
                     )
    df.replace(np.nan, '', regex=True, inplace=True)
    df = df.applymap(str)
    df["unlocode"] = df["country_code"] + df["location"]
    return df


def get_easy_match():
    global dcities, dunlocodes, list_unlocodes
    columns = ["location", "asciiname", "coordinates", "latitude", "longitude", "timezone","modification date"]

    easy_match = dunlocodes.set_index(['unlocode']).join(dcities.set_index(["unlocode"]), rsuffix='_other')
    easy_match.dropna(subset=["timezone"], inplace=True)
    easy_match["unlocode"] = easy_match["country_code"] + easy_match["location"]
    list_unlocodes = list(easy_match["unlocode"].unique())
    del easy_match["alternatenames"]

    easy_match.drop_duplicates("unlocode", keep="first", inplace=True)
    easy_match = easy_match.set_index(['name', 'country_code', "subdivision", "unlocode"])
    easy_match = easy_match.reindex()
    easy_match.to_csv("data/easy_%s.csv" % name, header=True, escapechar="\"", columns=columns, quoting=csv.QUOTE_NONE)

    dcities = dcities[-dcities['unlocode'].isin(list_unlocodes)]

    m.insert_records(easy_match[columns].to_dict('records'))
    return


def get_locations_match():
    global dcities, dunlocodes,list_unlocodes

    columns = ["unlocode", "location", "asciiname", "coordinates", "latitude", "longitude", "timezone",
               "modification date"]

    perfect_match = dunlocodes.set_index(['name', 'country_code', "subdivision"]).join(
        dcities.set_index(['name', 'country_code', "subdivision"]), rsuffix='_other')

    perfect_match = perfect_match[-perfect_match['unlocode'].isin(list_unlocodes)]

    perfect_match.dropna(subset=['timezone'], inplace=True)
    # perfect_match["unlocode"]=perfect_match["country_code"]+perfect_match["location"]
    list_unlocodes += list(perfect_match["unlocode"].unique())
    perfect_match[columns].to_csv("data/perfect_%s.csv" % name, index=True, quoting=csv.QUOTE_NONE)

    dcities = dcities[-dcities['unlocode'].isin(list_unlocodes)]
    m.insert_records(perfect_match[columns].to_dict('records'))
    return


def get_good_match():
    global dcities, dunlocodes

    dcities.drop_duplicates(subset=['name', 'country_code'], keep="first", inplace=True)

    good_match = dunlocodes.set_index(['name', 'country_code']).join(dcities.set_index(['name', 'country_code']),
                                                                     rsuffix='_other')
    good_match.dropna(subset=['timezone'], inplace=True)

    good_match = good_match[-good_match['unlocode'].isin(list_unlocodes)]

    columns = ["subdivision", "unlocode", "location", "asciiname", "coordinates", "latitude", "longitude", "timezone",
               "modification date"]
    good_match["subdivision"] = ""
    good_match[columns].to_csv("data/good_%s.csv" % name, index=True, quoting=csv.QUOTE_NONE)
    m.insert_records(good_match[columns].to_dict('records'))
    return


def process():
    get_easy_match()
    get_locations_match()
    get_good_match()
    return


if __name__ == "__main__":
    # global dcities, dunlocodes
    dcities = retrieve_all_countries()
    dunlocodes = retrieve_unlocodes()
    process()