#!/usr/bin/python

import serial
import time
import datetime
import MySQLdb

def insert_temp(temperature):
	conn = MySQLdb.connect("localhost","user","user01","test1")
	cursor = conn.cursor()
	
	try:
		cursor.execute("INSERT INTO `temp1`(`time`, `temperature`) VALUES (now(),"+temperature+")")
		conn.commit()
	except MySQLdb.Error, e:
		print "An error has occurred. %s" %e
	finally:
		cursor.close()
		conn.close()
	
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

i = "1"


ser.flush()
ser.write(str(i))
response = ser.readline()
print (response)

insert_temp(response)
ser.close()

