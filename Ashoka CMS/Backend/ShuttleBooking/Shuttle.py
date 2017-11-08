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
	print check_availability
	s_time=str(shuttle_time)
'''
	if len(check_availability)!=20:

		book_seat="""INSERT INTO Weekday_Ashoka (%s_time) VALUES ('%s',)""" % (shuttle_time,name,)
		cursor.execute(book_seat)
		cnn.commit()

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


'''

cnn.close()


print "</body>"
print "</html>"
