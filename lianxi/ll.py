#-*-coding:utf-8-*-

from selenium import webdriver
import  time

driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(1)
driver.get('http://www.baidu.com')
time.sleep(1)

js = 'return jQuery.find("[value=\'百度一下\'")'
a = driver.execute_script(js)
print a