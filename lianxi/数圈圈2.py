#-*-coding:utf-8-*-
'''\
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出
　　　圈子，问最后留下的是原来第几号的那位。
'''
n = 5
list_people = []
for x in xrange(n):
    list_people.append(x+1)
def devThree(serial_num = 1):
    for x in xrange(len(list_people)):
        if list_people[x] != 0:
            if serial_num == 3:
                list_people[x] = 0
                serial_num = 1
            else:
                serial_num += 1
    total = 0
    for i in list_people:
        if i != 0:
            total += 1
    if total >1:
        devThree(serial_num)
    else:
        return
devThree()
print "___________________________________"
print list_people
for i in xrange(len(list_people)):
    if list_people[i] >0:
        print list_people[i]
