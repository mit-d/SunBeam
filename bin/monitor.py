#!/usr/bin/env python3

import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the bus
spi = busio.SPI(clock = board.SCK, MISO = board.MISO, MOSI = board.MOSI);

# create the chip select
cs = digitalio.DigitalInOut(board.D5)

# create MCP object
mcp = MCP.MCP3008(spi, cs)

# create analog input channels
chan = [AnalogIn(mcp, MCP.P0), 
        AnalogIn(mcp, MCP.P1), 
        AnalogIn(mcp, MCP.P2), 
        AnalogIn(mcp, MCP.P3), 
        AnalogIn(mcp, MCP.P4), 
        AnalogIn(mcp, MCP.P5), 
        AnalogIn(mcp, MCP.P6), 
        AnalogIn(mcp, MCP.P7)]

# we will store our values (since powered on) here
# note: add permanent storage later at a less frequent interval
f = open("/tmp/MCP3008_v.csv", "w+")

while 1:
    f.write(time.time() + ',');
    f.write(str(chan[0].voltage) + ',')
    f.write(str(chan[1].voltage) + ',')
    f.write(str(chan[2].voltage) + ',')
    f.write(str(chan[3].voltage) + ',')
    f.write(str(chan[4].voltage) + ',')
    f.write(str(chan[5].voltage) + ',')
    f.write(str(chan[6].voltage) + ',')
    f.write(str(chan[7].voltage) + '\n')
    time.sleep(10)
