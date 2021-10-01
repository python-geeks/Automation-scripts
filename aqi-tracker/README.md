AQI Tracker
========================

aqi-tracker is a python script to retrive real-time air qualit index (AQI) value of a specific city from www.aqicn.org website.

Description
-----------
aqi-tracker lets the user retrieve real-time air quality index (AQI) value of a specific city from www.aqicn.org website. The python script will send a query to the webiste containing a city name and access token. If the query request is successful, the website returs json object containing real-time values.

Pre-Requisites
==============

Retriving Data From AQICN Website
----------------------------------
* Access-Token: User have to get an access token by registering on http://aqicn.org/data-platform/register/"
* if no access-token is provided then 'demo' access-token will be used and with 'demo' access token only Shanghai's air quality values can be retrieved."

 Retrived JSON Data:
 -------------------
```json
{
    "status":"ok",
    "data":{
        "aqi":74,
        "idx":1437,
        "attributions":[
            {
                "url":"https: //sthj.sh.gov.cn/",
                "name":"Shanghai Environment Monitoring Center(上海市环境监测中心)"
            },
            {
                "url":"http://106.37.208.233:20035/emcpublish/",
                "name":"China National Urban air quality real-time publishing platform (全国城市空气质量实时发布平台)"
            },
            {
                "url":"https://china.usembassy-china.org.cn/embassy-consulates/shanghai/air-quality-monitor-stateair/",
                "name":"U.S. Consulate Shanghai Air Quality Monitor"
            },
            {
                "url":"https://waqi.info/",
                "name":"World Air Quality Index Project"
            }
        ],
        "city":{
            "geo":[
                31.2047372,
                121.4489017
            ],
            "name":"Shanghai (上海)",
            "url":"https://aqicn.org/city/shanghai"
        },
        "dominentpol":"pm25",
        "iaqi":{
            "co":{
                "v":5.5
            },
            "h":{
                "v":55
            },
            "no2":{
                "v":13.8
            },
            "o3":{
                "v":48.4
            },
            "p":{
                "v":1010
            },
            "pm10":{
                "v":31
            },
            "pm25":{
                "v":74
            },
            "so2":{
                "v":2.6
            },
            "t":{
                "v":30
            },
            "w":{
                "v":2.5
            }
        },
        "time":{
            "s":"2021-10-01 12: 00: 00",
            "tz":"+08: 00",
            "v":1633089600,
            "iso":"2021-10-01T12: 00: 00+08: 00"
        },
        "forecast":{
            "daily":{
                "o3":[
                    {
                        "avg":1,
                        "day":"2021-09-29",
                        "max":4,
                        "min":1
                    },
                    {
                        "avg":3,
                        "day":"2021-09-30",
                        "max":10,
                        "min":1
                    },
                    {
                        "avg":1,
                        "day":"2021-10-01",
                        "max":3,
                        "min":1
                    },
                    {
                        "avg":1,
                        "day":"2021-10-02",
                        "max":13,
                        "min":1
                    },
                    {
                        "avg":5,
                        "day":"2021-10-03",
                        "max":20,
                        "min":1
                    },
                    {
                        "avg":2,
                        "day":"2021-10-04",
                        "max":11,
                        "min":1
                    },
                    {
                        "avg":2,
                        "day":"2021-10-05",
                        "max":8,
                        "min":1
                    },
                    {
                        "avg":1,
                        "day":"2021-10-06",
                        "max":1,
                        "min":1
                    }
                ],
                "pm10":[
                    {
                        "avg":78,
                        "day":"2021-09-30",
                        "max":126,
                        "min":29
                    },
                    {
                        "avg":102,
                        "day":"2021-10-01",
                        "max":123,
                        "min":73
                    },
                    {
                        "avg":83,
                        "day":"2021-10-02",
                        "max":123,
                        "min":56
                    },
                    {
                        "avg":51,
                        "day":"2021-10-03",
                        "max":57,
                        "min":46
                    },
                    {
                        "avg":49,
                        "day":"2021-10-04",
                        "max":56,
                        "min":46
                    },
                    {
                        "avg":73,
                        "day":"2021-10-05",
                        "max":123,
                        "min":46
                    },
                    {
                        "avg":94,
                        "day":"2021-10-06",
                        "max":179,
                        "min":28
                    },
                    {
                        "avg":60,
                        "day":"2021-10-07",
                        "max":76,
                        "min":46
                    }
                ],
                "pm25":[
                    {
                        "avg":164,
                        "day":"2021-09-30",
                        "max":252,
                        "min":69
                    },
                    {
                        "avg":207,
                        "day":"2021-10-01",
                        "max":252,
                        "min":159
                    },
                    {
                        "avg":158,
                        "day":"2021-10-02",
                        "max":177,
                        "min":127
                    },
                    {
                        "avg":127,
                        "day":"2021-10-03",
                        "max":159,
                        "min":85
                    },
                    {
                        "avg":108,
                        "day":"2021-10-04",
                        "max":141,
                        "min":69
                    },
                    {
                        "avg":150,
                        "day":"2021-10-05",
                        "max":252,
                        "min":85
                    },
                    {
                        "avg":168,
                        "day":"2021-10-06",
                        "max":252,
                        "min":68
                    },
                    {
                        "avg":137,
                        "day":"2021-10-07",
                        "max":177,
                        "min":89
                    }
                ],
                "uvi":[
                    {
                        "avg":0,
                        "day":"2021-09-30",
                        "max":0,
                        "min":0
                    },
                    {
                        "avg":1,
                        "day":"2021-10-01",
                        "max":6,
                        "min":0
                    },
                    {
                        "avg":1,
                        "day":"2021-10-02",
                        "max":6,
                        "min":0
                    },
                    {
                        "avg":2,
                        "day":"2021-10-03",
                        "max":7,
                        "min":0
                    },
                    {
                        "avg":1,
                        "day":"2021-10-04",
                        "max":6,
                        "min":0
                    },
                    {
                        "avg":2,
                        "day":"2021-10-05",
                        "max":7,
                        "min":0
                    }
                ]
            }
        },
        "debug":{
            "sync":"2021-10-01T13: 44: 12+09: 00"
        }
    }
}
```

Dependencies
------------
aqi-tracker depends on third party library and you will first need to install the application's dependencies. 
> urrlib

Running the Script
--------------------
Download the project source code directly or clone the repository on GitHub  Navigate to the folder with the source code on your machine in a terminal window.
```py
    $ 'usage: python aqi-tracker.py [-c city] [-a accesstoken] [-h help]'  
    "city: name of the city"
    "accesstoken: You need to get access token by registering on http://aqicn.org/data-platform/register/"
    "help: description and help"
```
AQI Guide and References
------------------------
* http://aqicn.org/faq/2015-09-06/ozone-aqi-using-concentrations-in-milligrams-or-ppb/
* http://aqicn.org/faq/2015-03-15/air-quality-nowcast-a-beginners-guide/
* http://aqicn.org/faq/2016-08-10/ozone-aqi-scale-update/
* https://en.wikipedia.org/wiki/Air_pollution
