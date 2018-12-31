#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/11/21 20:03
# software:PyCharm Community Edition

import scrapy
from  scrapy.selector import Selector
from 学神1809.ScrapySpider.ScrapySpider.items import ScrapyspiderItem

class TestSpidery(scrapy.spiders.Spider):
    name = "qiushiSpidery"

    def start_requests(self):

        url = "https://www.qiushibaike.com/pic/"
        # url = "https://www.baidu.com/"
        url = "http://www.xiaohuar.com/hua/"
        # url = "http://www.965dyy.com/dianying/lunli/"

        header =  {
            # "Referer":"http://www.965dyy.com/",

            # "Referer":"http://www.xiaohuar.com/",
            "Referer":"https://www.qiushibaike.com/",
            "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36"
        }
        yield  scrapy.Request(url=url,headers=header,method='GET')
    def parse(self,response):
        # select = Selector(response)
        # self.log(select)
        img_list = response.xpath("//img/@src")
        for img in img_list:
            item = ScrapyspiderItem()
            item["name"] = img.extract()
            # self.log(item)
            yield item




