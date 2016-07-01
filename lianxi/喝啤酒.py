#-*-coding:utf-8-*-
'''
    啤酒2块钱一瓶，4个瓶盖可以免费换一瓶，2个空瓶子可以免费换一瓶，求10块钱总共可以喝几瓶酒
'''

def sum(num):
    a = num/2
    s = 0  #喝酒数
    n = 0  #瓶盖
    m = 0  #空瓶
    while a > 0:
        n += 1
        m += 1
        if n >= 4:
            a += 1
            n -= 4
        if m >= 2:
            a += 1
            m -= 2
        a -= 1
        s += 1

    print s

sum(10)