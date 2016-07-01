#-*- coding:utf-8 -*-

import sys
import random
import time
import cPickle as p
reload(sys)
sys.setdefaultencoding('utf-8')
sign = {'admin' : 'admin'}
class room:
    '''地图的设置'''
    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.paths = {}
    def go(self,direction):
        return self.paths.get(direction,None)    
    def add_map(self,paths):
        self.paths.update(paths)
    def scan(self):
        print '接下来，你可以选择的地方：'.decode('utf-8') ,
        for name,address in self.paths.items():
            print name,'、',

start = room('地洞之门',
'''宝藏所在地的入口，杂草覆盖，乱木丛生，很是阴森，不过为了洞里的宝藏，拼了命也要进去！'''
                    )

monster = room('怪兽之屋',
'''你不慎闯入了怪兽SaTar的栖息地，它恶狠狠的看着你，对于你这样冒失的闯入者，它从来都是致命一击，毫不留情！'''
               )
lucky = room('幸运之沼',
'''虽然这是个沼泽之地，但是并不会要了你的小命，而且还给你带来了福音：它的里面有把宝剑，有了宝剑，你可以轻松打败宝藏守卫！'''
             )
dead = room('死亡之窟',
'''很不幸，你进入了死亡之窟，在这里没有人能走的出去，你也不例外，看到到处都是骷髅，你应该明白自己很难成为幸运儿！'''
            )
gold = room('黄金之城',
'''哈哈，恭喜终于到达了黄金之城，在这里有数不尽的黄金财宝，但是还有一个问题，有一个千年守卫\
一直守在这里，虽然你是为数不多的能够进入这里的冒险者，但是能不能拿到宝藏，还得守卫说了算！'''
            )
start.add_map({     '怪兽之屋' : monster,
                            '幸运之沼' : lucky
                    }) 
monster.add_map({    '地洞之门' : start,
                                '幸运之沼' : lucky
                 })
lucky.add_map({        '地洞之门' : start,
                                '黄金之城' : gold,
                                '死亡之窟' : dead,
                                '怪兽之屋' : monster
               })
dead.add_map({          '幸运之沼' : lucky
              })

def reg():
    '''注册模块'''
    global sign
    sign = { 'admin' : 'admin' }
    print 
    print '**注册用户名**'.decode('utf-8')
    name = raw_input('请输入用户名：'.decode('utf-8'))
    add_file(name)    #检查数据重复
    pwd = raw_input('请输入密码：'.decode('utf-8'))
    pwd2 = raw_input('请再次输入密码：'.decode('utf-8'))

    if name and pwd and pwd2:
        if pwd == pwd2:    
            sign[name] = pwd
            reg_txt(sign)    #存储数据
            print '注册完成，请登录！'.decode('utf-8')
            login()       
        else:
            print '密码不一致，请重新输入'.decode('utf-8')
            reg()
    else:
        print '请输入正确的注册信息'.decode('utf-8')
        reg()
        

def reg_txt(sign):
    '''存储注册信息'''
    na = open('sign.txt')
    zidian0 = p.load(na)
    sign.update(zidian0)
    f = file('sign.txt','w')   #追加失败
    p.dump(sign,f)
    f.close
def add_file(name):
    '''检查数据是否重复'''
    line = p.load(open('sign.txt'))
    if line.has_key(name):
        print '用户名已存在，请重新注册：'.decode('utf-8')
        reg()
    
def add_files(name,pwd):
    '''检查数据是否存在'''
    f = open('sign.txt')
    line = p.load(f)

    if line.has_key(name):
        if pwd == line[name]:
            return True
        else:
            print '密码错误'.decode('utf-8')
    else:
        print '用户名错误，请重新登录：'.decode('utf-8')
        no_login()

def __init__():
    '''初始化数据'''
    original = { 'admin' : 'admin' }
    f = open('sign.txt' , 'w')
    p.dump(original,f)
    f.close
    print '初始化中'.decode('utf-8'),
    for i in '.....':
        time.sleep(0.2)
        print i,
    print 
    time.sleep(1)
    print '初始化完成'.decode('utf-8')

def login():
    '''登录模块'''
    print '**登录账号**'.decode('utf-8')
    name = raw_input('请输入通行证：'.decode('utf-8'))
    pwd = raw_input('请输入密码：'.decode('utf-8'))
    if name and pwd:
        if add_files(name,pwd):
            print '登录中'.decode('utf-8'),
            for ii in '......':
                time.sleep(1)
                print ii,
            print 
            print '登录成功！'.decode('utf-8')
            time.sleep(2)
            print '*'*6,'Game Start!','*'*6
            time.sleep(2)
            start_game()
        else:
                print '密码错误，请输入正确的密码！'.decode('utf-8')
                login()
    else:
        print '请输入正确的用户名和密码！'.decode('utf-8')
        login()

def no_login():
    next= raw_input('请选择注册（R）/登录（L）？：'.decode('utf-8'))
    if next == 'R':
        reg()
    elif next == 'L':
        login()
    else:
        no_login()

def game(map):
    '''输出房间信息和方向'''
    print '='*10,map.name,'='*10
    for i in map.description.decode('utf-8'):  #打印房间的描述
        print i,
        time.sleep(0.1)
    print 
def gon(map):
    '''接受用户输入'''
    next = raw_input('你的选择是：'.decode('utf-8'))  #接受输入
    if map.paths.has_key(next):     #判断方向是否存在
        return next  
    else:
        print '请输入正确的方向！'.decode('utf-8')
        gon(map)
        
def start_game():
    game(start)#房间信息
    print start.scan()   #打印房间的方向选择
    next = gon(start)
    if start.go(next) == monster:
        monster_game()
    elif start.go(next) == lucky:
        lucky_game()
    else:
        start_game()

def monster_game():
    game(monster)
    monster_kill()
    print monster.scan()
    next = gon(monster)
    if monster.go(next) == start:
        start_game()
    elif monster.go(next) == lucky:
        lucky_game()
    else:
        monster_game()

def lucky_game():
    game(lucky)
    lucky_kill()
    print lucky.scan()
    next = gon(lucky)
    if lucky.go(next) == start:
        start_game()
    elif lucky.go(next) == monster:
        monster_game()
    elif lucky.go(next) == gold:
        gold_game()
    elif lucky.go(next) == dead:
        dead_game()
    else:
        lucky_game()
        
def gold_game():
    game(gold)
    gold_kill()

def dead_game():
    game(dead)
    print '不过，林哥还是给了你一次机会，你要好好把握！'.decode('utf-8')
    dead_kill()


key = False
number = 0
def monster_kill():
    global key
    global number
    print 
    for i in '提示：怪兽很凶猛，你随时都可能丧命，但是如果你能打倒它，可能得到钥匙，这把钥匙能开启特殊的宝箱'.decode('utf-8'):
        time.sleep(0.2)
        print i,
    print 
    next = raw_input('所以，你要怎么做？杀（K）还是闪（S）：'.decode('utf-8'))
    if super_sword:
        print '你拥有强大的神器，怪物不敢与你争斗，逃走了！'.decode('utf-8')
        time.sleep(1)
        print "你得到了 '黄金钥匙'!".decode('utf-8')
        number += 1    
        key = True
    else:
        if next == 'K':
            if sword:
                print '你有宝剑在手，成功的几率很高。'.decode('utf-8')
                print 
                print '战斗中'.decode('utf-8'),
                for ii in '...':
                    time.sleep(1)
                    print ii,
                print 
                i = random.randint(1,5)
                if i in (1,2,3,4):
                    print '你成功了，怪兽被你打死了!'.decode('utf-8')
                    if i in (2,3):
                        time.sleep(1)
                        print "恭喜你得到了'黄金钥匙'！".decode('utf-8')
                        key = True
                        number += 1
                else:
                    choose()       
            else:
                print 
                print '拳打脚踢中'.decode('utf-8'),
                for ii in '......':
                    time.sleep(1)
                    print ii,
                print 
                i = random.randint(1,5)
                if i in (2,3,4):
                    print '你成功了，怪兽被你打死了!'.decode('utf-8')
                    if i in (2,3):
                        print "恭喜你得到了'黄金钥匙'！".decode('utf-8')
                        number += 1
                        key = True
                else:
                    choose()
        elif next == 'S':
            i = random.randint(1,5)
            if i in (1,2,3):
                print '你没有溜掉，怪兽还是追上了你'.decode('utf-8')
                choose()
            else:
                print '你成功逃脱'.decode('utf-8')
        else:
            choose()
                
def choose():
        print 
        print '很不幸，你失败了，你太犹豫了，你缺乏生存智慧'.decode('utf-8')
        num = raw_input('重新来过，还是退出？（Y/N）：'.decode('utf-8'))
        if num == 'Y':
            monster_kill()
        elif num == 'N':
            print '你最后还是失败了...'.decode('utf-8')
            sys.exit()
        else:
            choose()


sword = False
def lucky_kill():
    global sword
    print 
    if sword:
        print '这里已经没有什么东西了，快去前往下个房间。'.decode('utf-8')
    else:
        print '你要寻找宝剑吗？'.decode('utf-8')
        next = raw_input('Y/N:')
        if next == 'Y':
            i = random.randint(1,6)
            if i in (1,2,3,4):
                print '恭喜你找到了宝剑！攻击力+5000！'.decode('utf-8')
                sword = True
            else:
                print '很不辛，你没有找到宝剑'.decode('utf-8')
        elif next == 'N':
            print '你直接绕过了沼泽，继续前进'.decode('utf-8')
        else:
            lucky_kill()

def gold_kill():
    print 
    for i in '提示：你必须杀了守卫，不然就是守卫杀了你，没有退路了！'.decode('utf-8'):
        time.sleep(0.3)
        print i,
    print 
    
    for i in [3,2,1]:
        time.sleep(1)
        print i 
    for i in '战斗开始！！！'.decode('utf-8'):
        time.sleep(0.5)
        print i,
    print 
    print '战斗中'.decode('utf-8'),
    for ii in '......':
        time.sleep(1)
        print ii,
    print 
    
    if sword:
        if super_sword:
            print '你有千年神器在手，守卫臣服了！'.decode('utf-8')
            print  '你带着黄金100000*%d,还有皇冠离开了！'.decode('utf-8') % number
            sys.exit()
        else:
            time.sleep(2)
            print '幸好你有宝剑在手，杀死守卫的成功率提高了'.decode('utf-8')
            print '刀光剑影中'.decode('utf-8'),
            for ii in '....':
                time.sleep(0.5)
                print ii,
            print 
            i = random.randint(1,6)
            time.sleep(2)
            if i in (1,2,3,4,5):
                print '你成功了，守卫被你杀死了，宝藏随你拿！'.decode('utf-8')
                key_d()
            else:
                print '很不辛，虽然你有宝剑，但是你毕了狗了，这都失败了！千古第一人也！'.decode('utf-8')
                restart()

    else:
         if super_sword:
            print '你有千年神器在手，守卫臣服了！'.decode('utf-8')
            print  '你带着黄金100000*%d,还有皇冠离开了！'.decode('utf-8') % number
            sys.exit()
         else:
            time.sleep(2)
            print '虽然没有宝剑，但是还是有可能杀死守卫的！'.decode('utf-8')
            print '你推我拉中'.decode('utf-8'),
            for ii in '......':
                time.sleep(0.5)
                print ii,
            print 
            i = random.randint(1,8)
            if i in (1,2,4,6):
                time.sleep(1)
                print 'Yes！好样的，没有宝剑也杀死了守卫，宝藏都是你的了！'.decode('utf-8')
                key_d()
            else:
                time.sleep(1)
                print '很不幸，你失败了，如果有宝剑的话，可能结果就不是这样了！'.decode('utf-8')
                restart()
             
def key_d():
    if key:
        time.sleep(0.8)
        print '你有黄金钥匙，太好了，你所能携带的宝藏+10000* %d！'.decode('utf-8') % number
        time.sleep(1)
        for i in '高兴之余，你突然诗兴大发，吟诗一首：'.decode('utf-8'):
            time.sleep(0.2)
            print i,
        print 
        time.sleep(0.4)
        poem()
        print
    else:
        time.sleep(0.8)
        print '你没有黄金钥匙，所以只能携带2000黄金离开！'.decode('utf-8')

super_sword = False     
sup_num = True   
def dead_kill():
    global super_sword
    global sup_num
    if sup_num:
        sup_num = False
        print 
        next = raw_input('你的选择是争取机会逃脱还是等死：Y/N：'.decode('utf-8'))
        if next == 'N':
            time.sleep(1)
            print '你太懦弱了，不适合当冒险家，你选择了死亡！'.decode('utf-8')
            sys.exit()
        elif next == 'Y':
            i = random.randint(1,5)
            if i == 2:
                time.sleep(1)
                print '你真是走狗屎运了，这都能成功。而且你还得到了一把千年神器，这是神的遗物！'.decode('utf-8')
                super_sword = True
                print "你被送回了'幸运之沼'！".decode('utf-8')
                time.sleep(1)
                lucky_game()
            else:
                print '我说过，没人能逃走的，你安息吧！'.decode('utf-8')
                restart()
        else:
            dead_kill()
    else:
        print '此地只能进入一次，快快离开！'.decode('utf-8')
        time.sleep(3)
        print "你被送回了'幸运之沼'！".decode('utf-8')
        time.sleep(1)
        lucky_game()
            
def START():
    printl('如果有账号请直接登录；如果没有，请先注册！')
    time.sleep(1)
    next = raw_input('请选择_登录（L）/注册（R）：'.decode('utf-8'))
    if next == 'L':
        login()
    elif next == 'R':
        reg()
    else:
        START()

def restart():
    print '想要重新来过吗？'.decode('utf-8')
    next = raw_input('是的话请按Y，否则请按N：'.decode('utf-8'))
    if next == 'Y':
        sup_num = True
        for i in "你轮回转世了，但是还惦记着宝藏，所以你又'执迷不悟'地前往那个地方！".decode('utf-8'):
            time.sleep(0.2)
            print i,
        print
        start_game()
    elif next == 'N':
        print '你最终选择了退出，再见！'.decode('utf-8')
        sys.exit()
    else:
        restart()

def poem():
    f = file('poem.txt','w')
    poem = '''不知天上宫阙，
    今夕是何年！'''
    f.write(poem)
    f.close
    
    f = file('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(0.6)
        for i in line.decode('utf-8'):
            time.sleep(0.4)
            print i,
def printl(str):
    print str.decode('utf-8')
START()