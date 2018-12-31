#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:黎涛
# datetime:2018/11/16 21:46
# software:PyCharm Community Edition

# def yieldTest():
#     a = 0
#     b = 1
#     a,b=b,a+b
#     yield b
# print(yieldTest())
#
# for i in yieldTest():
#     print(i)

# def yieldTest(Max):
#     a,b,c = 0,0,1
#     while a < Max:
#         yield c
#         b,c=c,b+c
#         a+=1
# print(yieldTest(8))
pardre = """tn: baiduimage
ct: 201326592
lm: -1
cl: 2
ie: gb18030
word: (unable to decode value)
fr: ala
ala: 1
alatpl: adress
pos: 0
hs: 2
xthttps: 111111"""
import os
# dicdd = [line for line in pardre.split("\n")]
# # print(dicdd)
# padd_dict={}
# for i in dicdd:
#     kv = i.split(": ")
#     # print(kv)
#     if len(kv) ==2:
#         padd_dict[kv[0]] =kv[1]
#     elif len(kv)==1:
#         padd_dict[kv[0]]=""
# print(padd_dict)

str1 = 'pic/sdsd/?35s'

print(str1.split('/'))
