from datetime import datetime
import pytz
import pymongo


class MongoQuery:
    db = None
    collection = None
    uri = "mongodb://%s@oceans-shard-00-00.iotwb.mongodb.net:27017,oceans-shard-00-01.iotwb.mongodb.net:27017,oceans-shard-00-02.iotwb.mongodb.net:27017/timezones?ssl=true&replicaSet=atlas-10a87j-shard-0&authSource=admin&retryWrites=true&w=majority"

    def __init__(self, u_p):
        client = pymongo.MongoClient(self.uri % (u_p))
        self.db = client.get_database("oceandb")
        self.collection = self.db["timezones"]

    def query(self, unlocode="NONE", name="NONE"):
        items = list(self.collection.find({"unlocode": {'$regex': unlocode,  '$options': 'i'}}, {"_id": 0}).limit(10))
        if len(items) == 0:
            items = list(self.collection.find({"city": {'$regex': name, '$options': 'i'}}, {"_id": 0}).limit(10))

        return items


def main(d):
    unlocode = d.get("unlocode")
    city = d.get("city")
    u_p = d.get("u_p", "NONE")
    mq = MongoQuery(u_p)
    tzs = mq.query(unlocode, city)

    for item in tzs:
        tz = pytz.timezone(item.get("timezone"))
        item["current_time"] = datetime.now(tz).isoformat(sep="T", timespec='minutes')

    resp = {"result": tzs}

    return resp