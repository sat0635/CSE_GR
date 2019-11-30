# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Subject(models.Model):
	TITLE=models.CharField(max_length=20)
	CODE=models.CharField(max_length=20)
	GRADE=models.IntegerField(default=0)
	CALSS=models.CharField(max_length=10)
	def __str__(self):
		return self.TITLE


class Gr(models.Model):
	USERID=models.CharField(max_length=20)
	CONTENT=models.CharField(max_length=100)
	def __str__(self):
		return self.CONTENT
