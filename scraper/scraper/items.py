# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Field
from scrapingapp.models import Outlet, Writer, Article

class OutletItem(DjangoItem):
	django_model = Outlet

class WriterItem(DjangoItem):
	django_model = Writer

class ArticleItem(DjangoItem):
	django_model = Article
