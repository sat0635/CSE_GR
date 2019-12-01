# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Subject(models.Model):
	TITLE=models.CharField(max_length=20)
	USEREMAIL=models.CharField(max_length=20,default = "NULL")
	CODE=models.CharField(max_length=20)
	GRADE=models.IntegerField(default=0)
	CLASS=models.CharField(max_length=10)
	def __str__(self):
		return self.TITLE


class Gr(models.Model):
	USEREMAIL=models.CharField(max_length=20)
	CONTENT=models.CharField(max_length=100)
	def __str__(self):
		return self.CONTENT


class CSEIntenCoSubject(models.Model):
	TITLE=models.CharField(max_length=20)
	CODE=models.CharField(max_length=20)
	CLASS=models.CharField(max_length=20)
	GRADE=models.IntegerField(default=0)
	ISDESIGN=models.BooleanField(default=False)
	def __str__(self):
		return self.TITLE

class CSEIntenCoNonSubject(models.Model):
	TITLE=models.CharField(max_length=20)
	CONTENT=models.CharField(max_length=100)
	def __str__(self):
		return self.TITLE

