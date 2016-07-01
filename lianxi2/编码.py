#coding:utf-8
import chardet,sys,time
type = sys.getfilesystemencoding()
name = raw_input('输入汉字:')
print chardet.detect(name)['encoding']
print name.decode(type).encode('utf-8')
time.sleep(1000)