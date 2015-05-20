#!/usr/bin/env bash

cd scraper
PYTHONPATH=.. scrapy crawl techcrunch
