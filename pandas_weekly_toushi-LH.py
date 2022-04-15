import pandas as pd
import numpy as np
import split
import matplotlib.pyplot as plt
from date_deal import get_week
from datetime import datetime
import numpy as np


color_bar = ['red','green','blue','yellow','aliceblue','aquamarine','blanchedalmond','brown','coral']

#数据表引入
df_EP = pd.read_excel("EP20-4 焊接信息汇总表.xlsx")

#解析第5周对应的实际日期

df_EP['VT Date'] = pd.to_datetime(df_EP['VT Date'])
min_date = df_EP['VT Date'].min()
year =int(min_date.strftime('%Y'))
df_EP.index= df_EP['VT Date']
df_EP.index=df_EP.index.week
df_EP['Week num'] = df_EP.index
max_x =int(df_EP['Week num'].max().squeeze())


x = range(max_x-4,max_x+1,1)
x_label = []
#GET_WEEK TIAOZHENG
x_label.append('0')
for i in x:
    week = get_week(year,i)
    
    x_label.append(get_week(year,i))


#df_EP.to_excel("test.xlsx")



Inspector_ep = df_EP.groupby(['Week num','Inspector'],as_index = False).agg({'VT Report No':'count'})

#选取近5周
Inspector_ep = Inspector_ep[Inspector_ep['Week num']>(max_x-5)]


Inspector_ep.to_excel("fenxi.xlsx")

name = Inspector_ep.drop_duplicates('Inspector')

name = np.array(name['Inspector'])

#绘图
plt.figure(num = 1,figsize=(18,8),dpi = None,edgecolor='blue',frameon= True)
plt.subplot(221)

for i in range(0,len(name)):
    #变量@
    name_i = name[i]
    x_In = Inspector_ep.query("Inspector.str.contains(@name_i)")
    x_value =np.array(x_In['Week num'])
    y_value = np.array(x_In['VT Report No'])
    if i == 0:
       a = plt.bar((x_value-max_x+5),y_value,width=0.1,color = color_bar[i])
    else:
        if i%2 ==1:
            x_value = x_value-((i+1)/2*0.1)
        else:
            print(i)
            x_value = x_value+(i/2)*0.1
        a = plt.bar((x_value-max_x+5),y_value,width=0.1,color = color_bar[i])
    #print(name_i)
    #xlabel调整
    plt.bar_label(a,label_type = 'edge')
plt.legend(name,fontsize = 7)

#xlabel调整
#plt.bar_label(a,label_type = 'edge')
plt.xticks(range(0,6,1),x_label)


plt.show()

