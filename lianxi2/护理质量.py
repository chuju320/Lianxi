#-*-coding:utf-8-*-
from selenium import webdriver
import os,time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://172.16.0.23:8085/login.html')
driver.implicitly_wait(30)
driver.find_element_by_id('os_username').clear()
driver.find_element_by_id('os_username').send_keys('autotest')
time.sleep(1)
driver.find_element_by_id('os_password').clear()
driver.find_element_by_id('os_password').send_keys('kyee')
time.sleep(1)
driver.find_element_by_id('loginButton').click()
driver.implicitly_wait(30)

driver.find_element_by_xpath(".//*[@title='护理人员档案管理']").click()
time.sleep(1)
driver.find_element_by_xpath(".//img[@title='人员信息查询']").click()
time.sleep(1)
driver.find_element_by_xpath(".//img[@title='科室人员信息二维码']").click()
time.sleep(1)
frame = driver.find_element_by_xpath(".//body[@id='layout']/div[4]//iframe")
driver.switch_to_frame(frame)
time.sleep(1)
driver.find_element_by_id("userName").send_keys('autotest')
time.sleep(0.5)
driver.find_element_by_xpath(".//span[text()='查询']").click()
time.sleep(1)
#------------------------系统设置-功能模块-右键菜单------------------------------
#frame = driver.find_element_by_xpath(".//body[@id='layout']/div[4]//iframe")
#driver.switch_to_frame(frame)
#time.sleep(2)
#driver.find_elements_by_xpath(".//button[text()=' 预览图片']")[0].click()
#mouse = driver.find_element_by_xpath(".//span[text()='护理人员档案管理']")
#ActionChains(driver).context_click(mouse).perform()
#time.sleep(1)
#driver.find_element_by_xpath(".//div[@id='mm']/div[2]/div").click()
#time.sleep(1)
#------------------------系统设置-功能模块-右键菜单------------------------------

name = driver.find_elements_by_xpath(".//td[@field='USER_NAME']")[1].text
time.sleep(1)
print name=='autotest'

driver.f
driver.quit()