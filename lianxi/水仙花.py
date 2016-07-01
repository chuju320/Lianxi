#-*-coding:utf-8-*-
'''\
题目：打印出1000内所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数
　　　本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
'''

'''另一种解法'''
n = 0
for i in range(1000):
    a = i/100
    b = i/10%10
    c = i%10
    if a**3 + b**3 + c**3 == a*100 + b*10 + c and a != 0:
        n += 1
        print a,b,c