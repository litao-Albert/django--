#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/11/23 19:55
# software:PyCharm Community Edition

import  scrapy
import time

from 学神1809.qiushispiders.qiushispiders.items import QiushispidersItem

class QinShi(scrapy.spiders.Spider):
    name = 'qinshi'
    allowed_domians = [
        "qiushibaike.com"
    ]
    start_urls = [
        "https://www.qiushibaike.com/pic/"
    ]

    def parse(self,response):

        page_list = response.xpath("//ul[@class='pagination']/li/a/@href")
       # [<Selector xpath="//*[@id='content-left']/ul/li/a/@href" data='/pic/page/2?s=5143270'>,
        # <Selector xpath="//*[@id='content-left']/ul/li/a/@href" data='/pic/page/3?s=5143270'>, <Selector xpath="//*[@id='content-left']/ul/li/a/@href" data='/pic/page/4?s=5143270'>, <Selector xpath="//*[@id='content-left']/ul/li/a/@href" data='/pic/page/5?s=5143270'>, <Selector xpath="//*[@id='content-left']/ul/li/a/@href" data='/pic/page/35?s=5143270'>, <Selector xpath="//*[@id='content-left']/ul/li/a/@href" data='/pic/page/2?s=5143270'>]
        # /pic/page/35?s=5143270'>]
        last_num = page_list[-2].extract() # 获取：/pic/page/35?s=5143270
        num = int(last_num.rsplit("?",1)[0].rsplit("/",1)[1])  #  获取 35
        pRang = range(1,num+1)
        for page in pRang:
            page_url = "https://www.qiushibaike.com" + last_num.replace(str(num), str(page))   #   得到/pic/page/35?s=5143270
            print(page_url)
    #
            yield scrapy.Request(page_url,callback=self.get_img,dont_filter=True)
            time.sleep(2)

    def get_img(self,response):

        img_src_list = response.xpath("//div[@id='content-left']//img/@src")
        for img in img_src_list:

            item= QiushispidersItem()
            item["src"] = img.extract()
            yield item


