# os :operation system
# mac os 苹果电脑
# ios  iphong os
# os 模块获取电脑的相关信息
# 并且有很强大的文件及文件夹操作功能
# 所以在操作文件或者文件夹的时候
# 首先要引入os模块
import  os
# 获取cpu核数
cpu_count = os.cpu_count()
print(cpu_count)

#  os可以获取本机的基本信息以及
# 可以对文件以及文件夹进行相关操作

name = os.name
# nt 代表windows操作系统
# posix代表linux操作系统
print(name)

# 判断是否存在某个文件
# path :路径 exists： 存在
# 如果不写路径地址 直接写文件名字
# 那么默认使用的是 相对路径
# -----------------------------文件夹操作------------------------------------------
# 绝对路径
result = os.path.exists('C:/Users/Administrator/Desktop/pythe 9/python/7/11/测试.txt')
print(result)
# 获取jueduilujing
result = os.getcwd()
print(result)

# abs absolute 绝对的
result = os.path.abspath('.')
print(result)
# 获取当前路径的父级路径
result = os. path.abspath('..')
print(result)
# 获取整个地址当中的最后一部分 basename
result = os.path.basename('http://www.baidu.com/music/perttyboy.mp3')
print(result)

result = os.path.basename('c:/user/a/Desktop/python 9/python/11/os操作.py')
print(result)

# 地址路径会被//分割成几部分  common 公共的  获取路径相同的部分
result = os.path.commonpath(['http://www.jd.com',
                             'http://www.taobao.com',
                             'http://www.baidu.com'])
print(result)


# 返回文件所在的文件夹
# 文档：返回一个文件夹共有的路径   direction name 获取指定文件所在的文件夹路径
result =os.path.dirname('c:/user/a/desktop/python 9/python/11/测试.txt')
print(result)

# 获取文件夹 信息-------------------------
# 文件夹信息包括 创建日期 修改日期 访问日期
#----------------------------------- 文件及信息处理-----------------------------
import  time
# get得到
# c 文档是：change  实际是：create
# 获取文件夹的创建时间
result = os.path.getctime('C:/Users/Administrator/Desktop/pythe 9/python/11')
print(time.localtime(result))
# a  : access:访问时间
result = os.path.getatime('C:/Users/Administrator/Desktop/pythe 9/python/11')
print(time.localtime(result))
# m : modify :修改、
result = os.path.getmtime('C:/Users/Administrator/Desktop/pythe 9/python/11')
print(time.localtime(result))
# size : 尺寸 大小 获取文件大小 （获取的大小为 字节大小   B）
# 1M = 1024KB kilo million
# 1KB =  1024B byte
# 1B =8b bit
result = os.path.getsize('C:/Users/Administrator/Desktop/pythe 9/python/11')
print(result / 1024)

# is 是否  isFile 判断是否为文件   isdigit 判断是否为数字
result = os.path.isfile('C:/Users/Administrator/Desktop/pythe 9/python/11')
print(result)
# -----------------------------文件分割操作----------------------------------------------
# split 分割
# 返回一个元祖 有路径和最后的文件名两部分组成
result = os.path.split('C:/Users/Administrator/Desktop/pythe 9/python/11')
print(result)


# splitext 返回一个元祖 有全部路径和最后的文件后缀两部分组成
result = os.path.splitext('C:/Users/Administrator/Desktop/pythe 9/python/11')
print(result)

# 文件增删改操作-----------------------、
# FileNotFoundError: [WinError 2] 系统找不到指定的文件。: '测试.txt' -> '发布.txt'
# 文件存在错误
# mkdir  : make  directory
# os.mkdir('python')

if os.path.exists('python'):
    pass
else:
    os.mkdir('python')
# 修改文件名字
# os.rename('测试.txt','发布.txt')

#------------------------------------- 文件读写操作-----------------------------
# 值1.写入的文件 如果有这个文件就直接写入  如果咩有这个文件就创建
# 值2. 对文件的操作方式 w 表示 write 写入
# 值3.文件的编码方式 utf-8防止乱码出现
# 写完后\n是换行  会对原内容覆盖掉
f = open('发布.txt','w',encoding='utf-8')
f.write('今天是周三 7月11日，距离毕业还有120天\n')
# # 当文件关闭以后不能对文件进行任何操作
f.write('明天是周四，后天是周五，大后天自习，然后休息\n')
f.close()
# append 追加
f = open('发布.txt','a',encoding='utf-8')
f.write('新来的内容----------------------')
f.close()

# r read
f = open('发布.txt','r',encoding='utf-8')
# readlines将所有的数据放入到一个数组当中
# f.read 将所有数据放入一个字符串当中
result = f.readlines()
print(result)
f.close()

#1. 小练习
# 创建一个文件，在里面存放10000个10位随机验证码
# import  random
# str = 'qwertyuiopASDFGHJKLZXCVBNM1234567890'
#
# # f = open('random.txt','w',encoding='utf-8')
# with open('random.txt','w',encoding='utf-8')as f:
#     for index in range(10000):
#         content = ''
#         for x in range(10):
# random.choice 如果对象是一个列表，元祖或字符串的时候
# 、从这个对象当中随机取出一块
#             char_str = random.choice(str)
#             content += char_str
#         f.write(content + '\n')
# f.close()
#
# with open('random1.txt','w',encoding='utf-8')as f :
#     for index in range(20):
#         content = ''
#         for x in range(10):
#             char_str = str[random.randint(0,len(str)-1)]
#             content += char_str
#         f.write(content + '\n')
# f.close()

# 3.小练习
# 获取练习中的文件，然后判断每隔验证码中数字出现的次数总和
# f = open('random1.txt','r',encoding='utf-8')
# str = f.readlines()
# for n in range(20):
#     # print(str[n])
#     str1 = str[n]
#     num = 0
#     for i in range(10):
#         txt = str[i]
#         if txt.isdigit():
#             num += 1
#     print(num)

# 4.小练习
# 统计：所有验证码中每一个数字出现的次数总和

# f = open('random1.txt','r')
# list1 = f.readlines()
# count0 = count1 = count2 = count3 = count4 = count5 = count6 = count7 = count8 =count9 =0
# for x in list1:
#     for y in x:
#         if y.isdigit():
#             z = int(y)
#             if z == 0:
#                 count0 += 1
#             elif z == 1:
#                 count1 += 1
#             elif z == 2:
#                 count2 += 1
#             elif z == 3:
#                 count3 += 1
#             elif z == 4:
#                 count4 += 1
#             elif z == 5:
#                 count5 += 1
#             elif z == 6:
#                 count6 += 1
#             elif z == 7:
#                 count7 += 1
#             elif z == 8:
#                 count8 += 1
#             elif z == 9:
#                 count9 += 1
#         else:
#             pass
# print(count0 ,count1 ,count2 ,count3 ,count4 ,count5 ,count6 ,count7 ,count8 ,count9 )
# f.close()

# 小程序
# 1.随意输入一个输入 如果是1 创建一个文件夹名字为test_one
# 2.如果是2 删除一个文件夹 名字是 test_one
# 3.如果是其他数字 返回

# while 后面需要跟一个判断条件
#     条件为真的情况下 会一直执行
#     直到条件为假 或者跳出循环
#
# while False:
#     num = input('请输入一个数字')
#     num = int(num)
#     if num ==1:
#         if os.path.exists('test_one'):
#             pass
#         else:
#             os.mkdir('test_one')
#     elif num ==2:
#         if os.path.exists('test_one'):
#             os.removedirs('test_one')
#         else:
#             pass
#     else:
#         break

# print('{}'.format(os.path.abspath('.')))
# print('{}'.format(os.getcwd()))
# change 改变 改变当前所在的目录
# os.chdir('test')
# 获取路径 获取当前路径的父路径
# os.path.abspath('...')
# 改变路径到指定的 路径下 pardir  directory parent
# os.chdir(os.path.pardir)
# print('{}'.format(os.getcwd()))
# os.removedirs('testA')

# 小练习:
# 创建一个文件 名字为code.txt 在里面存放10000个6位随机数字的验证码

# 防止中文乱码
# w : write 写入内容
# 写入的时候 会将之前的内容清除掉

import  random
f = open('code.txt','w',encoding='utf-8')
for x in range(10000):
   num = random.randint(0,999999)
   num = '%.6d'%num
f.write(num +'\n')

f.close()