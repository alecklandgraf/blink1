#!/usr/local/bin/python
'''
tests.py
'''

from blink1 import Blink1


def main():
    if '--loop' in sys.argv:
        jacket_weather_loop()
    jacket_weather()

if __name__ == "__main__":
    main()
