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
	CATEGORY=models.CharField(max_length=100,default = "N")
	CONTENT=models.CharField(max_length=100,default="N")
	def __str__(self):
		return self.CATEGORY


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

class GlobalSWCoSubject(models.Model):
	TITLE=models.CharField(max_length=20)
	CODE=models.CharField(max_length=20)
	CLASS=models.CharField(max_length=20)
	GRADE=models.IntegerField(default=0)
	def __str__(self):
		return self.TITLE

class GlobalSWCoNonSubject(models.Model):
	TITLE=models.CharField(max_length=20)
	TRACK=models.CharField(max_length=20,default="N")
	CONTENT=models.CharField(max_length=100)
	def __str__(self):
		return self.TITLE


class User(models.Model):
	USEREMAIL=models.CharField(max_length=100)
	STUDENT_NUMBER=models.IntegerField(default=0)
	MAJOR=models.CharField(max_length=20,default="N")
	TRACK=models.CharField(max_length=20,default="N")
	def __str__(self):
		return self.USEREMAIL


class Question(models.Model):
	USEREMAIL=models.CharField(max_length=100)
	TITLE=models.CharField(max_length=100)
	DESC=models.TextField(max_length=1000)
	def __str__(self):
		return self.TITLE

	
