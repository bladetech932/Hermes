#!/usr/bin/env python

import serial
import time
import json

ser = serial.Serial("/dev/ttyS0", baudrate=115200, timeout=3.0)
var = 0.1

#output = "Test String\n"
try:
	while True:
		x = ser.readline()
		print(x)
		ser.write(x)

except KeyboardInterrupt:
	print("closed")
