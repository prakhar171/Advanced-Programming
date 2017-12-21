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
'''
form = cgi.FieldStorage() 
cnn=mysql.connector.connect(user = "root", password = "", host = "localhost", database = "Shuttle")
cursor=cnn.cursor()
Name = form.getvalue('Name')
Ashoka_ID = form.getvalue('Ashoka_ID')

shuttle_time = form.getvalue('Time')
Origin = form.getvalue('Origin')

print Name, Ashoka_ID, time, Origin

id=form.getvalue('id')
print "<html>"
print "<head>"
print "<title>Shuttle Bookings</title>"
print "</head>"

addName="""INSERT INTO Bookings (Name,Ashoka_ID,Time,Origin) VALUES ('%s','%s','%s','%s',)""" % (name, Ashoka_ID, Shuttle_Time, Origin)
cursor.execute(addName)
cnn.commit()



weekno = datetime.datetime.today().weekday()
if weekno<4 and Origin=="Ashoka":
	check_availability = """SELECT COUNT FROM Weekday_Ashoka WHERE time = ?""",(Shuttle_Time)
	cursor.execute(check_availability)
	cnn.commit()
	book_shuttle = """INSERT INTO Weekday_Ashoka (Name,Ashoka_ID,Time,Origin) VALUES ('%s','%s','%s','%s',)""" % (name, Ashoka_ID, Shuttle_Time, Origin) 
elif weekno<4 and Origin == "Jahangirpuri": 
	book_shuttle = """INSERT INTO Weekday_Jahangirpuri (Name,Ashoka_ID,Time,Origin) VALUES ('%s','%s','%s','%s',)""" % (name, Ashoka_ID, Shuttle_Time, Origin)
elif weekno==5 and Origin == "Ashoka":
	book_shuttle = """INSERT INTO Friday_Ashoka (Name,Ashoka_ID,Time,Origin) VALUES ('%s','%s','%s','%s',)""" % (name, Ashoka_ID, Shuttle_Time, Origin)
elif weekno==5 and Origin == "Jahangirpuri":
	book_shuttle = """INSERT INTO Friday_Jahangirpuri (Name,Ashoka_ID,Time,Origin) VALUES ('%s','%s','%s','%s',)""" % (name, Ashoka_ID, Shuttle_Time, Origin)
elif weekno>5 and Origin=="Ashoka":
	book_shuttle = """INSERT INTO Weekend_Ashoka (Name,Ashoka_ID,Time,Origin) VALUES ('%s','%s','%s','%s',)""" % (name, Ashoka_ID, Shuttle_Time, Origin)
else:
    book_shuttle = """INSERT INTO Weekend_Jahangirpuri (Name,Ashoka_ID,Time,Origin) VALUES ('%s','%s','%s','%s',)""" % (name, Ashoka_ID, Shuttle_Time, Origin)




cnn.close()
'''

print "</body>"
print "</html>"
