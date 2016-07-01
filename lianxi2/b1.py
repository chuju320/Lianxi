#-*-coding:utf-8-*-
#coding=utf-8
#提示框，下拉框处理
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import chardet
driver=webdriver.Firefox()
driver.maximize_window()
driver.get("http://172.16.0.23:8085")
driver.implicitly_wait(10)
driver.find_element_by_id("os_username").clear()
driver.find_element_by_id("os_username").send_keys("kyee")
driver.find_element_by_id("os_password").clear()
driver.find_element_by_id("os_password").send_keys("qwe")
driver.find_element_by_id("loginButton").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='listSystem']/div[9]/img").click()
#.//img[@title='护理人员档案管理']
time.sleep(3)
driver.find_element_by_class_name("tree-title").click()
title=driver.title
print  title
if title==u"护理管理系统-上报事件管理":
    print"进入上报事件系统模块"
else:
    print "页面刷新缓慢或未进入系统页面"
name=driver.find_element_by_id("currentUser").text
print u"现在登陆用户为:%r"%name
time.sleep(2)
A=driver.find_element_by_xpath('//*[@id="tabs"]/div[2]/div[2]/div/iframe')
driver.switch_to_frame(A)
driver.implicitly_wait(30)
#定位下拉框
driver.find_element_by_xpath(".//*[@id='div_button']/div[1]/span[3]/input[1]").click()
#w=driver.find_element_by_class_name("textbox-text textbox-text-readonly validatebox-text")
time.sleep(1)
#定位下拉选项
driver.find_element_by_id("_easyui_combobox_i6_1").click()
time.sleep(2)
#定位查询按钮
driver.find_element_by_id("selectButton").click()
time.sleep(2)

driver.implicitly_wait(30)
driver.find_element_by_xpath(".//span[text()='上报申请']").click()
driver.implicitly_wait(30)
driver.switch_to_frame(0)
time.sleep(1)
'''
a = driver.find_elements_by_xpath(".//div[@id='divSearch']//tr/td/a")
b = driver.find_element_by_xpath(".//a[@id='btnDynamicFetch']").text
print 'a:',a
print 'b:',b,type(b).__name__'''

list1 = ['查询\n ','提取患者信息\n ','鱼骨图录入\n ','保存\n ','返回\n ']

'''
n = a[1].text
c = b.encode('utf-8')
print 'c:',type(c).__name__
print 'c:',c,chardet.detect(c),repr(c)
na = '提取患者信息\n '
print 'na:',na,chardet.detect(na),repr(na)
if c in list1:
    print 'b is OK'
else:
    print 'NO'
'''
for i in range(len(list1)):
    WebDriverWait(driver,30).until(expected_conditions.text_to_be_present_in_element
                               ((By.XPATH,".//div[@id='divSearch']//tr/td/a[%d]"%(i+1)),list1[i].decode('utf-8')))

    print '%s is good!'% list1[i]

driver.quit()


