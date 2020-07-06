import endpoint.main as e

def test_main():
    d = {"unlocode":"ZAPLZ"}
    # ZAPLZ,,TNPE,TRANSNET PORT TERMINALS PORT ELIZABETH,TRANSNET PORT TERMINALS,S 33°57'30",E 025°38'17",,2004-05-31 00:00:00,,https://www..transnetportterminals..net/pages/default..aspx,,
    # UNLOCODE,Alternative UNLOCODEs,Terminal Code,Terminal Facility Name,Terminal Company Name,Latitude (DMS),Longitude (DMS),Last change,Valid from,Valid until,Terminal Website,Terminal Address,Remarks
    r = e.main(d)
    a = {
        "locations":[
            {"unlocode":"ZAPLZ",
             "alternative":"",
             "terminal_code":"TNPE",
             "terminal_facility_name":"TRANSNET PORT TERMINALS PORT ELIZABETH",
             "terminal_company_name": "TRANSNET PORT TERMINALS",
             "latitude":"S 33°57'30",
             "longitude":"E 025°38'17",
             "last_change":"",
             "valid_from":"2004-05-31 00:00:00",
             "valid_until":"",
             'terminal_website': 'https://www.transnetportterminals.net/pages/default.aspx',
             "terminal_address":"",
             "remarks":""}
        ]
    }
    assert r == a

def test_main_2():
    d = {"unlocode":"TWKHH"}
    r = e.main(d)
    assert len(r["locations"]) > 2

def test_main_smdg_lookup():
    d = {"terminal_code":"PSABT"}
    r = e.main(d)
    assert len(r["locations"]) >= 1