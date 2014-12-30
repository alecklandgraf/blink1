"""
color_cycle.py
"""

import time
import sys
from random import randrange

from blink1 import Blink1


def get_color():
    choices = ['red', 'green', 'blue', 'on']
    return choices[randrange(len(choices))]


def set_color(blink1_device, color='green'):
    blink_color_setter = getattr(blink1_device, color)
    blink_color_setter()


def delay(default=5):
    time.sleep(default)


def cycle(blink1_device):
    color = get_color()
    set_color(blink1_device, color)


def chrismas_mode(blink1_device):
    while True:
        set_color(blink1_device, 'green')
        delay()
        set_color(blink1_device, 'red')
        delay()


def main():
    blinker = Blink1()
    if 'christmas' in sys.argv:
        chrismas_mode(blinker)
    while True:
        cycle(blinker)
        delay()

if __name__ == "__main__":
    main()
