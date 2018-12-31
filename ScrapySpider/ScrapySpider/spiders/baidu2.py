#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/11/16 21:59
# software:PyCharm Community Edition

import scrapy
from  scrapy import  Request

class TestSpider(scrapy.spiders.Spider):
    name = "baiduSpiderFly"  # 定义名字

    def start_requests(self):
        url = "https://www.baidu.com"

        headers = {
            "User - Agent": "Mozilla / 5.0(Windows NT 10.0;Win64; x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 67.0.3396 .99Safari / 537.36"

        }
        yield Request(url,headers=headers)