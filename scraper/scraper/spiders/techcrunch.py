# -*- coding: utf-8 -*-
import django
django.setup()

import scrapy
from scraper.items import OutletItem, WriterItem, ArticleItem
from scrapingapp.models import Outlet, Writer, Article
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy import Selector
from scrapy.contrib.spiders import Rule
from scrapy import log
from scrapy.http import Request
from datetime import datetime
import re

class TechcrunchSpider(scrapy.Spider):
    name = "techcrunch"
    allowed_domains = ["techcrunch.com"]
    start_urls = (
        'http://www.techcrunch.com',
    )

    # rules = (
    #   Rule(LxmlLinkExtractor(allow=(), restrict_xpaths=(), process_value='parse_text'))
    # )

    def getOutlet(self, sel, response):
      name = sel.xpath('//meta[@property="og:site_name"]/@content').extract()[0]
      description = sel.xpath('//meta[@property="og:description"]/@content').extract()[0]
      url = self.start_urls[0]
      outlet, created = Outlet.objects.get_or_create(name=name, url=url, description=description)
      return outlet

    def getWriters(self, sel, response):
      names = sel.xpath('//a[@rel="author"]/text()').extract()
      urls = sel.xpath('//a[@rel="author"]/@href').extract()
      twitters = sel.xpath('//span[@class="twitter-handle"]/a/text()').extract()
      writers = []
      for quantity in range(len(names)):
        name = names[quantity]
        url = urls[quantity]
        twitter = twitters[quantity]
        writer, created = Writer.objects.get_or_create(name=name, profile=self.start_urls[0] + url, twitter=twitter)  
        writers.append(writer)
      return writers

    def parse(self, response):
      sel = Selector(response)
      outlet = self.getOutlet(sel, response);

      links = sel.xpath('//h2[@class="post-title"]/a/@href').extract()
      for link in links:
        article = ArticleItem.django_model.objects.filter(url=link)
        if len(article) == 0:
          meta = dict()
          meta['outlet'] = outlet
          yield Request(link, callback=self.parse_article, meta=meta)
        else:
          log.msg("Already have it on db " + link)

    def parse_article(self, response):
      sel = Selector(response)
      writers = self.getWriters(sel,response)

      title = sel.xpath('//h1[@class="alpha tweet-title"]/text()').extract()[0]
      url = response.url
      content = sel.xpath('//div[@class="article-entry text"]//p//text()').extract()
      content = ''.join(content)
      image = sel.xpath('//meta[@property="og:image"]/@content').extract()[0]
      publication_date = sel.xpath('//meta[@name="timestamp"]/@content').extract()[0]
      log.msg(title);
      log.msg(url);
      log.msg(content);
      log.msg(image);
      log.msg(publication_date);
