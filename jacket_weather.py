"""
jacket_weather.py

blue if jacket weather
red if not jacket weather

uses http://openweathermap.org/ for FREE weather data!!
"""

import sys
import time
from time import strftime
from json import load
from urllib2 import urlopen
import os

from blink1 import Blink1


STATION = '2274'  # Portland, OR KPDX
CITY = '5746545'  # Portland
OPENWEATHERMAP_URL = 'http://api.openweathermap.org/data/2.1/weather/city/%s?type=json'
OPENWEATHERMAP_FORECAST_URL = 'http://api.openweathermap.org/data/2.1/forecast/city/%s?type=json'
ONE_MIN = 60 * 1
FIVE_MIN = 60 * 5
TEN_MIN = 60 * 10
FIFTEEN_MIN = 60 * 15
TEMP_THRESHOLD_F = 50

DELAY = ONE_MIN


def jacket_weather():
    blinker = Blink1()
    try:
        data = urlopen(OPENWEATHERMAP_URL % CITY)
        weather = load(data)
        current_temp_F = (float(weather['main']['temp']) - 273.15) * 9 / 5 + 32
        current_condition = weather['weather'][0]['description']
        current_condition_code = weather['weather'][0]['id']
    except:
        print "Error: couldn't get weather data"
        current_temp_F = "unknown"
        current_condition = "unknown"
        current_condition_code = -1

    print "Current weather for your location is %s degrees F and %s @ %s" % (current_temp_F, current_condition, strftime("%Y-%m-%d %H:%M:%S", time.localtime()), )
    os.system('echo -e "\033];temp is %s\007"' % current_temp_F)
    if current_temp_F > TEMP_THRESHOLD_F:
        if current_condition_code < 700:
            blinker.blink(DELAY, rgb_color=(255, 150, 0))
            blinker.orange()
        else:
            blinker.orange()
            blinker.delay(DELAY)
    else:
        if current_condition_code < 700:
            blinker.blink(DELAY, rgb_color=(0, 0, 255))
            blinker.blue()
        else:
            blinker.blue()
            blinker.delay(DELAY)

    if current_temp_F == "unknown":
        blinker.random(35)


def jacket_weather_loop():
    while True:
        jacket_weather()


def main():
    if '--loop' in sys.argv:
        jacket_weather_loop()
    jacket_weather()

if __name__ == "__main__":
    main()
