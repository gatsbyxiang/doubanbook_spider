# -*- coding: utf-8 -*-

import scrapy
import sys
from doubanread.items import DoubanreadItem
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import Rule,CrawlSpider
from scrapy.linkextractors import LinkExtractor

reload(sys)
sys.setdefaultencoding('utf8')

class DoubanreadSpider(scrapy.Spider):
    name = "doubanread"


    allowed_domains = []
    start_urls = [
        "https://book.douban.com/top250?start=0"
    ]



    def parse(self, response):

        for sel in response.xpath("//tr[@class='item']/td[2]"):

            item = DoubanreadItem()

            book_name = sel.xpath('div/a/text()').extract()
            book_url = sel.xpath('div/a/@href').extract()
            book_star = sel.xpath('div[2]/span[2]/text()').extract()
            book_about = sel.xpath('p[1]/text()').extract()

            item['book_name'] = [n.encode('utf-8') for n in book_name]
            item['book_url'] = [url for url in book_url]
            item['book_star'] = [s for s in book_star]
            item['book_about'] = [a.encode('utf-8') for a in book_about]

            yield item

        next_url = response.xpath(".//div[@class='paginator']/span[3]/a/@href").extract()
        if next_url:
            next_url = next_url[0]
            yield Request(next_url)



# .// li / div[2] / h2 / a
# .// li / div[2] / div[1]
# .// li / div[2] / div[2] / span[2]


