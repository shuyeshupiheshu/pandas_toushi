from inspector import inspector_daily,pip_drawing
import matplotlib.pyplot as plt
filename1 = 'EP20-4 焊接信息汇总表.xlsx'
filename2 ='LF12-3 焊口信息汇总表.xlsx'
filename3 ='LH11-1焊口信息汇总表.xlsx'

start_date = '2022-4-1'
end_date = '2022-4-10'


plt.figure(num = 1,figsize=(18,8),dpi = None,edgecolor='blue',frameon= True)
window = plt.subplot(221)
total1 = inspector_daily(filename1,window,start_date,end_date)

window = plt.subplot(223)
total2 = inspector_daily(filename2,window,start_date,end_date)


window = plt.subplot(224)
total3 = inspector_daily(filename3,window,start_date,end_date)

window = plt.subplot(222)
A = []
ep = pip_drawing(filename1,start_date,end_date) 
A.append(ep)
lf12 = pip_drawing(filename2,start_date,end_date)
A.append(lf12)
lh = pip_drawing(filename3,start_date,end_date)
A.append(lh)
plt.pie(A)
window.legend(['EP','LF12-3','LH'],fontsize = 7)
plt.show()


