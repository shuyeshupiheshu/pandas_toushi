import pandas as pd
import numpy as np
import split
import matplotlib.pyplot as plt
from date_deal import create_assist_date,timeforce
from datetime import datetime
import numpy as np

def inspector_daily(filname,window,start_date,end_date):
    color_bar = ['red','green','blue','yellow','aliceblue','aquamarine','blanchedalmond','brown','coral']
    df = pd.read_excel(filname)

    df = df[df['VT Date'].between(start_date,end_date)]


    Inspector = df.groupby(['VT Date','Inspector'],as_index = False).agg({'Length':'sum'})
    
    #建立x_label索引表
    x_label = create_assist_date(start_date,end_date)
    x_dist = {}
    x_value = []
    j = 1
    for i in x_label:
         x_dist[i] = j
         j = j+1

    name = Inspector.drop_duplicates('Inspector')

    name = np.array(name['Inspector'])
    for i in range(0,len(name)):
    #变量@
        name_i = name[i]
        x_In = Inspector.query("Inspector.str.contains(@name_i)")
        for i in x_In:

            #问题点
            i = timeforce(i)
            x_value.append(x_dist[i])
        y_value = x_In['VT Report No']
        if i == 0:
           a = window.bar(x_value,y_value,width=0.1,color = color_bar[i])
        else:
            if i%2 ==1:
                x_value = x_value-((i+1)/2*0.1)
            else:
                
                x_value = x_value+(i/2)*0.1
            a = window.bar(x_value,y_value,width=0.1,color = color_bar[i])
    #xlabel调整
        window.bar_label(a,label_type = 'edge')
    window.legend(name,fontsize = 7)
    plt.xticks(range(0,len(x_label),1),x_label)
    return Inspector

def pip_drawing(filname,start_date,end_date):
    
    df = pd.read_excel(filname)
    df['VT Date'] = pd.to_datetime(df['VT Date'])
    df = df[df['VT Date'].between(start_date,end_date)]
    return(df['VT Date'].sum())
