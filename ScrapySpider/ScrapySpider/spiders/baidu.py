#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/11/16 21:04
# software:PyCharm Community Edition

import scrapy

class TestSpider(scrapy.spiders.Spider):
    name = "baiduSpider"  # 定义名字
    allow_domains = [
        "https://www.qiushibaike.com/"
    ] # 允许爬的范围
    start_urls = ["https://www.qiushibaike.com/pic/"]  # 爬取起始位置

    def parse(self,response):
        content_list = response.xpath("//img/@src")  # 利用xpath 匹配img
        # content_list = response.css("img")   # 利用css匹配img
        # content_list = response.css("img").xpath("@src")  # 利用css和xpath混合匹配img
        for content in content_list:
            self.log(content.extract())
        # self.log(response.body.decode())

