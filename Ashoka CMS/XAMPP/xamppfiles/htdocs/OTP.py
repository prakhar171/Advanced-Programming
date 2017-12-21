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
cnn=mysql.connector.connect(user = "root", password = "", host = "localhost", database = "Shuttle")
cursor=cnn.cursor()
ID = form.getvalue('Email_ID')
Password = form.getvalue('OTP')

id=form.getvalue('id')
def mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("cmsashoka", "APProject@2017")
	msg = "Your Verification Code is " + code + "." + "\n\n" + "Please enter this into the field given to verify your email."
	server.sendmail("cmsashoka@gmail.com", ashoka_id, msg)
	server.quit()

Verified = "SELECT (Random) FROM Verification"
cursor.execute(Verified)
Verified = cursor.fetchall()
cnn.commit()

for i in Verified:
	for j in i:
		if j==Password:
			print "<html>" 
			print "<head>" 
			print "<meta http-equiv='refresh' content='0;url=/shuttle.html' /> "
			print "<title>You are going to be redirected</title>"
			print "</head> "
			print "<body> "
			print "</body> "
			print "</html>"
#else:


print "<!DOCTYPE html>"
print "<head>"
print "<title>Shuttle Bookings</title>"
print "</head>"