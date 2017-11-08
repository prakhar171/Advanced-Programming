#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"
import smtplib
import datetime
import mysql.connector
import random
from mysql.connector import errorcode
# Import modules for CGI handling 
import cgi, cgitb
# import datetime
# weekno = datetime.datetime.today().weekday()
# Create instance of FieldStorage 
# print "<a href=/programs/SignUp.html>Re-Register</a>"
form = cgi.FieldStorage() 
cnn=mysql.connector.connect(user = "root", password = "", host = "localhost", database = "Food_Outlets")
cursor=cnn.cursor()
outlet = form.getvalue('Outlet')
price = form.getvalue('Budget')
id=form.getvalue('id')
print "<!DOCTYPE html>"
print "<head>"
print "<title>Shuttle Bookings</title>"
print "</head>"
print "<body>"
print price, outlet
if outlet=="THC":
	get_menu = "SELECT category FROM THC Where price < %s" % (price,)

	get_menu = "SELECT category FROM THC"
	get_menu = "SELECT category FROM THC"
	cursor.execute(get_menu)
	get_menu=cursor.fetchall()
	cnn.commit()
	
elif outlet =="foodjunc":
	get_menu = "SELECT category FROM foodjunc"
	cursor.execute(get_menu)
	get_menu=cursor.fetchall()
	cnn.commit()

elif outlet == "chicago":
	get_menu = "SELECT category FROM chicago"
	cursor.execute(get_menu)
	get_menu=cursor.fetchall()
	cnn.commit()

elif outlet == "chitchat":
	get_menu = "SELECT category FROM chitchat"
	cursor.execute(get_menu)
	get_menu=cursor.fetchall()
	cnn.commit()

elif outlet == "juicebar":	
	get_menu = "SELECT category FROM juicebar"
	cursor.execute(get_menu)
	get_menu=cursor.fetchall()
	cnn.commit()

cnn.close()


print "</body>"
print "</html>"