
# date  data
# 日期  数据
import datetime
# 获取今天的时间
date1 = datetime.datetime.today()
print(date1)
# 获取现在的时间  2018-07-02 11:05:33.268490
date2 = datetime.datetime.now()
print(date2)
# %y 获取年  %m获取月  %d 获取日
# strftime 不能进行中文编码
date3 = date2.strftime('%yyear%mmonth%dday')
# 但是可以将得到的结果进行转换
print(date3.replace('year','年').
      replace('month','月').replace('day','日'))
# 设置时间间隔
date4 = datetime.timedelta(hours=12 ,minutes= 30)
print(date4)
# 从现在往后 推迟指定的时间
date5 = datetime.datetime.now() + date4
print(date5)

date5=  datetime.datetime.today()
# 只获取当前的日期
date6 = date5.date()
print('-----------------------------')
print(date6)
print('{}年{}月{}日'.format(date6.year ,date6.month ,date6.day))
# 只获取当前的时间
date7 = date5.time()
print(date7)
print('{}时{}分{}秒'.format(date7.hour ,date7.minute ,date7.second))
# 获取当前时间戳
print('当前的时间戳为{}'.format(date5.timestamp()))



