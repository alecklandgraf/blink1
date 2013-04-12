#!/usr/local/bin/python
"""
weather_blink.py

blue if jacket weather
red if not jacket weather

uses http://openweathermap.org/ for FREE weather data!!
"""

from json import load
from urllib2 import urlopen

from blink1 import Blink1


STATION = '2274'  # Portland, OR KPDX
OPENWEATHERMAP_URL = 'http://api.openweathermap.org/data/2.1/weather/station/%s?type=json'
FIVE_MIN = 60 * 5
TEMP_THRESHOLD_F = 55


def main():
    blinker = Blink1()
    data = urlopen(OPENWEATHERMAP_URL % STATION)
    weather = load(data)
    current_temp_F = (float(weather['main']['temp']) - 273.15) * 9/5 + 32

    if current_temp_F > TEMP_THRESHOLD_F:
        blinker.red()
    else:
        blinker.blue()


if __name__ == "__main__":
    main()
