# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from  urllib import request
import time

class ScrapyspiderPipeline(object):
    def process_item(self, item, spider):

        src = item["name"]
        url = src
        # url =  "http  :"+src
        print("++++"*100)
        print(url)
        path ="D:\\img\\"+str(time.time())+".gif"
        try:
            request.urlretrieve(url,path)
        except Exception as  e :
            print(str(e)+"*"*100)
        else:
            print("%s path"%path)
        return item
