#-*-coding:utf-8-*-
'''\
题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程
　　　找出1000以内的所有完数。
'''


for i in range(2,1001):
    list = []
    s = i
    for j in range(1,i):
        if i % j == 0:
            s -= j
            list.append(j)
    if s == 0:
        print i
        for a in list:
            print a,
        print