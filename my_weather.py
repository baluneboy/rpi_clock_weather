#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
import syslog
import urllib.request, urllib.parse, urllib.error
from my_config import api_key, loc_id


def get_my_weather():
    service_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = service_url + urllib.parse.urlencode({'id': loc_id, 'APPID': api_key, 'units': 'imperial'})
    url_read = urllib.request.urlopen(url).read()
    data_json = json.loads(url_read)
    temp = int(round(float(data_json['main']['temp'])))
    humidity = int(data_json['main']['humidity'])
    condition = data_json['weather'][0]['description']
    return '%d%sF %d%%\n%s' % (temp, u'\N{DEGREE SIGN}', humidity, condition)

 
def get_weather():
    err = None
    try:
        msg = get_my_weather()
    except ValueError:
        msg = "Value error, so something was not a valid value."
    except:
        msg = "Unhandled error:", sys.exc_info()[0]
    if err is not None:
    	syslog.syslog(syslog.LOG_ERR, 'my_weather::%s' % sys.exc_info()[0])

    return msg


if __name__ == '__main__':
    s = get_weather() 
    print(s)

