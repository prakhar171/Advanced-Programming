#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import smtplib
import datetime
import mysql.connector
import random
from mysql.connector import errorcode
# Import modules for CGI handling 
import cgi, cgitb
#code = random.rantint(100000,999999)
# import datetime
# weekno = datetime.datetime.today().weekday()
# Create instance of FieldStorage 
# print "<a href=/programs/SignUp.html>Re-Register</a>"

form = cgi.FieldStorage() 
cnn=mysql.connector.connect(user = "root", password = "", host = "localhost", database = "Shuttle")
cursor=cnn.cursor()
ashoka_id = form.getvalue('Ashoka_ID')
id=form.getvalue('id')
code=random.randint(100000,999999)
code = str(code)
def mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("cmsashoka", "APProject@2017")
	msg = "Your Verification Code is " + code + "." + "\n\n" + "Please enter this into the field given to verify your email."
		
	server.sendmail("cmsashoka@gmail.com", ashoka_id, msg)
	server.quit()

print "<!DOCTYPE html>"
print "<head>"
print "<title>Shuttle Bookings</title>"
print "</head>"

if ashoka_id[-13:] == "ashoka.edu.in":
	multiple_bookings = "SELECT (Ashoka_ID) FROM Verification" 
	cursor.execute(multiple_bookings)
	multiple_bookings = cursor.fetchall()
	cnn.commit()
	x=""
	for i in multiple_bookings:
		for j in i:
			if j == ashoka_id:
				x = "multiple_bookings"
				break
		if x=="multiple_bookings":
			print "<html>" 
			print "<head>" 
			print "<meta http-equiv='refresh' content='0;url=/verify.html' /> "
			print "<title>You are going to be redirected</title>"
			print "</head> "
			print "<body> "
			print "<script>"
			print "window.alert('Sorry, you have reached your shuttle booking limit for today. :)');"
			print "</script>"
			print "</body> "
			print "</html>"
			break
	else:
		addName="""INSERT INTO Verification (Ashoka_ID,Random) VALUES ('%s','%s')""" % (ashoka_id,code,)
		cursor.execute(addName)
		cnn.commit()
		mail()
		print "<html>" 
		print "<head>" 
		print "<meta http-equiv='refresh' content='0;url=/shuttle.html' /> "
		print "<title>You are going to be redirected</title>"
		print "</head> "
		print "<body> "
		print "</body> "
		print "</html>"



else:
	print "<html>" 
	print "<head>" 
	print "<meta http-equiv='refresh' content='0;url=/verify.html' /> "
	print "<title>You are going to be redirected</title>"
	print "</head> "
	print "<body> "
	print "<script>"
	print "window.alert('Please use a valid Ashoka ID only');"
	print "</script>"
	print "</body> "
	print "</html>"

weekno = datetime.datetime.today().weekday()
weekno+=1

'''
def mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("cmsashoka", "APProject@2017")
	msg = "Dear " +name + "\n \n" + "Congratulations, your Shuttle has been booked. Please reach your boarding location 10 minutes before the departure time to avail your seat." + "\n \n" + "In Service," + "\n" + "Team Byte_Me"
		
	server.sendmail("cmsashoka@gmail.com", ashoka_id, msg)
	server.quit()


if weekno<4 and origin=="Ashoka":
	check_availability = "SELECT  `%s` from Weekday_Ashoka" % (shuttle_time,)
	cursor.execute(check_availability)
	check_availability = cursor.fetchall()
	cnn.commit()
	s_time=str(shuttle_time)
	available_seats=[]
	for i in check_availability:
		for j in i:
			if j!="":
				available_seats.append(j)

	if len(available_seats)<21:		
		book_seat="""INSERT INTO Weekday_Ashoka (`%s`) VALUES ('%s')""" % (shuttle_time,name)
		cursor.execute(book_seat)
		cnn.commit()
		mail()
		
	else:
		print "<script> window.alert('Your Shuttle has been booked');</script>"

elif weekno<4 and origin == "Jahangirpuri": 
	check_availability = "SELECT  `%s` from Weekday_Jahangirpuri" % (shuttle_time,)
	cursor.execute(check_availability)
	check_availability = cursor.fetchall()
	cnn.commit()

	s_time=str(shuttle_time)
	available_seats=[]
	for i in check_availability:
		for j in i:
			if j!="":
				available_seats.append(j)
	if len(available_seats)<21:
		
		book_seat="""INSERT INTO Weekday_Jahangirpuri (`%s`) VALUES ('%s')""" % (shuttle_time,name)
		cursor.execute(book_seat)
		cnn.commit()
		#mail()
	else:
		print '<script> window.alert(1+4);'+'</script>'
elif weekno==5 and origin == "Ashoka":
	check_availability = "SELECT  `%s` from Friday_Ashoka" % (shuttle_time,)
	cursor.execute(check_availability)
	check_availability = cursor.fetchall()
	cnn.commit()
	s_time=str(shuttle_time)
	available_seats=[]
	for i in check_availability:
		for j in i:
			if j!="":
				available_seats.append(j)
	if len(available_seats)<21:
		book_seat="""INSERT INTO Friday_Ashoka (`%s`) VALUES ('%s')""" % (shuttle_time,name)
		cursor.execute(book_seat)
		cnn.commit()
		mail()
	else:
		print "The Shuttle is Full"		
elif weekno==5 and origin == "Jahangirpuri":
	check_availability = "SELECT  `%s` from Friday_Jahangirpuri" % (shuttle_time,)
	cursor.execute(check_availability)
	check_availability = cursor.fetchall()
	cnn.commit()
	s_time=str(shuttle_time)
	available_seats=[]
	for i in check_availability:
		for j in i:
			if j!="":
				available_seats.append(j)
	if len(available_seats)<21:
		book_seat="""INSERT INTO Friday_Jahangirpuri (`%s`) VALUES ('%s')""" % (shuttle_time,name)
		cursor.execute(book_seat)
		cnn.commit()
		mail()
	else:
		print "The Shuttle is Full"
elif weekno>5 and origin=="Ashoka":
	check_availability = "SELECT  `%s` from Weekend_Ashoka" % (shuttle_time,)
	cursor.execute(check_availability)
	check_availability = cursor.fetchall()
	cnn.commit()
	s_time=str(shuttle_time)
	available_seats=[]
	for i in check_availability:
		for j in i:
			if j!="":
				available_seats.append(j)
	if len(available_seats)<21:
		book_seat="""INSERT INTO Weekend_Ashoka (`%s`) VALUES ('%s')""" % (shuttle_time,name)
		cursor.execute(book_seat)
		cnn.commit()
		mail()
	else:
		print "The Shuttle is Full"
else:
	check_availability = "SELECT  `%s` from Weekend_Jahangirpuri" % (shuttle_time,)
	cursor.execute(check_availability)
	check_availability = cursor.fetchall()
	cnn.commit()
	s_time=str(shuttle_time)
	available_seats=[]
	for i in check_availability:
		for j in i:
			if j!="":
				available_seats.append(j)
	if len(available_seats)<21:
		book_seat="""INSERT INTO Friday_Ashoka (`%s`) VALUES ('%s')""" % (shuttle_time,name)
		cursor.execute(book_seat)
		cnn.commit()
		mail()
	else:
		print "The Shuttle is Full"
print "<html>" 
print "<head>" 
print "<meta http-equiv='refresh' content='0;url=/booked.html' /> "
print "<title>You are going to be redirected</title>"
print "</head> "
print "<body> "
print "</body> "
print "</html>"
'''
cnn.close()

print "</html>"