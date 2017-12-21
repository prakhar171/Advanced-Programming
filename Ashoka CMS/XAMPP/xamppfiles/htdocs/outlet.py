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
cnn=mysql.connector.connect(user = "root", password = "", host = "localhost", database = "Food_Outlet")
cursor=cnn.cursor()
outlet = form.getvalue('Outlet')
price = form.getvalue('Budget')
id=form.getvalue('id')
category=form.getvalue('Category')
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
	get_cal="SELECT calories from thc where price < %s" %(price,)
	cursor.execute(get_cal)
	get_cal=cursor.fetchall()
	cnn.commit()
	

elif outlet =="foodjunc":
	get_category = "SELECT category FROM foodjunc Where price < %s" % (price,)	
	cursor.execute(get_category)
	get_category=cursor.fetchall()
	get_fooditem = "SELECT fooditem FROM foodjunc Where price < %s" % (price,)
	cursor.execute(get_fooditem)
	get_fooditem=cursor.fetchall()
	get_price = "SELECT price FROM foodjunc Where price < %s" % (price,)
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
	get_cal="SELECT calories from chicago where price < %s" %(price,)
	cursor.execute(get_cal)
	get_cal=cursor.fetchall()
	cnn.commit()

elif outlet == "chitchat":
	get_category = "SELECT Category FROM chitchat Where price < %s" % (price,)	
	cursor.execute(get_category)
	get_category=cursor.fetchall()
	get_fooditem = "SELECT Fooditem FROM chitchat Where price < %s" % (price,)
	cursor.execute(get_fooditem)
	get_fooditem=cursor.fetchall()
	get_price = "SELECT price FROM chitchat Where price < %s" % (price,)
	cursor.execute(get_price)
	get_price=cursor.fetchall()
	get_cal="SELECT calories from chitchat where price < %s" %(price,)
	cursor.execute(get_cal)
	get_cal=cursor.fetchall()
	cnn.commit()

elif outlet == "juicebar":	
	get_category = "SELECT category FROM juicebar Where price < %s" % (price,)	
	cursor.execute(get_category)
	get_category=cursor.fetchall()
	get_fooditem = "SELECT fooditem FROM juicebar Where price < %s" % (price,)
	cursor.execute(get_fooditem)
	get_fooditem=cursor.fetchall()
	get_price = "SELECT price FROM juicebar Where price < %s" % (price,)
	cursor.execute(get_price)
	get_price=cursor.fetchall()
	get_cal="SELECT calories from juicebar where price < %s" %(price,)
	cursor.execute(get_cal)
	get_cal=cursor.fetchall()
	cnn.commit()

elif category == "pizza":
	print category
	get_category = "SELECT category FROM total Where category = '%s' " % (category,)	
	cursor.execute(get_category)
	get_category=cursor.fetchall()
	
	
	get_fooditem = "SELECT fooditem FROM total Where category = '%s' " % (category,)
	cursor.execute(get_fooditem)
	get_fooditem=cursor.fetchall()
	
	get_price = "SELECT price FROM total Where category = '%s' " % (category,)
	cursor.execute(get_price)
	get_price=cursor.fetchall()
	
	get_cal = "SELECT calories FROM total Where category = '%s' " % (category,)
	cursor.execute(get_cal)
	get_cal=cursor.fetchall()
	
	cnn.commit()

elif category == "ice creme":
	get_category = "SELECT category FROM total Where category = '%s'" % (category,)	
	cursor.execute(get_category)
	get_category=cursor.fetchall()
	get_fooditem = "SELECT fooditem FROM total Where category = '%s'" % (category,)
	cursor.execute(get_fooditem)
	get_fooditem=cursor.fetchall()
	get_price = "SELECT price FROM total Where category = '%s'" % (category,)
	cursor.execute(get_price)
	get_price=cursor.fetchall()
	
	get_cal = "SELECT calories FROM total where category = '%s'" %(category,)
	cursor.execute(get_cal)
	get_cal=cursor.fetchall()
	cnn.commit()

elif category == "Beverages":
	get_category = "SELECT category FROM total Where category = '%s'" % (category,)	
	cursor.execute(get_category)
	get_category=cursor.fetchall()
	
	get_fooditem = "SELECT fooditem FROM total Where category = '%s'" % (category,)
	cursor.execute(get_fooditem)
	get_fooditem=cursor.fetchall()
	
	get_price = "SELECT price FROM total Where category = '%s'" % (category,)
	cursor.execute(get_price)
	get_price=cursor.fetchall()
	
	
	get_cal = "SELECT calories FROM total where category = '%s'" %(category,)
	cursor.execute(get_cal)
	get_cal=cursor.fetchall()
	cnn.commit()	

elif category == "Maggi":
	get_category = "SELECT category FROM total Where category = '%s'" % (category,)	
	cursor.execute(get_category)
	get_category=cursor.fetchall()
	get_fooditem = "SELECT fooditem FROM total Where category = '%s'" % (category,)
	cursor.execute(get_fooditem)
	get_fooditem=cursor.fetchall()
	get_price = "SELECT price FROM total Where category = '%s'" % (category,)
	cursor.execute(get_price)
	get_price=cursor.fetchall()
	
	get_cal = "SELECT calories FROM total where category = '%s'" % (category,)
	cursor.execute(get_cal)
	get_cal=cursor.fetchall()
	cnn.commit()

elif category == "Rolls":
	get_category = "SELECT category FROM total Where category = '%s'" % (category,)	
	cursor.execute(get_category)
	get_category=cursor.fetchall()
	get_fooditem = "SELECT fooditem FROM total Where category = '%s'" % (category,)
	cursor.execute(get_fooditem)
	get_fooditem=cursor.fetchall()
	get_price = "SELECT price FROM total Where category = '%s'" % (category,)
	cursor.execute(get_price)
	get_price=cursor.fetchall()
	get_cal = "SELECT calories FROM total where category = '%s'" %(category,)
	cursor.execute(get_cal)
	get_cal=cursor.fetchall()
	cnn.commit()

else:
	print("not found")

food_category=[]
food_fooditem=[]
food_price=[]
calories=[]
for i in range (len(get_category)):
	food_category.append(get_category[i])
	food_fooditem.append(get_fooditem[i])
	food_price.append(get_price[i])
	calories.append(get_cal[i])
print "<!doctype html>"


print "<html lang='en'>"
print "<head>"
print    "<meta charset='utf-8'>"
print    "<meta name='description' content='The Wild Ones(Hostel 2), IIT Bombay'>"
print    "<meta name='author' content='Viswa Virinchi'>"
print    "<meta name='viewport' content='width=device-width, initial-scale=1'>"
print    "<link rel='icon' type='image/png' href='/images/logo.jpg'>"
print    "<title>Mess | Hostel 2 | IIT Bombay</title>"

print    "<!-- Page styles -->"
print    "<link href='https://fonts.googleapis.com/css?family=Roboto:regular,bold,italic,thin,light,bolditalic,black,medium&amp;lang=en' rel='stylesheet'>"
print    "<link href='https://fonts.googleapis.com/icon?family=Material+Icons' rel='stylesheet'>"
print    "<link rel='stylesheet' href='https://storage.googleapis.com/code.getmdl.io/1.0.0/material.min.css' media='screen,projection'>"
print    "<link rel='stylesheet' href='../styles.css' media='screen,projection'>"
print    "<!--<link rel='stylesheet' href='../css/materialize.css' media='screen,projection'>-->"

print    "<!-- Basic stylesheet -->"
print    "<link rel='stylesheet' href='../owl-carousel/owl.carousel.css'>"

print    "<!-- Default Theme -->"
print    "<link rel='stylesheet' href='../owl-carousel/owl.theme.css'>"

print    "<!-- Bootstrap -->"
print    "<link href='../css/bootstrap.min.css' rel='stylesheet'>"
print    "<link href='../css/pgwslideshow.css' rel='stylesheet'>"
print    "<link href='../css/pgwslideshow_light.css' rel='stylesheet'>"
print    "<link href='../css/bootstrap-theme.min.css' rel='stylesheet'>"
print "</head>"
print "<body>"

#print "category",
#print "fooditem",
#print "price",
#print "calories"
#print '<br>'

print "<p align='center'>"
print "<table class='mdl-cell mdl-cell--6-col mdl-cell--5-col-tablet mdl-cell--5-col-phone mdl-data-table mdl-js-data-table mdl-shadow--2dp'>"
print                "<thead align=center'>"
print                "<tr>"
print                    "<th class='mdl-data-table__cell--non-numeric'>FOOD ITEM</th>"
print					"<th>CATEGORY</th>"
print					"<th>PRICE</th>"
print                    "<th>CALORIES</th>"

print                "</tr>"
print                "</thead>"




for j in range(len(food_category)):
	print "<p align='center'>"
	print "<table class='mdl-cell mdl-cell--6-col mdl-cell--5-col-tablet mdl-cell--5-col-phone mdl-data-table mdl-js-data-table mdl-shadow--2dp'>"
	print                "<thead align=center'>"
	print                "<tr>"
	print                    "<th class='mdl-data-table__cell--non-numeric'>CATEGORY</th>"
	print					"<th>FOOD</th>"
	print					"<th>PRICE</th>"
	print                    "<th>CALORIES</th>"

	print                "</tr>"
	print                "</thead>"

	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	
	print food_category[j][0],
	print "&emsp;"
	print "&emsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	

	print food_fooditem[j][0]
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"



	print food_price[j][0]
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"

	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"

	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"
	print "&nbsp;"

	print "&nbsp;"
	
	print calories[j][0]
	print "&nbsp;"
	print "&nbsp;"
	print "</p>"
	print '<br>'

cnn.close()

print "</body>"
print "</html>"
