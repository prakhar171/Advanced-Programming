#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"
import smtplib
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
cnn=mysql.connector.connect(user = "root", password = "", host = "localhost", database = "Shuttle")
cursor=cnn.cursor()
name = form.getvalue('Name')
ashoka_id = form.getvalue('Ashoka_ID')
shuttle_time = form.getvalue('Shuttle_Time')
origin = form.getvalue('Origin')
Password = form.getvalue('OTP')
id=form.getvalue('id')
print "<html>"
print "<head>"
print "<title>Shuttle Bookings</title>"
print "</head>"

weekno = datetime.datetime.today().weekday()
weekno+=1

def mail():
	msg = "Dear " + name + "\n \n" + "Congratulations, your Shuttle has been booked. Please reach your boarding location 10 minutes before the departure time to avail your seat." + "\n \n" + "In Service," + "\n" + "Team Byte_Me"
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("cmsashoka", "APProject@2017")
	server.sendmail("cmsashoka@gmail.com", ashoka_id, msg)
	server.quit()
def redirect():
	print "<html>" 
	print "<head>" 
	print "<meta http-equiv='refresh' content='0;url=/booked.html' /> "
	print "<title>You are going to be redirected</title>"
	print "</head> "
	print "<body> "
	print "</body> "
	print "</html>"

Verify = "SELECT (Random) FROM Verification"
cursor.execute(Verify)
Verify = cursor.fetchall()
cnn.commit()
y=True
r=0
for i in Verify:
	for j in i:
		if j==Password:

			multi_booking = "SELECT (OTP) FROM Bookings"
			cursor.execute(multi_booking)
			multi_booking= cursor.fetchall()
			cnn.commit()
			x=True
			for k in multi_booking:
				for l in k:
					if l==Password:
						print "<script> window.alert('This Verification Code has already been used.');</script>"
						print "<html>" 
						print "<head>" 
						print "<meta http-equiv='refresh' content='0;url=/shuttle.html' /> "
						print "<title>You are going to be redirected</title>"
						print "</head> "
						print "<body> "
						print "</body> "
						print "</html>"
						x=False
						break
				if x==False:
					break
			else:
				addName="""INSERT INTO Bookings (Name,Ashoka_ID,Shuttle_Time,Origin,OTP) VALUES ('%s','%s','%s','%s', '%s')""" % (name,ashoka_id,shuttle_time,origin,Password)
				cursor.execute(addName)
				cnn.commit()


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
						redirect()
					else:
						print "<script> window.alert('Your Shuttle is full. Please try another shuttle.');</script>"
						print "<html>" 
						print "<head>" 
						print "<meta http-equiv='refresh' content='0;url=/shuttle.html' /> "
						print "<title>You are going to be redirected</title>"
						print "</head> "
						print "<body> "
						print "</body> "
						print "</html>"


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
						mail()
						redirect()
					else:
						print "<script> window.alert('Your Shuttle is full. Please try another shuttle.');</script>"
						print "<html>" 
						print "<head>" 
						print "<meta http-equiv='refresh' content='0;url=/shuttle.html' /> "
						print "<title>You are going to be redirected</title>"
						print "</head> "
						print "<body> "
						print "</body> "
						print "</html>"
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
						redirect()
					else:
						print "<script> window.alert('Your Shuttle is full. Please try another shuttle.');</script>"
						print "<html>" 
						print "<head>" 
						print "<meta http-equiv='refresh' content='0;url=/shuttle.html' /> "
						print "<title>You are going to be redirected</title>"
						print "</head> "
						print "<body> "
						print "</body> "
						print "</html>"
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
						redirect()
					else:
						print "<script> window.alert('Your Shuttle is full. Please try another shuttle.');</script>"
						print "<html>" 
						print "<head>" 
						print "<meta http-equiv='refresh' content='0;url=/shuttle.html' /> "
						print "<title>You are going to be redirected</title>"
						print "</head> "
						print "<body> "
						print "</body> "
						print "</html>"
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
						redirect()
					else:
						print "<script> window.alert('Your Shuttle is full. Please try another shuttle.');</script>"
						print "<html>" 
						print "<head>" 
						print "<meta http-equiv='refresh' content='0;url=/shuttle.html' /> "
						print "<title>You are going to be redirected</title>"
						print "</head> "
						print "<body> "
						print "</body> "
						print "</html>"
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
						redirect()
					else:
						print "<script> window.alert('Your Shuttle is full. Please try another shuttle.');</script>"
						print "<html>" 
						print "<head>" 
						print "<meta http-equiv='refresh' content='0;url=/shuttle.html' /> "
						print "<title>You are going to be redirected</title>"
						print "</head> "
						print "<body> "
						print "</body> "
						print "</html>"
			y=False
			break
	if y==False:
		break	
else:
	print "<script> window.alert('Please enter a valid verification code.');</script>"
	print "<html>" 
	print "<head>" 
	print "<meta http-equiv='refresh' content='0;url=/shuttle.html' /> "
	print "<title>You are going to be redirected</title>"
	print "</head> "
	print "<body> "
	print "</body> "
	print "</html>"
cnn.close()
print "</body>"
print "</html>"