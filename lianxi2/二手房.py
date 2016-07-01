#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("http://b.eb.test.fang.com")
driver.maximize_window()
time.sleep(1)
driver.find_element_by_id("str_username").clear()
driver.find_element_by_id("str_username").send_keys("zusoufun111")
time.sleep(1)
js1="$(\"input[id='txtpasswd']\").removeAttr('onfocus');$(\"input[id='txtpasswd']\").removeAttr('onblur')"
driver.execute_script(js1)
time.sleep(1)
driver.find_element_by_id("txtpasswd").clear()
driver.find_element_by_id("txtpasswd").send_keys("zf2016")

time.sleep(1)
driver.find_element_by_id("login_submit").click()
#driver.find_element_by_id("ogin_submit").submit()
time.sleep(1)
driver.quit()