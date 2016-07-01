#-*-coding:utf-8-*-
import pythoncom
import pyHook

def onKeyboardEvent(event):
    if event.Key != 'W' and event.Key != 'w':
        while 1:
                print '1'
        else:
            print '结束'
    return True
#创建一个钩子管理器
hm = pyHook.HookManager()
#监听所有键盘事件
hm.KeyDown = onKeyboardEvent
#设置键盘钩子
hm.HookKeyboard()
pythoncom.PumpMessages()