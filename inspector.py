import pandas as pd
import numpy as np
import split
import matplotlib.pyplot as plt
from date_deal import get_week
from datetime import datetime
import numpy as np

def inspector_daily(filname,window,start_date,end_date):
    color_bar = ['red','green','blue','yellow','aliceblue','aquamarine','blanchedalmond','brown','coral']
    df = pd.read_excel(filname)
    df['VT Date'] = pd.to_datetime(df['VT Date'])
    df = df[df['VT Date'].between(start_date,end_date)]
    min_date = df['VT Date'].min()
    year =int(min_date.strftime('%Y'))
    df.index= df['VT Date']
    df.index=df.index.week
    df['Week num'] = df.index
    
    max_x =int(df['Week num'].max().squeeze())


    x = range(max_x-4,max_x+1,1)
    x_label = []
#GET_WEEK TIAOZHENG
    x_label.append('0')
    for i in x:
        week = get_week(year,i)
    
        x_label.append(get_week(year,i))


#df_EP.to_excel("test.xlsx")



    Inspector = df.groupby(['Week num','Inspector'],as_index = False).agg({'VT Report No':'count'})

#选取近5周
    Inspector = Inspector[Inspector['Week num']>(max_x-5)]


    #Inspector.to_excel("fenxi.xlsx")

    name = Inspector.drop_duplicates('Inspector')

    name = np.array(name['Inspector'])
    for i in range(0,len(name)):
    #变量@
        name_i = name[i]
        x_In = Inspector.query("Inspector.str.contains(@name_i)")
        x_value =np.array(x_In['Week num'])
        y_value = np.array(x_In['VT Report No'])
        if i == 0:
           a = window.bar((x_value-max_x+5),y_value,width=0.1,color = color_bar[i])
        else:
            if i%2 ==1:
                x_value = x_value-((i+1)/2*0.1)
            else:
                
                x_value = x_value+(i/2)*0.1
            a = window.bar((x_value-max_x+5),y_value,width=0.1,color = color_bar[i])
    #print(name_i)
    #xlabel调整
        window.bar_label(a,label_type = 'edge')
    window.legend(name,fontsize = 7)
    plt.xticks(range(0,6,1),x_label)
    return Inspector

def pip_drawing(filname,start_date,end_date):
    
    df = pd.read_excel(filname)
    df['VT Date'] = pd.to_datetime(df['VT Date'])
    df = df[df['VT Date'].between(start_date,end_date)]
    return(df['VT Date'].count())
