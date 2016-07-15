#-*-coding:utf-8-*-
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import chardet
driver=webdriver.Firefox()
driver.maximize_window()
driver.get("http://172.16.12.146:4044/")
driver.implicitly_wait(10)
driver.find_element_by_id("os_username").clear()
driver.find_element_by_id("os_username").send_keys("ljl")
driver.find_element_by_id("os_password").clear()
driver.find_element_by_id("os_password").send_keys("a\n")
#driver.find_element_by_id("loginButton").click()