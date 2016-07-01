#-*-coding:utf-8-*-
'''\
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出
　　　圈子，问最后留下的是原来第几号的那位。
'''

list2 = ['小明','小红','小王','小李','小吴','小花','小郑','小鱼','小何','小徐']
def s(list,k):
    while len(list)>1:
        for i in range(len(list)):
            if k % 3 == 0:
                print list[0],'数到了3，被去除'
                list.remove(list[0])
            else:
                #print k,'被转移'
                list.append(list[0])
                list.remove(list[0])
            #print list
            k += 1
        s(list,k)
    else:
        print '最后剩余:',list[0].decode('utf-8')
s(list2,1)