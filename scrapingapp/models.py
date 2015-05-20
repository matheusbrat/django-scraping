from django.db import models

class Outlet(models.Model):
	name = models.CharField(max_length=255)
	url  = models.CharField(max_length=255, unique=True)
	description = models.CharField(max_length=255)

class Writer(models.Model):
	name = models.CharField(max_length=255)
	twitter = models.CharField(max_length=255)
	profile = models.CharField(max_length=255, unique=True)

class Article(models.Model):
	writers = models.ManyToManyField(Writer)
	outlet = models.ForeignKey(Outlet)
	publication_date = models.DateTimeField()
	content = models.TextField()
	url = models.URLField(null=True)
	title = models.TextField(default=None)
	image = models.TextField(default=None)

	