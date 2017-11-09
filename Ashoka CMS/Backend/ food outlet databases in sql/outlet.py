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
if outlet=="THC":
	get_category = "SELECT category FROM THC Where price < %s" % (price,)	
	cursor.execute(get_category)
	get_category=cursor.fetchall()
	get_fooditem = "SELECT fooditem FROM THC Where price < %s" % (price,)
	cursor.execute(get_fooditem)
	get_fooditem=cursor.fetchall()
	get_price = "SELECT price FROM THC Where price < %s" % (price,)
	cursor.execute(get_price)
	get_price=cursor.fetchall()
	cnn.commit()
	
	
elif outlet =="foodjunc":
	get_category = "SELECT category FROM THC Where price < %s" % (price,)	
	cursor.execute(get_category)
	get_category=cursor.fetchall()
	get_fooditem = "SELECT fooditem FROM THC Where price < %s" % (price,)
	cursor.execute(get_fooditem)
	get_fooditem=cursor.fetchall()
	get_price = "SELECT price FROM THC Where price < %s" % (price,)
	cursor.execute(get_price)
	get_price=cursor.fetchall()
	cnn.commit()

elif outlet == "chicago":
	get_category = "SELECT category FROM THC Where price < %s" % (price,)	
	cursor.execute(get_category)
	get_category=cursor.fetchall()
	get_fooditem = "SELECT fooditem FROM THC Where price < %s" % (price,)
	cursor.execute(get_fooditem)
	get_fooditem=cursor.fetchall()
	get_price = "SELECT price FROM THC Where price < %s" % (price,)
	cursor.execute(get_price)
	get_price=cursor.fetchall()
	cnn.commit()

elif outlet == "chitchat":
	get_category = "SELECT Category FROM THC Where price < %s" % (price,)	
	cursor.execute(get_category)
	get_category=cursor.fetchall()
	get_fooditem = "SELECT Fooditem FROM THC Where price < %s" % (price,)
	cursor.execute(get_fooditem)
	get_fooditem=cursor.fetchall()
	get_price = "SELECT price FROM THC Where price < %s" % (price,)
	cursor.execute(get_price)
	get_price=cursor.fetchall()
	cnn.commit()

elif outlet == "juicebar":	
	get_category = "SELECT category FROM THC Where price < %s" % (price,)	
	cursor.execute(get_category)
	get_category=cursor.fetchall()
	get_fooditem = "SELECT fooditem FROM THC Where price < %s" % (price,)
	cursor.execute(get_fooditem)
	get_fooditem=cursor.fetchall()
	get_price = "SELECT price FROM THC Where price < %s" % (price,)
	cursor.execute(get_price)
	get_price=cursor.fetchall()
	cnn.commit()
food_category=[]
food_fooditem=[]
food_price=[]
for i in range (len(get_category)):
	food_category.append(get_category[i])
	food_fooditem.append(get_fooditem[i])
	food_price.append(get_price[i])
print "category"
print "fooditem"
print "price"
print '<br>'
for j in range(len(food_category)):
	print food_category[j][0]
	print food_fooditem[j][0]
	print food_price[j][0]
	print '<br>'
cnn.close()


print "</body>"
print "</html>"