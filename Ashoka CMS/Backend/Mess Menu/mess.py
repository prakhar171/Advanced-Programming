#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"
import mysql.connector
from mysql.connector import errorcode
# Import modules for CGI handling #The module is being used to fetch data from HTML form
import cgi, cgitb
import xlrd



# Create instance of FieldStorage 
# print "<a href=/programs/SignUp.html>Re-Register</a>"
form = cgi.FieldStorage() 
cnn=mysql.connector.connect(user = "root", password = "", host = "localhost", database = "Rooms")
cursor=cnn.cursor()
day  = form.getvalue('Day')
meal = form.getvalue('Meal')
# To create a simple webpage to display our result
print "<html>"
print "<head>"
print "<title>Mess Menu</title>"

print "</head>"
# Comparing data received from the user in the variable 'day' and 'meal' and comparing the variables to find if they correspoding to anything to our Mess Menu in the cloud
if day=="Monday" and meal=="Breakfast":
    print "<iframe width='204' height='230' frameborder='0' scrolling='no' src='https://goo.gl/K5kWFz'></iframe>"

elif (day=="Monday" and meal=="Lunch"):
     print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://goo.gl/nkZQ1g'></iframe>"                       

    
elif (day=="Monday" and meal=="Snacks"):
        print "<iframe width='204' height='105' frameborder='0' scrolling='no' src='https://goo.gl/2b6c8R'></iframe>"
elif (day=="Monday" and meal=="Dinner"):
        print "<iframe width='204' height='251' frameborder='0' scrolling='no' src='https://goo.gl/78ceXj'></iframe>"
elif (day=="Tuesday" and meal=="Breakfast"):
        print "<iframe width='200' height='230' frameborder='0' scrolling='no' src='https://goo.gl/kJzu9Z'></iframe>"
elif (day=="Tuesday" and meal=="Lunch"):
       print "<iframe width='200' height='303' frameborder='0' scrolling='no' src='https://goo.gl/TkUtGf'></iframe>"
elif (day=="Tuesday" and meal=="Snacks"):
       print "<iframe width='200' height='105' frameborder='0' scrolling='no' src='https://goo.gl/7G6epi'></iframe>"
elif (day=="Tuesday" and meal=="Dinner"):
       print "<iframe width='200' height='251' frameborder='0' scrolling='no' src='https://goo.gl/6ZDJcB'></iframe>"
elif (day=="Wednesday" and meal=="Breakfast"):
       print "<iframe width='200' height='230' frameborder='0' scrolling='no' src='https://goo.gl/pLWBap'></iframe>"
elif (day=="Wednesday" and meal=="Lunch"):
       print "<iframe width='200' height='303' frameborder='0' scrolling='no' src='https://goo.gl/zhFZdF'></iframe>"
elif (day=="Wednesday" and meal=="Snacks"):
       print "<iframe width='200' height='105' frameborder='0' scrolling='no' src='https://goo.gl/Wg5ukp'></iframe>"
elif (day=="Wednesday" and meal=="Dinner"):
       print "<iframe width='200' height='251' frameborder='0' scrolling='no' src='https://goo.gl/S8pbqi'></iframe>"
elif (day=="Thursday" and meal=="Breakfast"):
       print "<iframe width='200' height='230' frameborder='0' scrolling='no' src='https://goo.gl/TF65Em'></iframe>"
elif (day=="Thursday" and meal=="Lunch"):
       print "<iframe width='200' height='303' frameborder='0' scrolling='no' src='https://goo.gl/Hp7VEL'></iframe>"
elif (day=="Thursday" and meal=="Snacks"):
       print "<iframe width='200' height='105' frameborder='0' scrolling='no' src='https://goo.gl/d1tejn'></iframe>"
elif (day=="Thursday" and meal=="Dinner"):
       print "<iframe width='200' height='251' frameborder='0' scrolling='no' src='https://goo.gl/H2iGBe'></iframe>"
elif (day=="Friday" and meal=="Breakfast"):
      print "<iframe width='200' height='230' frameborder='0' scrolling='no' src='https://goo.gl/tYcTpf'></iframe>"
elif (day=="Friday" and meal=="Lunch"):
      print "<iframe width='200' height='230' frameborder='0' scrolling='no' src='https://goo.gl/8X5HQS'></iframe>"
elif (day=="Friday" and meal=="Snacks"):
      print "<iframe width='200' height='105' frameborder='0' scrolling='no' src='https://goo.gl/1ddKns'></iframe>"
elif (day=="Friday" and meal=="Dinner"):
      print "<iframe width='200' height='251' frameborder='0' scrolling='no' src='https://goo.gl/6qBCRC'></iframe>"
elif (day=="Saturday" and meal=="Breakfast"):
      print "<iframe width='200' height='230' frameborder='0' scrolling='no' src='https://goo.gl/7eVFCP'></iframe>"
elif (day=="Saturday" and meal=="Lunch"):
      print "<iframe width='200' height='303' frameborder='0' scrolling='no' src='https://goo.gl/RQguzS'></iframe>"
elif (day=="Saturday" and meal=="Snacks"):
      print "<iframe width='200' height='105' frameborder='0' scrolling='no' src='https://goo.gl/o1BrX3'></iframe>"
elif (day=="Saturday" and meal=="Dinner"):
      print "<iframe width='200' height='251' frameborder='0' scrolling='no' src='https://goo.gl/2s24AQ'></iframe>"
elif (day=="Sunday" and meal=="Breakfast"):
      print "<iframe width='200' height='230' frameborder='0' scrolling='no' src='https://goo.gl/H2nLir'></iframe>"
elif (day=="Sunday" and meal=="Lunch"):
      print "<iframe width='200' height='303' frameborder='0' scrolling='no' src='https://goo.gl/a5GhGi'></iframe>"
elif (day=="Sunday" and meal=="Snacks"):
      print "<iframe width='200' height='105' frameborder='0' scrolling='no' src='https://goo.gl/pwTSE1'></iframe>"
elif (day=="Sunday" and meal=="Dinner"):
      print "<iframe width='200' height='251' frameborder='0' scrolling='no' src='https://goo.gl/YHviww'></iframe>"


cnn.close()

print "</body>"
print "</html>"
