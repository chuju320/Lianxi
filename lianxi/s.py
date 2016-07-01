#-*-coding:utf-8-*-
from selenium import webdriver
import time,os
#import s2

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Firefox()
driver.maximize_window()
time.sleep(0.5)
driver.get('http://172.16.0.23:8013/Index.aspx')
driver.find_element_by_id('txtName').clear()
driver.find_element_by_id('txtName').send_keys('admin')
driver.find_element_by_id('txtPassWord').clear()
driver.find_element_by_id('txtPassWord').send_keys('admin')
driver.find_element_by_id('Button1').click()

time.sleep(1)
driver.switch_to_frame(driver.find_element_by_name('leftFrame'))
time.sleep(1)
driver.find_element_by_id('imgmenu3').click()
time.sleep(1)
driver.find_element_by_xpath("//a[text()='HIS人员查询']").click()
time.sleep(1)
driver.switch_to_default_content()
time.sleep(0.5)
driver.switch_to_frame(driver.find_element_by_name('mainFrame'))
time.sleep(1)
#driver.find_element_by_id('ddl_Dept').click()
#time.sleep(1)
#driver.find_element_by_xpath(".//*[@id='ddl_Dept']/option[1]").click()
#time.sleep(1)
driver.find_element_by_id('btn_Select')
time.sleep(1)
driver.find_element_by_xpath("//td[text()='rt']/following-sibling::td//a[text()='删除']").click()
time.sleep(1)
# v = [u'class name',u'xubox_iframe']
# a = driver.find_element(*v)
# driver.switch_to_frame(a)
driver.find_element_by_xpath('//a[text()="取消"]').click()
#driver.find_element_by_id('imgmenu3').click()
time.sleep(1)


