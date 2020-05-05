#!/usr/bin/env python

#横向对比
import pandas as pd
from matplotlib import pyplot as plt
from pandas import Series
df=pd.read_excel('demo/data.xlsx')     #读取数据
names=df['标题'].tolist()    #把标题读取出来作为列表格式
#绿心、红心、黄心、
signs={'绿心':0,'红心':0,'黄心':0,'其他':0}
for i in names:
    name='其他'
    if '绿心' in i:
        name='绿心'
    elif '红心' in i:
        name='红心'
    elif '黄心' in i:
        name='黄心'
    signs[name]=signs[name]+1
ser=Series(signs)     #把signs格式转换成series格式
names=ser.index.tolist()     #属性列表
y=ser.tolist()
x=list(range(len(y)))
plt.rcParams['font.sans-serif']=['simhei']      #改变字体
plt.figure(figsize=(12,12))    #定义面板大小
p,L_text,p_text=plt.pie(y,labels=names,autopct='%0.2f%%')     #绘制饼图
plt.title('不 同 种 类 猕 猴 桃 对 比',fontsize=18)    #设置标题
for i,j in zip(L_text,p_text):
    i.set_size(16)      #设置字体大小
    j.set_size(16)      #设置百分占比字体大小
plt.savefig('demo/不同种类猕猴桃对比.png',dpi=400)    #保存数据
