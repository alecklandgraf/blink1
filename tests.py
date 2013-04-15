#!/usr/local/bin/python
'''
tests.py
'''

from blink1 import Blink1


def rgb_test(blink_device):
    blink_device.rgb(rgb_color=(255, 0, 0))
    assert "set dev:0 to rgb:0xff,0x00,0x00 over 300 msec" in blink_device.command_output
    blink_device.delay(1)
    blink_device.rgb(rgb_color=(0, 255, 0))
    assert "set dev:0 to rgb:0x00,0xff,0x00 over 300 msec" in blink_device.command_output
    blink_device.delay(1)
    blink_device.rgb((0, 0, 255))
    assert "set dev:0 to rgb:0x00,0x00,0xff over 300 msec" in blink_device.command_output
    blink_device.delay(1)
    blink_device.rgb()
    assert "set dev:0 to rgb:0x00,0x00,0xff over 300 msec" in blink_device.command_output
    blink_device.rgb(hex_color='#ff0000')
    assert "set dev:0 to rgb:0xff,0x00,0x00 over 300 msec" in blink_device.command_output
    blink_device.delay(1)
    blink_device.rgb(hex_color='#1072B9')
    assert "set dev:0 to rgb:0x10,0x72,0xb9 over 300 msec" in blink_device.command_output
    blink_device.delay(1)
    blink_device.rgb(hex_color='#959595')
    assert "set dev:0 to rgb:0x95,0x95,0x95 over 300 msec" in blink_device.command_output
    blink_device.delay(1)
    blink_device.rgb(hex_color='#8BC542')
    assert "set dev:0 to rgb:0x8b,0xc5,0x42 over 300 msec" in blink_device.command_output
    blink_device.delay(1)
    blink_device.rgb(hex_color='1072B9')
    assert "set dev:0 to rgb:0x10,0x72,0xb9 over 300 msec" in blink_device.command_output


def _hex_to_rgb_test(blink_device):
    assert blink_device._hex_to_rgb('#ff0000') == (255, 0, 0)
    assert blink_device._hex_to_rgb('#00ff00') == (0, 255, 0)
    assert blink_device._hex_to_rgb('#0000FF') == (0, 0, 255)


def orange_test(blink_device):
    blink_device.orange()


def main():
    blinker = Blink1()
    blinker.quite_mode = False
    rgb_test(blinker)
    orange_test(blinker)
    _hex_to_rgb_test(blinker)


if __name__ == "__main__":
    main()
