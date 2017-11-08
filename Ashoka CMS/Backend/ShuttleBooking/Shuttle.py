#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"
import datetime
import mysql.connector
from mysql.connector import errorcode
# Import modules for CGI handling 
import cgi, cgitb
# import datetime
# weekno = datetime.datetime.today().weekday()
# Create instance of FieldStorage 
# print "<a href=/programs/SignUp.html>Re-Register</a>"
form = cgi.FieldStorage() 
cnn=mysql.connector.connect(user = "root", password = "", host = "localhost", database = "Rooms")
cursor=cnn.cursor()
name = form.getvalue('Name')
ashoka_id = form.getvalue('Ashoka_ID')
shuttle_time = form.getvalue('Shuttle_Time')
origin = form.getvalue('Origin')
print name, ashoka_id, shuttle_time, origin
id=form.getvalue('id')
print "<html>"
print "<head>"
print "<title>Shuttle Bookings</title>"
print "</head>"
addName="""INSERT INTO Bookings (Name,Ashoka_ID,Shuttle_Time,Origin) VALUES ('%s','%s','%s','%s')""" % (name,ashoka_id,shuttle_time,origin)
cursor.execute(addName)
cnn.commit()
weekno = datetime.datetime.today().weekday()
weekno+=1
if weekno<4 and origin=="Ashoka":
	check_availability = "SELECT  `%s` from Weekday_Ashoka" % (shuttle_time,)
	cursor.execute(check_availability)
	check_availability = cursor.fetchall()
	cnn.commit()
	s_time=str(shuttle_time)
	if len(check_availability)!=20:	
		print len(check_availability)	
		book_seat="""INSERT INTO Weekday_Ashoka (`%s`) VALUES ('%s')""" % (shuttle_time,name)
		cursor.execute(book_seat)
		cnn.commit()
elif weekno<4 and Origin == "Jahangirpuri": 
	check_availability = "SELECT  `%s` from Weekday_Jahangirpuri" % (shuttle_time,)
	cursor.execute(check_availability)
	check_availability = cursor.fetchall()
	cnn.commit()
	s_time=str(shuttle_time)
	if len(check_availability)!=20:
		book_seat="""INSERT INTO Weekday_Jahangirpuri (`%s`) VALUES ('%s')""" % (shuttle_time,name)
		cursor.execute(book_seat)
		cnn.commit()
elif weekno==5 and Origin == "Ashoka":
	check_availability = "SELECT  `%s` from Friday_Ashoka" % (shuttle_time,)
	cursor.execute(check_availability)
	check_availability = cursor.fetchall()
	cnn.commit()
	s_time=str(shuttle_time)
	if len(check_availability)!=20:
		book_seat="""INSERT INTO Friday_Ashoka (`%s`) VALUES ('%s')""" % (shuttle_time,name)
		cursor.execute(book_seat)
		cnn.commit()
elif weekno==5 and Origin == "Jahangirpuri":
	check_availability = "SELECT  `%s` from Friday_Jahangirpuri" % (shuttle_time,)
	cursor.execute(check_availability)
	check_availability = cursor.fetchall()
	cnn.commit()
	s_time=str(shuttle_time)
	if len(check_availability)!=20:
		book_seat="""INSERT INTO Friday_Jahangirpuri (`%s`) VALUES ('%s')""" % (shuttle_time,name)
		cursor.execute(book_seat)
		cnn.commit()
elif weekno>5 and Origin=="Ashoka":
	check_availability = "SELECT  `%s` from Weekend_Ashoka" % (shuttle_time,)
	cursor.execute(check_availability)
	check_availability = cursor.fetchall()
	cnn.commit()
	s_time=str(shuttle_time)
	if len(check_availability)!=20:
		book_seat="""INSERT INTO Weekend_Ashoka (`%s`) VALUES ('%s')""" % (shuttle_time,name)
		cursor.execute(book_seat)
		cnn.commit()
else:
	check_availability = "SELECT  `%s` from Weekend_Jahangirpuri" % (shuttle_time,)
	cursor.execute(check_availability)
	check_availability = cursor.fetchall()
	cnn.commit()
	s_time=str(shuttle_time)
	if len(check_availability)!=20:
		book_seat="""INSERT INTO Friday_Ashoka (`%s`) VALUES ('%s')""" % (shuttle_time,name)
		cursor.execute(book_seat)
		cnn.commit()
cnn.close()
print "</body>"
print "</html>"
