# calendar 日历
# 引入 日历包
import  calendar
# time1 = time.time()
# date1 = datetime.datetime.today()
# date2 = datetime.datetime.now()
calen = calendar.Calendar()
print(calen)

# iterable 可迭代的 for  产品版本迭代
ca1 = calen.iterweekdays()
# 迭代指定的月份   0表示非本月日期
ca1 = calen.itermonthdays(year=2018 ,month=7)
# 迭代指定的月份 获取的元组对象有两个字值

# 值1：是否属于本月 0表示非本月
# 值2：日子对应的星期   0是周一  6是周日
ca1 = calen.itermonthdays2(year=2018 ,month= 7)
# 迭代指定月份的日历 格式为yyyy-mm-dd
ca1 = calen.itermonthdates(year=2018 , month=7)
print(ca1)
for x in ca1 :
    print(x)

# 获取文本日历
calen = calendar.TextCalendar()
# 给文本日历指定月份
calen.prmonth(theyear=2018,themonth=7)
print(calen)
calen.pryear(theyear=2018)
print(calen)

