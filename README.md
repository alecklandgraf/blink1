blink1
======

python scripts and library for your blink1

http://thingm.com/products/blink-1.html

## setup
set your `blink1_tool_file_path` in `blink1.py`

or 

clone this repo 

## examples
get the device
```
from blink1 import Blink1
b = Blink1()
```
call the blink method
```
b.blink(10, hex_color='#8BC542')
```
call blue and wait for 10 seconds
```
b.blue()
b.delay(10)
```

## jacket_weather.py
`./jacket_weather.py` or `python jacket_weather.py`

`./jacket_weather.py --loop` to keep running, updates every minute

orange if it's warm (>50F), blue if it's cold,
blinks if it's raining

uses http://openweathermap.org/

## color_cycle.py
`./color_cycle.py` or `python color_cycle.py`
cycles though various colors

`christmas` mode available for the holidays

## tests.py
`./tests.py` or `python tests.py`
many good examples