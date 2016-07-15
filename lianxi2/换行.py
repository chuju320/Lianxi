#-*-coding:utf-8-*-


f = open('123.txt')
for i in  f.readlines():
    print repr(i)
f.close()