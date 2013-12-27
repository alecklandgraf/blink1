#!/usr/local/bin/python
"""
happy_hour.py

green is happy hour time!

"""

from datetime import datetime
import sys
import time

from blink1 import Blink1


def happy_hour():
    b = Blink1()
    now = datetime.now()
    happy_hour_time = datetime(now.year, now.month, now.day, 15)

    if now < happy_hour_time:
        b.blue()
    else:
        b.green()
        b.blink(5)


def happy_hour_loop():
    while True:
        happy_hour()
        time.sleep(10)


def main():
    if '--loop' in sys.argv:
        happy_hour_loop()
    happy_hour()

if __name__ == "__main__":
    main()
