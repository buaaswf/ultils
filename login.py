#!/usr/bin/env python 
# -*- coding:utf-8 -*- 
'''
 * @Author: shifaqiang(石发强)--[14061115@buaa.edu.cn] 
 * @Date: 2018-12-02 19:22:42 
 * @Last Modified by:   shifaqiang 
 * @Last Modified time: 2018-12-02 19:22:42 
 * @Desc: a tool to login in Campus Network of BeiHang University by command line when you are no UI Web broswer
    usage: 
        python login.py
        then you can type your username and password for Campus Network of BeiHang University
'''

import requests
import bs4
import getpass
import base64

username=input("username:")
password=getpass.getpass("password:")

url="https://gw.buaa.edu.cn:801/beihangview.php"
params={"username":username,
     "ac_id":22,
     "action":"login",
     "password":password}
result=requests.post(url,data=params)
result=bs4.BeautifulSoup(result.text,"lxml")
try:
    p=result.findAll(attrs={"alert alert-success"})[0]
    print(p.findAll()[0].text)
except:
    print("用户名不存在或密码错误")
