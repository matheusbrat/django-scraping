from django.db import models

class Outlet(models.Model):
	name = models.CharField(max_length=255)
	url  = models.CharField(max_length=255)
	description = models.CharField(max_length=255)

class Writer(models.Model):
	name = models.CharField(max_length=255)
	twitter = models.CharField(max_length=255)
	profile = models.CharField(max_length=255)

class Article(models.Model):
	writers = models.ManyToManyField(Writer)
	outlet = models.ForeignKey(Outlet)
	publication_date = models.DateField()
	content = models.TextField()