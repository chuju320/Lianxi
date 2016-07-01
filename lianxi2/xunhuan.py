#-*-coding:utf-8-*-
import pythoncom, pyHook,sys,time,thread,os
import win32gui,win32api,win32con
from selenium import webdriver
import subprocess
Lcontrol_press = False
Lmenu_press = False

def OnKeyboardEvent(event):
    global Lcontrol_press #在函数里面使用全局变量的时候要加上global关键字
    global Lmenu_press
    print 'Key:', event.Key
    if event.Key == "Lcontrol":
        Lcontrol_press = True
    if event.Key == "Lmenu":
        Lmenu_press = True
    handel_key()

    return True
def handel_key() :
    global Lcontrol_press
    global Lmenu_press
    if Lcontrol_press and Lmenu_press:
        print 'good'
        Lcontrol_press = False
        Lmenu_press = False
        #sys.exit()
        subprocess.call("pause",shell=True)
def ss(name):
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()

def f(name):
    while 1:
        try:
            driver = webdriver.Firefox()
        except:
            driver = webdriver.Ie()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get('http://www.baidu.com')
        driver.implicitly_wait(30)
        driver.find_element_by_id('kw').send_keys('fanyi The head is not bad!')
        time.sleep(1)
        driver.find_element_by_id('su').click()
        print 'hehe'
        time.sleep(1)
        driver.close()
def num(name):
    a = 1
    while a:
        print 'hit your ass %s times' %a
        a += 1
        time.sleep(1)
try:
    thread.start_new_thread(ss,('Thread-1',))
    thread.start_new_thread(f,('Thread-2',))
    thread.start_new_thread(num,('Thread-3',))
except:
    print 'The thread lost!'

while 1:
    pass