#!/usr/bin/env python

#地图数据
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
df=pd.read_excel('demo/data.xlsx')    #读取数据
plt.rcParams['font.sans-serif']=['simhei']   #设置字体
ser=df['地址'].value_counts()     #统计不同地址的数量
locs=ser.index.tolist()
fig=plt.figure(figsize=(15,10))    #改变画布大小
ax=fig.add_subplot(1,1,1)
m=Basemap(projection='mill',llcrnrlat=15,llcrnrlon=70,urcrnrlon=135,urcrnrlat=55)
C2E={'Shanghai':"上海",'Shaanxi':"陕西",'Sichuan':"四川",'Guangdong':"广东",'Zhejiang':"浙江",'Henan':"河南",'Beijing':"北京",'Jiangsu':"江苏",
         'Shandong':"山东",'Guangxi':"广西",'Liaoning':"辽宁",'Anhui':"安徽",'Hunan':"湖南",'Yunnan':"云南",'Fujian':"福建",'Guizhou':"贵州",'Chongqing':"重庆",
         'Hubei':"湖北",'Jiangxi':"江西",'Hebei':"河北",'Shanxi':"山西",'Heilongjiang':"黑龙江",'Tianjin':"天津",'Hainan':"海南",'Xinjiang Uygur':"新疆",'Nei Mongol':"内蒙古",'Jilin':"吉林",
         'Gansu':"甘肃",'Xizang':"西藏",'Qinghai':"青海",'Xianggang':"香港"}
data={'Shanghai':0,'Shanxi':0,'Sichuan':0,'Guangdong':200,'Zhejiang':0,'Henan':112,'Beijing':92,'Jiangsu':68,
         'Shandong':64,'Guangxi':42,'Liaoning':0,'Anhui':26,'Hunan':24,'Yunnan':19,'Fujian':18,'Guizhou':16,'Chongqing':14,
         'Hubei':13,'Jiangxi':12,'Hebei':11,'Shaanxi':10,'Heilongjiang':8,'Tianjin':5,'Hainan':5,'Xinjiang Uygur':3,'Nei Mongol':3,'Jilin':3,
         'Gansu':1,'Xizang':1,'Qinghai':1,'Xianggang':1}

for i in data: #循环遍历data
    if not C2E[i] in locs:# 地名不在locs里面就跳过
        continue
    data[i]=ser[C2E[i]] #改变data的数据

m.readshapefile('help/gadm36_CHN_shp/gadm36_CHN_1','china',linewidth=2)    #读取省份数据
for info,shap in zip(m.china_info,m.china):
    proid=info['NAME_1']
    if proid in data:
        poly=Polygon(shap,facecolor='yellow',edgecolor='c',alpha=data[proid]/ser.tolist()[0])     #给省份添加颜色
        ax.add_patch(poly)
m.readshapefile('help/gadm36_TWN_shp/gadm36_TWN_1','tw',linewidth=2)    #读取台湾的数据

plt.title('不 同 地 区 分 布 情 况')    #设置标题
plt.savefig('demo/地图.png',dpi=400)    #保存表格
