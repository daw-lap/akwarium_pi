#!/usr/bin/python

import MySQLdb
#import datetime
#import mysql.connector

def read_db(date):
	conn = MySQLdb.connect("localhost","user","user01","test1")
	cursor = conn.cursor()
	temp_sum = 0
	row_sum = 0
	
	query = "SELECT `temperature` FROM `temp2` WHERE `date` = '"+date+"';"
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
	
def insert_temp(p_temp,date):
	conn = MySQLdb.connect("localhost","user","user01","test1")
	cursor = conn.cursor()
	
	query = "INSERT INTO `temp_daily`(`date`, `temperature`) VALUES (STR_TO_DATE('21,5,2016','%d,%m,%Y'),"+str(p_temp)+");"
	
	try:
		cursor.execute(query)
		conn.commit()
	except MySQLdb.Error, e:
		print "An error has occurred. %s" %e
	finally:
		cursor.close()
		conn.close()
		
def delete_rows(date):
	conn = MySQLdb.connect("localhost","user","user01","test1")
	cursor = conn.cursor()
	
	query = "DELETE FROM `temp2` WHERE `date` = '"+date+"';"
	
	try:
		cursor.execute(query)
		conn.commit()
	except MySQLdb.Error, e:
		print "An error has occurred, during deleting from database. %s" %e
	finally:
		cursor.close()
		conn.close()

date = "2016-05-21"
print read_db(date)

insert_temp(read_db(date),date)

delete_rows(date)