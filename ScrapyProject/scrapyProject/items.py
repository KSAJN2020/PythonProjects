# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesItem(scrapy.Item):
    # define the fields for your item here like:
    text = scrapy.Field()
    author=scrapy.Field()
    tags=scrapy.Field()
    last_upd_timestamp = scrapy.Field()

class CoreyMSItem(scrapy.Item):
    # define the fields for your item here like:
    header = scrapy.Field()
    summary=scrapy.Field()
    youtube_link=scrapy.Field()
