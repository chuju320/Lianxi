#-*-coding:utf-8-*-
import urllib as ur

res =ur.urlopen('http://www.baidu.com')
html = res.read()
print html.decode('utf-8')
