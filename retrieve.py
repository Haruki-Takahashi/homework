#-*- coding:utf-8 -*-
import urllib.request
url='http://www.baidu.com'
urllib.request.urlretrieve(url,'./html.txt')#保存在当前路径的html.txt中