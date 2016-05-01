#!/usr/bin/python

import serial
	
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

i = "1"

#ser.open()
ser.flush()
ser.write("testing")

try:
	while 1:
		ser.write(raw_input("write:"))
		response = ser.readline()

		print response
except KeyboardInterrupt:
	print("serial port closed")
	ser.close()
