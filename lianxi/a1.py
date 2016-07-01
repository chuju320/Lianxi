#coding:utf-8

import os



file = 'xunbao.py'
path = r'E:\12'
b = r'C:\Python27\Scripts\pyinstaller.exe --onefile %s --distpath %s'%(file,path)

os.system(b)
