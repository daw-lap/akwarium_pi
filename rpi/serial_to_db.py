#!/usr/bin/python

import serial
import time
import datetime
import MySQLdb

def insert_temp(p_temp):
	conn = MySQLdb.connect("localhost","user","user01","test1")
	cursor = conn.cursor()
	

	#query = "INSERT INTO `temp1`(`time`, `temperature`) VALUES (now(),"+p_temp+");"
	query = "INSERT INTO `temp2`(`date`, `time`, `temperature`) VALUES (curdate(),curtime(),"+p_temp+");"

	print query
	
	try:
		cursor.execute(query)
		conn.commit()
	except MySQLdb.Error, e:
		print "An error has occurred. %s" %e
	finally:
		cursor.close()
		conn.close()
	
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=3)

i = "1"
ser.flush()
ser.write(str(i))
ser.flush()
response = ser.readline()
print (response)
ser.close()

insert_temp(response)

