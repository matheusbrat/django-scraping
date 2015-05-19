# -*- coding: utf-8 -*-
import django
django.setup()

import scrapy
from scraper.items import OutletItem, WriterItem, ArticleItem
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy import Selector
from scrapy.contrib.spiders import Rule
from scrapy import log

class TechcrunchSpider(scrapy.Spider):
    name = "techcrunch"
    allowed_domains = ["techcrunch.com"]
    start_urls = (
        'http://www.techcrunch.com/',
    )

    # rules = (
    # 	Rule(LxmlLinkExtractor(allow=(), restrict_xpaths=(), process_value='parse_text'))
    # )

    def parse(self, response):
    	sel = Selector(response)
    	links = sel.xpath('//h2[@class="post-title"]/a/@href').extract()
    	for link in links:
    		article = ArticleItem.django_model.objects.filter(url=link)
    		if len(article) == 0:
    			log.msg("Downaloading " + link)
    		else:
    			log.msg("Already have it on db")
    		
    	return OutletItem(name='Abc', url='test.com', description='description')

   	def parse_text(response):
			log.msg("TESTE2")
    	log.msg(response.url)
    	return OutletItem(name='Abc', url='test.com', description='description')   		