#-*-coding:utf-8-*-
import time
from selenium import webdriver


driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(1)
driver.get('https://www.douban.com/accounts/login')
driver.implicitly_wait(30)

driver.add_cookie({'name':'bid','value':'1132960777@qq.com'})
driver.add_cookie({'name':'ps','value':'jl1989421'})
time.sleep(1)
driver.get('https://www.douban.com/accounts/login')

print driver.get_cookies()
