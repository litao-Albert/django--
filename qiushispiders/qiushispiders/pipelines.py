# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from  urllib import request
import time
class QiushispidersPipeline(object):
    def process_item(self, item, spider):
        src = item["src"]

        url = "http:"+ src
        print(url)
        path = "D:\\img\\"+str(time.time())+".jpg"
        try:
            request.urlretrieve(url,path)
        except Exception as e:
            print(e)
        else:
            print("正在爬去，请稍等")


        return item
