from os import mkdir
from os.path import exists
from zipfile import ZipFile

import numpy as np
import pandas as pd
import urllib.request as request
from io import BytesIO

datadir = "data"
if not exists(datadir):
    mkdir(datadir)

if not exists("scripts/tmp"):
    mkdir("scripts/tmp")

unlocodes = "https://github.com/marek5050/UN-LOCODE/raw/master/data/code-list.csv"
cities = "http://download.geonames.org/export/dump/%s.zip"

names_cities = "geonameid,name,asciiname,alternatenames,latitude,longitude,feature class,feature code,country_code,cc2,subdivision,admin2 code,admin3 code,admin4 code,population,elevation,dem,timezone,modification date".split(",")
cities_use_cols  = "name,asciiname,latitude,longitude,country_code,subdivision,timezone,modification date".split(",")
names_locodes="change,country_code,location,name,asciiname,subdivision,status,function,date,iata,coordinates,remarks".split(",")
locodes_use_cols="country_code,location,name,subdivision,coordinates".split(",")
name = "allCountries"


def retrieve_all_countries():
    z = request.urlopen(cities % name)
    myzip = ZipFile(BytesIO(z.read())).extract('%s.txt' % name)
    d2 = pd.read_csv(myzip, delimiter="\t",
                     names=names_cities,
                     usecols=cities_use_cols,
                     dtype={'name': str,"asciiname": str,"latitude":float,
                            "longitude":float,"country_code":str,"subdivision":str, "timezone":str,"modification date":str})
    d2.drop_duplicates(subset=['name','subdivision','country_code'], keep="first", inplace = True)
    d2[["latitude","longitude"]]= d2[["latitude","longitude"]].applymap(lambda x: '{0:.4f}'.format(x))
    d2.replace(np.nan, '', regex=True, inplace=True)
    d2 = d2.applymap(str)
    return d2

def retrieve_unlocodes():
    df = pd.read_csv(unlocodes, names=names_locodes,
                     skiprows=1, usecols=locodes_use_cols,
                     dtype={'country_code': str, "location": str, "name": str,
                            "subdivision": str, "coordinates":str }
                     )
    df.replace(np.nan, '', regex=True, inplace=True)
    df = df.applymap(str)
    df["unlocode"] = df["country_code"] + df["location"]
    return df

def process(dcities, dunlocodes):
    perfect_match = dunlocodes.set_index(['name','country_code',"subdivision"]).join(dcities.set_index(['name','country_code',"subdivision"]), rsuffix='_other')
    perfect_match.dropna(subset=['timezone'], inplace=True)

    columns = ["unlocode","location","asciiname","coordinates","latitude","longitude","timezone","modification date"]
    perfect_match[columns].to_csv("data/perfect_%s.csv" % name, index=True)

    dcities.drop_duplicates(subset=['name', 'country_code'], keep="first", inplace=True)
    good_match = dunlocodes.set_index(['name','country_code']).join(dcities.set_index(['name','country_code']), rsuffix='_other')
    good_match.dropna(subset=['timezone'], inplace=True)

    columns = ["subdivision","unlocode","location","asciiname","coordinates","latitude","longitude","timezone","modification date"]
    good_match = good_match[-good_match['unlocode'].isin(perfect_match["unlocode"].unique())]
    good_match["subdivision"]=""
    good_match[columns].to_csv("data/good_%s.csv" % name, index=True)


if __name__ == "__main__":
    dcities= retrieve_all_countries()
    dunlocodes = retrieve_unlocodes ()
    process(dcities, dunlocodes)
