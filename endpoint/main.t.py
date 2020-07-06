import pandas as pd


def main(d):
    unlocode = d.get("unlocode")
    city = d.get("city")
    names = "city,country_code,subdivision,unlocode,location,asciiname,coordinates,latitude,longitude,timezone,modification date".split(
        ",")
    frame = pd.DataFrame([x.split(",") for x in db.split('\n')[1:]], columns=names)
    resp = {"result": []}

    if unlocode:
        resp["result"] = frame[frame['unlocode'].str.contains(unlocode) == True][:20].to_dict("records")
    elif city:
        resp["result"] = frame[frame['terminal_code'].str.contains(city) == True][:20].to_dict("records")

    return resp
