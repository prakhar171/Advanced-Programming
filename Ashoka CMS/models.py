# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Monday(models.Model):
	selection=models.CharField(max_length=5)
	# capacity=models.CharField(max_length=2)
	# location=models.CharField(max_length=50)
	number=models.CharField(max_length=10)
	# status=models.NullBooleanField(null=False)

	def __str__ (self):
		return self.selection + ' - ' + self.number

class Info(models.Model):
	number = models.ForeignKey(Monday, on_delete=models.CASCADE)
	capacity=models.CharField(max_length=2)
	location=models.CharField(max_length=50)
	status=models.NullBooleanField(null=False)

	def __str__ (self):
		return self.status