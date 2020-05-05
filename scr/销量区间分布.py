#!/usr/bin/env python

#销量区间分布
import pandas as pd
from matplotlib import pyplot as plt
df=pd.read_excel('demo/data.xlsx')

ages=[0,20,50,100,1000,2000,4000,6000,8000,10000,12000,14000,16000]
ser=pd.cut(df['收货人数'],ages)
ser=ser.value_counts().sort_index(ascending=True)
names=ser.index.tolist()
x=list(range(len(names)))
y=ser.tolist()
plt.rcParams['font.sans-serif']=['simhei']
plt.figure(figsize=(19,8))
plt.bar(x,y,tick_label=names)
plt.xticks(rotation=90)
data=[sum(y[:i]) for i in range(1,len(y)+1)]
plt.plot(x,data,color='red')
for i in x:
    plt.text(x[i],y[i],y[i])
plt.xlabel('数 量',fontsize=16)
plt.ylabel('销 量 区 间',fontsize=16)
plt.title('销 量 区 间 分 布',fontsize=16)
plt.savefig('demo/销量区间分布.png',dpi=400)
