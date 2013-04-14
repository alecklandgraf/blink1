"""
Blink1 class/lib for blink1-tool and device
usage:
        from blink1 import Blink1
        blinker = Blink1()
        blinker.random(5)
"""

from subprocess import call
import time


class Blink1():
    """Blink1"""

    blink1_tool_file_path = 'lib/blink1-tool'
    quite_mode = True

    def blink(self, number_of_blinks, rgb_color=None, hex_color=None):
        if rgb_color or hex_color:
            self.rgb(rgb_color=rgb_color, hex_color=hex_color)
        self._call_blink1_tool('--blink', str(number_of_blinks))

    def random(self, number_of_blinks):
        self._call_blink1_tool('--random', str(number_of_blinks))

    def rgb(self, rgb_color, hex_color=None):
        ''' rgb_color should be a tuple or list of strings or ints i.e. ('0xff', '0', '00') or [255,'0', '255]
            hex_colorh should be a string i.e. '#FF0000'
        '''
        if rgb_color:
            if len(rgb_color != 3):
                raise Exception('rgb_color takes 3 arguments')
            rgb_string = '%s,%s,%s' % (rgb_color[0], rgb_color[1], rgb_color[2], )
            self._call_blink1_tool('--rgb', rgb_string)

    def on(self):
        self._call_blink1_tool('--on')

    def off(self):
        self._call_blink1_tool('--off')

    def red(self):
        self._call_blink1_tool('--red')

    def green(self):
        self._call_blink1_tool('--green')

    def blue(self):
        self._call_blink1_tool('--blue')

    def _call_blink1_tool(self, *args):
        if all(isinstance(item, basestring) for item in args):
            call_list = list(args)
            call_list.insert(0, self.blink1_tool_file_path)
            if self.quite_mode:
                call_list.append('-q')
            call(call_list)
        else:
            raise TypeError('arguments must be strings')

    def delay(self, delay=5):
        time.sleep(delay)
