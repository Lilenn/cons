
# 引入时间包
import time
time_line = time.time()
# 获取从1970年到现在的秒数
# 32位计算机   64年    64位计算机
# 1970年操作系统出现
print(time_line)

# time.struct_time  struct 结构体
# 0 周日  1 -6 周一到周六 js
# 0 周一  6 周日
# 获取当前的时间 local本地
time1 = time.localtime()
print(time1)
# 获取从1970年开始往后指定的秒数所对应的时间
time2 = time.localtime(1530400000)
print(time2)
# access_token
# 系统桌面判断登录过期 ？

# 设置自定义时间 2018-07-02  12:12:12
# y  year m month d day H hours M minute S second
time4 = time.strftime('%y-%m-%d %H:%M:%S',time.localtime())
print(time4)

while True :
    # 获取当前时间
    time5 = time.localtime()
    print('检测')
    if time5.tm_year == 2018 and time5.tm_mon == 8 and time5.tm_mday == 2 and time5.tm_hour == 10 :
        print('发送邮件')
        break
    # 线程休眠  sleep 睡觉

    time.sleep(1)