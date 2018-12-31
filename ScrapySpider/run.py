#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/11/16 21:23
# software:PyCharm Community Edition

from  scrapy import  cmdline

# 执行调用命令

cmdline.execute(("scrapy crawl qiushiSpidery").split())
# cmdline.execute(("scrapy crawl baiduSpiderFly").split())