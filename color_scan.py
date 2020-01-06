#!/usr/bin/python

# Little tool to figure out Native Instruments Komplete Kontrol mk2 
# simple color scheme on 0x81

import hid
import time

device=hid.device()
# 0x17cc: Native Instruments. 0x1620: KK S61 MK2
device.open(0x17cc, 0x1620)
device.write([0xa0])
device.set_nonblocking(False)

num_keys = 61

def set_color(c):
    device.write([0x81] + ([c] * num_keys))

color = 0
while True:
    for color in range(0x4, 0x1f):
        time.sleep(0.1)
        print("color: ", hex(color))
        set_color(color)    

#           Low, Medium, High, Saturated 
# RED:      0x04, 0x05, 0x06, 0x07
# ORANGE:   0x08, 0x09, 0x0a, 0x0b
# L ORANGE: 0x0c, 0x0d, 0x0e, 0x0f
# YELLOW:   0x10, 0x11, 0x12, 0x13
# YELLOW2:  0x14, 0x15, 0x16, x017
# L GREEN:  0x18, 0x19, 0x1a, 0x1b
# GREEN:    0x1c, 0x1d, 0x1e, 0x1f