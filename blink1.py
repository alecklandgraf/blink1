"""
Blink1 class
"""

from subprocess import call


class Blink1():
    """Blink1"""

    blink1_tool_file_path = 'lib/blink1-tool'

    def blink(self, number_of_blinks, rgb_color=None):
        if rgb_color:
            self.rgb(rgb_color)
        self._call_blink1_tool('--blink %s' % number_of_blinks)

    def random(self, number_of_blinks):
        self._call_blink1_tool('--random', str(number_of_blinks))

    def rgb(self, rgb_color):
        self._call_blink1_tool('--rgb %s' % rgb_color)

    def _call_blink1_tool(self, *args):
        call_list = list(args)
        call_list.insert(0, self.blink1_tool_file_path)
        call(call_list)
