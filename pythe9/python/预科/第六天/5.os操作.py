# operation system 操作系统
# os模块获取电脑的相关信息
# 并且有很强大的文件及文件夹操作能力
# 所以在操作文件或者文件夹的时候
# 首先要引入os模块
import os
# 获取电脑cpu个数
cpuCount = os.cpu_count()
print(cpuCount)

name = os.name
# nt代表windows操作系统 linux为posix
print('操作系统的名字是:{}'.format(name))

# exists存在 path路径
# 相对路径
result = os.path.exists('1.homework.py')
if result :
    print('存在')
else :
    print('不存在')

print(result)

# C:\Users\a\Desktop\os测试
# C:/Users/a/Desktop/os测试
result = os.path.exists('C:/Users/a/Desktop/os测试/python.txt')
print(result)