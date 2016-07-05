#!/usr/bin/python

import MySQLdb
#import datetime
#import mysql.connector

def today_medium():
	conn = MySQLdb.connect("localhost","user","user01","test1")
	cursor = conn.cursor()
	temp_sum = 0
	row_sum = 0
	
	query = "SELECT `temperature` FROM `temp2` WHERE `date` = curdate();"
	try:
		cursor.execute(query)
		conn.commit()
		
	except MySQLdb.Error, e:
		print "An error has occurred. %s" %e
	finally:
		cursor.close()
		conn.close()
	
	for temperature in cursor:
		temp_sum = temp_sum + temperature[0]
		row_sum = row_sum + 1
	return round(temp_sum/row_sum,2)
	
def insert_temp(p_temp):
	conn = MySQLdb.connect("localhost","user","user01","test1")
	cursor = conn.cursor()
	
	query = "INSERT INTO `temp_daily`(`date`, `temperature`) VALUES (curdate(),"+str(p_temp)+");"
	
	try:
		cursor.execute(query)
		conn.commit()
	except MySQLdb.Error, e:
		print "An error has occurred. %s" %e
	finally:
		cursor.close()
		conn.close()
		
def today_delete():
	conn = MySQLdb.connect("localhost","user","user01","test1")
	cursor = conn.cursor()
	
	query = "DELETE FROM `temp2` WHERE `date` = curdate();"
	
	try:
		cursor.execute(query)
		conn.commit()
	except MySQLdb.Error, e:
		print "An error has occurred, during deleting from database. %s" %e
	finally:
		cursor.close()
		conn.close()

#date = "2016-05-21"
#print read_db(date)

insert_temp(today_medium())

today_delete()