#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"
import mysql.connector
from mysql.connector import errorcode
# Import modules for CGI handling 
import cgi, cgitb
'''
# Create instance of FieldStorage 
# print "<a href=/programs/SignUp.html>Re-Register</a>"
form = cgi.FieldStorage() 
cnn=mysql.connector.connect(user = "root", password = "", host = "localhost", database = "Rooms")
cursor=cnn.cursor()
name = form.getvalue('name')
ashoka_id = form.getvalue('ashoka_id')
e_number  = form.getvalue('e_number')
purpose  = form.getvalue('purpose')
mobile = form.getvalue('mobile')
capacity = = form.getvalue('capacity')
id=form.getvalue('id')

print "Content-type:text/html\r\n\r\n"
'''
print "<html>"
print "<head>"
print "<title>Room Bookings</title>"
print "</head>"
'''
registers = 'SELECT e_number FROM rooms'

cursor.execute(registers)
# Fetch all the rows in a list of lists.
result_register = cursor.fetchall()
print result_register
for i in result_register:
	
	if int(i[0])==int(e_number):
		print "User Exists"
		print "\n"
		print "<a href=/programs/SignUp.html>Re-Register</a>"    
		break
else:
	

	print "Welcome"
	addName="""INSERT INTO rooms (name,ashoka_id,e_number,mobile) VALUES ('%s','%s','%s','%s')""" % (name, ashoka_id , e_number , mobile)
#addName="""INSERT INTO seats (name,ashoka_id,e_number,mobile) VALUES (abc,def,hgi,zxc)"""
	cursor.execute(addName)
	cnn.commit()
	cnn.close()
#print "<a href='/cgi-bin/getdata.py'> Check Availability </a>"
print "<body>"
#print "<h2> Hello %s %s %s %s %s %s %s %s </h2>" % (first_name,last_name,middle_name,mobile,day,month,year,qualification)
'''
print "</body>"
print "</html>"