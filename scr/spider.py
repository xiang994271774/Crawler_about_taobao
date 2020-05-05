#!/usr/bin/env python

import requests
from pandas import DataFrame,Series
import pandas as pd
import json
import re
import os
try:
    os.mkdir('demo')
except:
    pass
url="https://s.taobao.com/search"    #链接
params={     #请求参数
    'data-key': 's',
    'data-value': '44',
    'ajax': 'true',
    'q': '猕猴桃',
    'commend': 'all',
    'ssid': 's5-e',
    'search_type': 'item',
    'sourceId': 'tb.index',
    'spm': 'a21bo.2017.201856-taobao-item.1',
    'ie': 'utf8',
    'initiative_id': 'tbindexz_20170306',
    'bcoffset': '1',
    'ntoffset': '7',
    'p4ppushleft': '2,48',
}
headers={    #头部信息
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    
    'referer':'https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20200504&stats_click=search_radio_all%3A1&js=1&imgfile=&q=%E7%8C%95%E7%8C%B4%E6%A1%83&suggest=history_2&_input_charset=utf-8&wq=&suggest_query=&source=suggest',
    
    'cookie':'cna=XulHFvKQUTYCAd9fB8A9iIRB; lgc=xiang994271774; tracknick=xiang994271774; enc=h42G%2Bvtgg%2FeSKbTcp%2BH22UsF5PcBeZiSjhIGeHN5PffEM0s1i9DylsAvdiSJQgF9YRLlJxCjaaZLxhrHsq8uHg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; t=a4ef1774e1fa59250bf3fdda9d2358fd; sgcookie=Ev9Ki1onixjVPULpeq7lo; uc3=lg2=UIHiLt3xD8xYTw%3D%3D&vt3=F8dBxGR02uFE1WalPGE%3D&id2=UojUASc%2Bmsfj3A%3D%3D&nk2=G4mgLUpqKDrsbcGZphw%3D; uc4=nk4=0%40GToWFgMgIVMBowEQy1Q9TqeP%2B3JT63kvKQ%3D%3D&id4=0%40UOBQhEzTNggG0pSnhq57sV9Gez5W; _cc_=URm48syIZQ%3D%3D; tfstk=cLWVB7i39-e4dJwR9KpwcU4keimAaqLMRY-ei6lKPLni_bRv8sxqW3qSW3-wJ8Ac.; mt=ci=-1_0; cookie2=120ef9248dc556aa9ca0ba62b5496d7b; v=0; _tb_token_=e0b83314edbe6; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _samesite_flag_=true; _m_h5_tk=ccd728b46f34aa45ac4c2ae9c91d72fb_1588491574538; _m_h5_tk_enc=9a2a7212e607be6c7cf7fed04b6ed2a4; JSESSIONID=FF5C307050E9FFCEDB2A740158BA7C9B; uc1=cookie14=UoTUMtULam%2FafQ%3D%3D; l=eBSupIEeQH4l3w9NBOfCFurza7797IRbouPzaNbMiT5PO7feczvOWZjn9WYwCnGVnsEJR354uljQBW8U-yUIh2nk8b8CgsDK0dTh.; isg=BLq60qsYsJpDnTyzBW8QR8JDC-Dcaz5FTx_6Y8Szcs0Nt1vxrPo_VRmBB0NrIbbd',
    
}

class Spider():
    def __init__(self):
        self.df=DataFrame()    #定义一个dataframe格式的变量
        self.columns=['标题','价格','地址','收货人数']   #属性
        for i in range(0,2000,44):
            print('*********    %s.      ******************'%i)
            params['data-value']=str(i)    #翻页处理
            self.get_info()    #爬信息
            self.df.to_excel('demo/淘宝数据.xlsx',index=False,columns=self.columns)    #保存数据
    def get_info(self):
        r=requests.get(url,headers=headers,params=params)    #请求数据
        js=json.loads(r.text)     #解析返回的json格式的数据
        for i in js['mods']['itemlist']['data']['auctions']:
            item_loc=i['item_loc'].split(' ')[0]     #地址
            try:
                view_sales=i['view_sales']    #付款人数
            except:
                continue
            raw_title=i['raw_title']    #标题
            price=i['view_price']    #价格
            data=[raw_title,price,item_loc,view_sales]
            
            ser=Series(data,index=self.columns)
            self.df=self.df.append(ser,ignore_index=True)      #把数据添加到变量self.df中
        
            
            
            
            
            
if __name__=="__main__":
    Spider()
