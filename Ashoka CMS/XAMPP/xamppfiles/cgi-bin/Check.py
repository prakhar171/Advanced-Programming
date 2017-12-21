#!/usr/bin/python
import mysql.connector
from mysql.connector import errorcode
# Import modules for CGI handling 
import cgi, cgitb
print "Content-type:text/html\r\n\r\n"
cnn=mysql.connector.connect(user = "root", password = "", host = "localhost", database = "Rooms")
print '<html>'
print '<head>'
print '<title>Hello Word - First CGI Program</title>'
print '</head>'
print '<body>'
print '<h2>Hello Word! This is my first CGI program</h2>'
print '</body>'
print '</html>'