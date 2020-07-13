# UN Locodes with coordinates and timezones 
![.github/workflows/actions.yml](https://github.com/marek5050/UN-Locode-with-Timezone/workflows/.github/workflows/actions.yml/badge.svg)

The repository contains the latest UN-Locode-with-Timezone information.


## Sources
`The GeoNames geographical database covers all countries and contains over eleven million placenames that are available for download free of charge.`
https://www.geonames.org


`The "United Nations Code for Trade and Transport Locations" is commonly more known as "UN/LOCODE". Although managed and maintained by the UNECE, it is the product of a wide collaboration in the framework of the joint trade facilitation effort undertaken within the United Nations.`

https://www.unece.org/cefact/locode/service/location.html
Last updated:  Mon Jul 13 12:44:39 EDT 2020
```
==> ./data/all_data.csv <==
name,country_code,subdivision,unlocode,location,asciiname,coordinates,latitude,longitude,timezone,modification date
Andorra la Vella,AD,,ADALV,ALV,Andorra la Vella,4230N 00131E,42.5078,1.5211,Europe/Andorra,2020-03-03
Al Ain,AE,,AEAAN,AAN,Al Ain City,,24.1917,55.7606,Asia/Dubai,2019-05-29
Abu Dhabi,AE,AZ,AEAUH,AUH,Abu Dhabi,2428N 05422E,24.4512,54.3970,Asia/Dubai,2019-09-05
Dubai,AE,DU,AEDXB,DXB,Dubai,2515N 05516E,25.0772,55.3093,Asia/Dubai,2019-08-28
Al Fujayrah,AE,FU,AEFJR,FJR,Al Fujairah City,2507N 05620E,25.1164,56.3414,Asia/Dubai,2019-05-29
Ras Al Khor,AE,DU,AERAK,RAK,Ras Al Khaimah City,2517N 05534E,25.7895,55.9432,Asia/Dubai,2019-09-09
Ras al Khaimah,AE,,AERKT,RKT,Ras Al Khaimah City,2547N 05557E,25.7895,55.9432,Asia/Dubai,2019-09-09
Sharjah,AE,SH,AESHJ,SHJ,Sharjah,2521N 05523E,25.3374,55.4121,Asia/Dubai,2019-09-05
Bamian,AF,,AFBIN,BIN,Bamyan,,34.8216,67.8273,Asia/Kabul,2020-06-09

==> ./data/easy_cities15000.csv <==
name,country_code,subdivision,unlocode,location,asciiname,coordinates,latitude,longitude,timezone,modification date
Andorra la Vella,AD,,ADALV,ALV,Andorra la Vella,4230N 00131E,42.5078,1.5211,Europe/Andorra,2020-03-03
Al Ain,AE,,AEAAN,AAN,Al Ain City,,24.1917,55.7606,Asia/Dubai,2019-05-29
Abu Dhabi,AE,AZ,AEAUH,AUH,Abu Dhabi,2428N 05422E,24.4512,54.3970,Asia/Dubai,2019-09-05
Dubai,AE,DU,AEDXB,DXB,Dubai,2515N 05516E,25.0772,55.3093,Asia/Dubai,2019-08-28
Al Fujayrah,AE,FU,AEFJR,FJR,Al Fujairah City,2507N 05620E,25.1164,56.3414,Asia/Dubai,2019-05-29
Ras Al Khor,AE,DU,AERAK,RAK,Ras Al Khaimah City,2517N 05534E,25.7895,55.9432,Asia/Dubai,2019-09-09
Ras al Khaimah,AE,,AERKT,RKT,Ras Al Khaimah City,2547N 05557E,25.7895,55.9432,Asia/Dubai,2019-09-09
Sharjah,AE,SH,AESHJ,SHJ,Sharjah,2521N 05523E,25.3374,55.4121,Asia/Dubai,2019-09-05
Bamian,AF,,AFBIN,BIN,Bamyan,,34.8216,67.8273,Asia/Kabul,2020-06-09

==> ./data/good_cities15000.csv <==
name,country_code,subdivision,unlocode,location,asciiname,coordinates,latitude,longitude,timezone,modification date
's-Gravenzande,NL,,NLGRZ,GRZ,'s-Gravenzande,5200N 00410E,52.0017,4.1653,Europe/Amsterdam,2017-10-17
's-Hertogenbosch,NL,,NLHTB,HTB,'s-Hertogenbosch,5142N 00519E,51.6992,5.3042,Europe/Amsterdam,2020-01-13
Aalen,DE,,DEAAL,AAL,Aalen,,48.8378,10.0933,Europe/Berlin,2014-05-09
Aalsmeer,NL,,NLAAM,AAM,Aalsmeer,,52.2592,4.7597,Europe/Amsterdam,2017-10-17
Aalst,BE,,BEAAB,AAB,Aalst,5056N 00402E,50.9360,4.0355,Europe/Brussels,2020-06-01
Aalten,NL,,NLLTE,LTE,Aalten,,51.9250,6.5806,Europe/Amsterdam,2017-10-17
Aalter,BE,,BEAAL,AAL,Aalter,5105N 00327E,51.0902,3.4469,Europe/Brussels,2019-01-17
Aarschot,BE,,BEAAS,AAS,Aarschot,5059N 00450E,50.9871,4.8369,Europe/Brussels,2012-01-18
Abadeh,IR,,IRJBD,JBD,Abadeh,3002N 05232E,31.1608,52.6506,Asia/Tehran,2020-06-30

==> ./data/perfect_cities15000.csv <==
name,country_code,subdivision,unlocode,location,asciiname,coordinates,latitude,longitude,timezone,modification date
Aarau,CH,AG,CHAAR,AAR,Aarau,,47.3925,8.0442,Europe/Zurich,2020-06-29
Aberdeen,US,WA,USGHR,GHR,Aberdeen,4658N 12349W,46.9754,-123.8157,America/Los_Angeles,2017-03-09
Abington,US,MA,USUUM,UUM,Abington,4207N 07056W,42.1048,-70.9453,America/New_York,2017-05-23
Acton,US,MA,USUAH,UAH,Acton,,42.4851,-71.4328,America/New_York,2017-05-23
Acworth,US,GA,USAWR,AWR,Acworth,,34.0663,-84.6784,America/New_York,2017-03-09
Addison,US,IL,USUAP,UAP,Addison,,41.9317,-87.9890,America/Chicago,2017-05-23
Addison,US,TX,USDDX,DDX,Addison,3258N 09650W,32.9618,-96.8292,America/Chicago,2017-03-09
Adelanto,US,CA,USADU,ADU,Adelanto,3434N 11724W,34.5828,-117.4092,America/Los_Angeles,2017-03-09
Adelphi,US,MD,USA9D,A9D,Adelphi,3859N 07658W,39.0032,-76.9719,America/New_York,2011-05-14
```
