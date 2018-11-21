
import  time
# time.struct_time 结构体
time1 = time.localtime()
print(time)
# 从1970年到现在的秒数  1531274999.5757902
time2 = time.time()
print(time2)
# 从1970年开始往后指定的秒数
time3 = time .localtime(1531134000)
print(time3)
# 时 分 秒 字母大写
result = time.strftime('%y %m %d %H %M %S',time.localtime())
print(result)
# 线程休眠（秒）
# 爬虫：获取对方数据太快有可能被地方认为时爬虫程序 所以在爬虫中有事需要减缓速度
# 线程：a代码块的执行受b代码的执行 必须确保B代码的执行 这时候就可以让A代码休眠一段时间
#       (注意：休眠不是必须的 也不是最好的)
# 定时任务：需要代码到指定时间时 去执行某个任务 当时间还未到达 可以让程序先休眠
# time.sleep(5)
print('今天是周三， 一星期马上过去一半了')
# data:数据
# date 日期
# import datetime
# date1 = datetime.datetime.now():
# print(date1)
# date2 = datel.strftime('%y %m %d %H: %M: %S')
# print(date2)
#
# date2 = date1.strftime('%y year %m month %d day %H hour %M minute %S second')
# print(date2)
# date2 = date1.strftime('%y年%m月%d日')

# 编码错误：本地文件不能对指定位置的字符进行编码
# date2 = date2.replace('year','年').replace('month','月').replace('day','日')
# print(date2)

# 怎么获取今天往后推一天的时间
# 可以用来计算过期时间
# timedelta: 推迟
date4 = datetime.timedelta(days= 1 ,hours=12)
date5 = datetime.datetime.now() + date4
print(date5)

date6 = datetime.datetime.now()
# TypeError: Required argument 'year' (pos 1) not found
date7 = date6.date()
print(date7.year , date7.day , date7.month)

date8 = date6.time()
print(date8)

date9 = datetime.datetime.now()
# stamp 邮戳
# timestapm 时间戳 时间线
print(date9.timestamp())