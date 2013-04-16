"""
Blink1 class/lib for blink1-tool and device
    see tests.py for examples
"""

import os
import time


class Blink1():
    """Blink1"""

    blink1_tool_file_path = 'lib/blink1-tool'
    quite_mode = True
    command_output = ''

    def blink(self, number_of_blinks, rgb_color=None, hex_color=None):
        if rgb_color or hex_color:
            if hex_color:
                rgb_color = self._hex_to_rgb(str(hex_color))
            rgb_string = self._construct_rgb_string(rgb_color)
            self._call_blink1_tool('--rgb', rgb_string, '--blink', str(number_of_blinks))
        else:
            self._call_blink1_tool('--blink', str(number_of_blinks))

    def random(self, number_of_blinks):
        self._call_blink1_tool('--random', str(number_of_blinks))

    def rgb(self, rgb_color=None, hex_color=None):
        ''' rgb_color should be a tuple or list of strings or ints i.e. ('0xff', '0', '00') or [255,'0', '255]
            hex_color should be a string i.e. '#FF0000'
        '''
        if hex_color:
            rgb_color = self._hex_to_rgb(str(hex_color))
        if rgb_color:
            rgb_string = self._construct_rgb_string(rgb_color)
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

    def orange(self):
        self.rgb((255, 150, 0))

    def delay(self, delay=5):
        time.sleep(delay)

    def _call_blink1_tool(self, *args):
        if all(isinstance(item, basestring) for item in args):
            arg_list = list(args)
            arg_list.insert(0, self.blink1_tool_file_path)
            if self.quite_mode:
                arg_list.append('-q')

            arg_string = ''
            for arg in arg_list:
                arg_string += arg + ' '

            child = os.popen(arg_string)
            self.command_output = child.read()
            err = child.close()
            if err:
                raise RuntimeError('%s failed with exit code %d' % (arg_string, err))
        else:
            raise TypeError('arguments must be strings')

    def _hex_to_rgb(self, value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv / 3], 16) for i in range(0, lv, lv / 3))

    def _construct_rgb_string(self, rgb_color):
        if len(rgb_color) != 3:
            raise Exception('rgb_color is a tuple of three ints or strings')

        return '%s,%s,%s' % (rgb_color[0], rgb_color[1], rgb_color[2])
