# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import json
import codecs
reload(sys)
sys.setdefaultencoding('utf8')

class DoubanreadPipeline(object):

    def __init__(self):
        self.file = codecs.open('doubanread.json',mode='wb',encoding='utf-8')

    def process_item(self, item, spider):

        # 保存为txt文件
        # filename  = 'doubanread.txt'
        # with open(filename,'a') as fp:
        #     for i in range(len(item['book_name'])):
        #         fp.write(item['book_name'][i]+'\t'+item['book_star'][i]+'\t'+item['book_about'][i]+'\t'+item['book_url'][i])
        # return item


        for i in range(len(item['book_star'])):

            book_name = {'book_name':str(item['book_name'][i]).replace('\n','')}
            book_star = {'book_star': item['book_star'][i].replace('\n','')}
            book_url = {'book_url': item['book_url'][i].replace('\n','')}
            book_about = {'book_about':str(item['book_about'][i]).replace(' ','').replace('\n','')}
            line =  json.dumps(book_name, ensure_ascii=False)
            line = line + json.dumps(book_star, ensure_ascii=False)
            line = line + json.dumps(book_url,ensure_ascii=False)
            line = line + json.dumps(book_about,ensure_ascii=False) +'\n\n'



        self.file.write(line)

    def close_spider(self,spider):
        self.file.close()




