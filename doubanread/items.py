# -*- coding: utf-8 -*-
import scrapy


class DoubanreadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    book_url = scrapy.Field()
    book_star = scrapy.Field()
    book_about = scrapy.Field()

