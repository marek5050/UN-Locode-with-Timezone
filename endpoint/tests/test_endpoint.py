import endpoint.main as e

def test_main():
    d = {"unlocode":"USWAT"}
    r = e.main(d)
    a = {'result': [{'asciiname': 'Waterbury',
             'city': 'Waterbury',
             'coordinates': '',
             'country_code': 'US',
             'latitude': '41.5581',
             'location': 'WAT',
             'longitude': '-73.0515',
             'modification date': '2017-05-23',
             'subdivision': 'CT',
             'timezone': 'America/New_York',
             'unlocode': 'USWAT'}]
         }
    assert r == a

def test_main_2():
    d = {"unlocode":"TWKHH"}
    a = {'result': [{'asciiname': 'Kaohsiung',
             'city': 'Kaohsiung',
             'coordinates': '',
             'subdivision': '',
             'latitude': '22.6163',
             'location': 'KHH',
             'longitude': '120.3133',
             'modification date': '2017-09-26',
             'country_code': 'TW',
             'timezone': 'Asia/Taipei',
             'unlocode': 'TWKHH'}]}
    r = e.main(d)
    assert r == a