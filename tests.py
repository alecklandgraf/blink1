#!/usr/local/bin/python
'''
tests.py
'''

from blink1 import Blink1


def rgb_test(blink_device):
    blink_device.rgb(rgb_color=[255, 0, 0])


def main():
    blinker = Blink1()
    rgb_test(blinker)


if __name__ == "__main__":
    main()
