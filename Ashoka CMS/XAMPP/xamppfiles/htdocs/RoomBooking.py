#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"
import mysql.connector
from mysql.connector import errorcode
# Import modules for CGI handling 
import cgi, cgitb

# Create instance of FieldStorage 
# print "<a href=/programs/SignUp.html>Re-Register</a>"
form = cgi.FieldStorage() 
cnn=mysql.connector.connect(user = "root", password = "", host = "localhost", database = "Rooms")
cursor=cnn.cursor()
name = form.getvalue('Name')
ashoka_id = form.getvalue('Ashoka_ID')
purpose  = form.getvalue('Purpose')
capacity = form.getvalue('Capacity')
day  = form.getvalue('Day')
start_time = form.getvalue('Start_Time')
end_time = form.getvalue('End_Time')
print name, ashoka_id, purpose, capacity, day, start_time, end_time
id=form.getvalue('id')
print "<html>"
print "<head>"
print "<title>Room Bookings</title>"
print "</head>"
addName="""INSERT INTO rooms (Name,Ashoka_ID,Purpose,Capacity,Day,Start_Time,End_Time) VALUES ('%s','%s','%s','%s','%s','%s','%s')""" % (name, ashoka_id, purpose, capacity, day, start_time, end_time)
total_time=[]
start_time_var = start_time.replace(':','')
start_time_var = int(start_time_var)
end_time_var = end_time.replace(':', '')
end_time_var = int(end_time_var)
if end_time_var%100!=0:
	end_time_var+20

if start_time_var%100!=0:
	start_time_var+20

slots = (end_time_var-start_time_var)/50
cursor.execute(addName)
#available_capacity = "SELECT Capacity from Class_Rooms"
# TO PRINT OUT ALL CAPACITIES FROM CLASS ROOMS
# for i in available_capacity:
# 	for j in i:
# 		if j =='':
# 			continue
# 		else:
# 			j=int(j)
# 	print j
if capacity == '25':
	room_number = "SELECT Room_number from Class_Rooms where Capacity = '25'"
elif capacity == '50':
	room_number = "SELECT Room_number from Class_Rooms where Capacity = '50'"
elif capacity =='100':
	room_number = "SELECT Room_number from Class_Rooms where Capacity = '100'"
else:
	room_number = "SELECT Room_number from Class_Rooms where Capacity = '200'"
cursor.execute(room_number)
room_number = cursor.fetchall()
cnn.commit()
print room_number
room_numbers=[]
for i in room_number:
	
	for j in i:
		
		room_numbers.append(j)

if day == "monday" or day == "Monday":
	book = """ UPDATE Monday set TR101='abhay'"""   #, (rooms_number[0], name, start_time)
	#time = "SELECT Time FROM Monday WHERE Time = '1:00'"
	cursor.execute(book)
	book = cursor.fetchall()
	cnn.commit()

''' 
		book_room = """INSERT INTO Monday ('%s') VALUES ('%s')""" % (i,name)
		cursor.execute(book_room)
		book_room=cursor.fetchall()
		cnn.commit()


			available_capacity = 'SELECT Capacity from Monday'
			start_time = 'SELECT Time'
			if available_capacity == capacity:
				if start_time == 
elif Day = "Tuesday":
	available_capacity = 'SELECT Capacity from Tuesday'
elif Day = "Wednesday":
	available_capacity = 'SELECT Capacity from Wednesday'
elif Day = "Thursday":
	available_capacity = 'SELECT Capacity from Thursday'
elif Day = "Friday":
	available_capacity = 'SELECT Capacity from Friday'
elif Day = "Saturday":
	available_capacity = 'SELECT Capacity from Saturday'
elif Day = "Sunday":
	available_capacity = 'SELECT Capacity from Sunday'
cursor.execute(room_capacity)
''' 


cnn.close()

print "</body>"
print "</html>"