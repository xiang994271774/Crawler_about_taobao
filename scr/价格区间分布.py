#!/usr/bin/env python

#销量区间分布
import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_excel('demo/data.xlsx')

ages=[0,10,20,30,40,50,100,200,300,400,500,1000]
ser=pd.cut(df['价格'],ages)
ser=ser.value_counts().sort_index(ascending=True)
names=ser.index.tolist()
x=list(range(len(names)))
y=ser.tolist()
plt.rcParams['font.sans-serif']=['simhei']
plt.figure(figsize=(14,8))
plt.bar(x,y,tick_label=names)
plt.xticks(rotation=90)
for i in x:
    plt.text(x[i],y[i],y[i])
plt.xlabel('价 格',fontsize=16)
plt.ylabel('价 格 区 间',fontsize=16)
plt.title('价 格 区 间 分 布',fontsize=16)
plt.savefig('demo/价格区间分布.png',dpi=400)
