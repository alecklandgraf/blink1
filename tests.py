#!/usr/local/bin/python
'''
tests.py
'''

from blink1 import Blink1


def rgb_test(blink_device):
    blink_device.rgb(rgb_color=(255, 0, 0))
    blink_device.delay(5)
    blink_device.rgb(rgb_color=(0, 255, 0))
    blink_device.delay(5)
    blink_device.rgb((0, 0, 255))
    blink_device.delay(1)
    blink_device.rgb()


def main():
    blinker = Blink1()
    blinker.quite_mode = False
    rgb_test(blinker)


if __name__ == "__main__":
    main()
