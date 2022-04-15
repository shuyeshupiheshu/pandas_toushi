import pandas as pd
import numpy as np
from date_deal import add_up
from datetime import datetime


filname = 'LF12-3 焊口信息汇总表.xlsx'
df = pd.read_excel(filname)
#df['VT Date'] = pd.to_datetime(df['VT Date'])
df.index= df['VT Date']
df['Week num']=df.index.week
df['year']= df.index.year
df['month'] = df.index.month
df['Week num'] = df['Week num'].apply(lambda x:int(x) if not (pd.isna(x)) else x)

#df['year'] =df['VT Date'].apply(lambda x :x.year() if not(pd.isna(x)) else x)

df['num'] = df['Week num']+df['year']*52

print(df['num'].max()/52)
#print(df['num'].max)
df.to_excel('1.xlsx')

