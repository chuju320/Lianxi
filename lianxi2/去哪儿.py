#-*-coding:utf-8-*-
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://www.qunar.com/')
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_xpath(".//*[text()='出发']/following-sibling::input").clear()
driver.find_element_by_xpath(".//*[text()='出发']/following-sibling::input").send_keys(u'成都(CTU)')
time.sleep(2)
driver.find_elements_by_id('js_domestic_fromdate')[0].clear()
driver.find_elements_by_id('js_domestic_fromdate')[0].send_keys('2016-08-10')
#js1 = '$("input[name=\'fromDate\']").attr("value","2016-08-20 10:10:10")'
#driver.execute(js1)
time.sleep(2)
driver.find_element_by_xpath(".//div[text()='到达']/following-sibling::input").clear()
driver.find_element_by_xpath(".//div[text()='到达']/following-sibling::input").send_keys(u'北京(BJS)')
time.sleep(2)
driver.find_element_by_xpath(".//*[@id='js_flight_domestic_searchbox']/div[2]/div[2]/div[3]/div/div/div[1]").click()
time.sleep(0.5)
driver.find_element_by_name('toDate').clear()
driver.find_element_by_name('toDate').send_keys('2016-08-20')
time.sleep(2)
driver.find_element_by_xpath(".//span[@class='p_btn']/button").click()
