# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import Http404
from .models import Monday
from django.template import loader
from django.shortcuts import render
#from django.shortcuts import render


# Create your views here.
def index(request):
	all_days = Monday.objects.all()
	#template= loader.get_template('RoomBooking/index.html')
	# context = { 
	# 'all_days': all_days,
	# }
	# html = ''
	# for day in all_days:
	# 	url = '/RoomBooking/' + str(day.id) +  '/'
	# 	html +='<a href = "' + url + '">' + day.number + '</a><br>'
	#return HttpResponse(html)
	return render(request, 'RoomBooking/index.html', {'all_days': all_days})

def detail(request, number):
	# all_days = Monday.objects.all()
	# html = ''
	# for day in all_days:
		
	# 	html +='Info for room number' + str(day) + '<br>'
	# return HttpResponse(html)
	#return HttpResponse("<h2>Info for room " + str(number) + "</h2>")
	try:
		day = Monday.objects.get(pk=number)
	except Monday.DoesNotExist:
		raise Http404("number does not exist")
	return render ( request, 'RoomBooking/detail.html', {'number': number})