#!/usr/bin/env python

#数据清洗
import pandas as pd
import re
df=pd.read_excel('demo/淘宝数据.xlsx')
df['价格']=df['价格'].astype('float')
wan=df[df['收货人数'].str.findall('万').str.len()>0].index
df['收货人数']=df['收货人数'].str.replace('[人付款+万]','').astype('float')
df['收货人数'].iloc[wan.tolist(),]=df['收货人数'].iloc[wan.tolist(),]*1000
df.to_excel('demo/data.xlsx',index=False)
