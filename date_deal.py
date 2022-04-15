import pandas as pd
import split
import matplotlib.pyplot as plt
from datetime import datetime , timedelta
def create_assist_date(datestart = None,dateend = None):
# 创建日期辅助表
	if datestart is None:
	    datestart = '2016-01-01'
	if dateend is None:
		dateend = datetime.now().strftime('%Y-%m-%d')

	# 转为日期格式
	datestart=datetime.strptime(datestart,'%Y-%m-%d')
	dateend=datetime.strptime(dateend,'%Y-%m-%d')
	date_list = []
	date_list.append(datestart.strftime('%Y-%m-%d'))
	while datestart<dateend:
		# 日期叠加一天
	    datestart+=timedelta(days=+1)
	    # 日期转字符串存入列表
	    date_list.append(datestart.strftime('%Y-%m-%d'))
	return date_list

def timeforce(time):
	#date_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
	date_time_2 = datetime.strftime(time, '%Y-%m-%d')
	return date_time_2

def create_assist_weak(datestart = None,dateend = None):
# 创建日期辅助表
	if datestart is None:
	    datestart = '2016-01-01'
	if dateend is None:
		dateend = datetime.now().strftime('%Y-%m-%d')

	# 转为日期格式
	#datestart=datetime.strptime(datestart,'%Y-%m-%d')
	#dateend=datetime.strptime(dateend,'%Y-%m-%d')
	date_list = []
	date_list.append(datestart.strftime('%Y-%m-%d'))
	while datestart<dateend:
		# 日期叠加一天
	    datestart+=timedelta(days=+7)
	    # 日期转字符串存入列表
	    date_list.append(datestart.strftime('%Y-%m-%d'))
	return date_list

def get_week(year,num):
    #year year-%y-%d
    year = datetime(year,1,1)
    year.strftime('%Y-%m-%d')
    #日期偏移
    week = year + timedelta(days=+7*num)
    week = week.strftime('%Y-%m-%d')
    return week
