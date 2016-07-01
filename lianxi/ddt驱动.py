#-*-coding:utf-8-*-
import unittest
from selenium import webdriver
from ddt import ddt,data,unpack
import time

@ddt
class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')
        self.addCleanup(self.driver.quit)

    @data( ('','',u'请您填写手机/邮箱/用户名'),('admin','',u'请您填写密码'),
           ('','admin',u'请您填写手机/邮箱/用户名'))
    @unpack
    def testLogin(self,value1,value2,expected):
        self.driver.find_element_by_link_text(u'登录').click()
        time.sleep(1)
        print '输入百度账号'
        self.driver.find_element_by_id('TANGRAM__PSP_8__userName').clear()
        self.driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys(value1)
        time.sleep(1)
        print '输入密码'
        self.driver.find_element_by_id('TANGRAM__PSP_8__password').clear()
        self.driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys(value2)
        time.sleep(1)
        print '点击登录'
        self.driver.find_element_by_id('TANGRAM__PSP_8__submit').click()
        print '获取返回的错误信息'
        time.sleep(1)
        errorText = self.driver.find_element_by_id('TANGRAM__PSP_8__error').text
        self.assertTrue(errorText,expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)