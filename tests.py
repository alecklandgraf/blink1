#!/usr/local/bin/python
'''
tests.py
'''

from blink1 import Blink1


def rgb_test(blink_device):
    blink_device.rgb(rgb_color=(255, 0, 0))
    print "return code", blink_device.command_output
    blink_device.delay(1)
    blink_device.rgb(rgb_color=(0, 255, 0))
    blink_device.delay(1)
    blink_device.rgb((0, 0, 255))
    blink_device.delay(1)
    blink_device.rgb()
    blink_device.rgb(hex_color='#ff0000')
    blink_device.delay(1)
    blink_device.rgb(hex_color='#1072B9')
    blink_device.delay(1)
    blink_device.rgb(hex_color='#959595')
    blink_device.delay(1)
    blink_device.rgb(hex_color='#8BC542')
    blink_device.delay(1)
    blink_device.rgb(hex_color='1072B9')


def _hex_to_rgb_test(blink_device):
    assert blink_device._hex_to_rgb('#ff0000') == (255, 0, 0)
    assert blink_device._hex_to_rgb('#00ff00') == (0, 255, 0)
    assert blink_device._hex_to_rgb('#0000FF') == (0, 0, 255)


def main():
    blinker = Blink1()
    blinker.quite_mode = False
    rgb_test(blinker)
    _hex_to_rgb_test(blinker)


if __name__ == "__main__":
    main()
