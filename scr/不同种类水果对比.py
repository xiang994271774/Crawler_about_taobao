#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 06:57:48 2020

@author: xiang994271774
"""
#
#统计水果
import pandas as pd
from matplotlib import pyplot as plt
from pandas import Series
df=pd.read_excel('demo/水果.xlsx')
names=df['标题'].tolist()
#绿心、红心、黄心、
signs={'西瓜':0,'香蕉':0,'葡萄':0,'苹果':0,'猕猴桃':0,'其他':0,
       '梨':0,"枇杷":0,"芒果":0,"菠萝":0,"橘":0,"火龙果":0,"柚":0,"橙":0,"水蜜桃":0,"荔枝":0,"柠檬":0,"榴莲":0,"杨梅":0}
for i in names:
    s=0
    for j in signs:
        if j in i:
            signs[j]=signs[j]+1
            s=1
    if s==0:
        signs['其他']=signs['其他']+1
ser=Series(signs)
names=ser.index.tolist()
y=ser.tolist()
x=list(range(len(y)))
plt.rcParams['font.sans-serif']=['simhei']
plt.figure(figsize=(12,12))
p,L_text,p_text=plt.pie(y,labels=names,autopct='%0.2f%%')
plt.title('不 同 种 类 水 果 对 比',fontsize=18)
for i,j in zip(L_text,p_text):
    i.set_size(16)
    j.set_size(12)
plt.savefig('demo/不同种类水果对比.png',dpi=400)
