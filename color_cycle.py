#!/usr/local/bin/python
"""
color_cycle.py
"""

from time import time
from subprocess import call
from random import randrange


def get_color():
    choices = ['red', 'green', 'blue', 'on']
    return choices[randrange(len(choices))]


def set_color(color='green'):
    call(['../blink1-tool', '--%s' % color])


def delay(default=5):
    time.wait(default)


def cycle():
    color = get_color()
    set_color(color)


def main():
    while True:
        delay()
        cycle()

if __name__ == "__main__":
    main()
