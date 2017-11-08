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
day  = form.getvalue('Day')
meal = form.getvalue('Meal')

print "<html>"
print "<head>"
print "<title>Room Bookings</title>"
print "</head>"


if day=="Monday" and meal=="Breakfast":
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Monday" and meal=="Lunch"):
     print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://goo.gl/nkZQ1g'></iframe>"                       

    
elif (day=="Monday" and meal=="Snacks"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Monday" and meal=="Dinner"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Tuesday" and meal=="Breakfast"):
    print "<iframe width='200' height='230' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&AllowTyping=True&ActiveCell='30%20OCT%20to%2005%20Nov%2017'!C5&Item='30%20OCT%20to%2005%20Nov%2017'!C5%3AC12&wdHideGridlines=True&wdDownloadButton=True&wdInConfigurator=True'></iframe>"
elif (day=="Tuesday" and meal=="Lunch"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Tuesday" and meal=="Snacks"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Tuesday" and meal=="Dinner"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Wednesday" and meal=="Breakfast"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Wednesday" and meal=="Lunch"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Wednesday" and meal=="Snacks"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Wednesday" and meal=="Dinner"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Thursday" and meal=="Breakfast"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       
elif (day=="Thursday" and meal=="Lunch"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Thursday" and meal=="Snacks"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Thursday" and meal=="Dinner"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Friday" and meal=="Breakfast"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Friday" and meal=="Lunch"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Friday" and meal=="Snacks"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Friday" and meal=="Dinner"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Saturday" and meal=="Breakfast"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Saturday" and meal=="Lunch"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Saturday" and meal=="Snacks"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Saturday" and meal=="Dinner"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Sunday" and meal=="Breakfast"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Sunday" and meal=="Lunch"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Sunday" and meal=="Snacks"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       

elif (day=="Sunday" and meal=="Dinner"):
    print "<iframe width='204' height='252' frameborder='0' scrolling='no' src='https://onedrive.live.com/embed?resid=640F5B6FB6A804C%21807&authkey=%21ABxP6VSeANl0lAc&em=2&wdAllowInteractivity=False&Item='30%20OCT%20to%2005%20Nov%2017'!B4%3AB12&wdHideGridlines=True&wdInConfigurator=True'></iframe>"                       



cnn.close()

print "</body>"
print "</html>"
