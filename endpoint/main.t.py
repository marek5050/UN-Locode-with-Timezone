import pandas as pd

def main(d):
    unlocode = d.get("unlocode")
    terminal_code = d.get("terminal_code")
    names = ["unlocode","alternative","terminal_code",
             "terminal_facility_name","terminal_company_name",
             "latitude","longitude","last_change",
             "valid_from","valid_until","terminal_website",
             "terminal_address","remarks"]
    frame = pd.DataFrame([x[1:-1].split("','",12) for x in db.split('\n')[2:]],columns=names)
    resp = {"locations":[]}
    frame['latitude'] = frame['latitude'].str.replace("\'\'","'")
    frame['latitude'] = frame['latitude'].str.replace('\"',"")
    frame['longitude'] = frame['longitude'].str.replace("\'\'","'")
    frame['longitude'] = frame['longitude'].str.replace('\"',"")
    if unlocode:
        resp["locations"] = frame[frame['unlocode'].str.contains(unlocode)==True][:20].to_dict("records")
    elif terminal_code:
        resp["locations"] =   frame[frame['terminal_code'].str.contains(terminal_code)==True][:20].to_dict("records")

    return resp