# 声明方法1
# 创建一个txt文件，里面存放1000条数据，每条数据长度为10 ，包含大小写字母和数字
# import random
# str = 'qwertyuiopASDFGHJKL1234567890'
# def getRandom():
#     with open('random.txt','w') as f:
#         for index in range(1000):
#             content = ''
#             for x in range(10):
#                 char = random.choice(str)
#                 content += char
#             f.write(content + '\n')
#     f.close()
# getRandom()
# 声明方法2
# 读取txt文件里面的所有数据，如果该条数据只有数字，那么创建一个txt文件 保存起来
def readAllInfo():
    list = []
    with open('random.txt','r') as f:
        for line in f.readlines():
            line = line[0:-1]
            list.append(line)
    f.close()
    return  list
  # 获取所有数据当中全部为数字的数据
def getAllInfo():
    list = readAllInfo()
    with open('num.txt','w')as f:
        for value in list :
            if value.isdigit():
                f.write(value +'\n')
    f.close()

getAllInfo()


 # 声明方法3
# 读取txt文件里面的所有数据 如果该条数据只有字母 那么创建一个txt文件 保存起来

# 第一种 用系统方式
# def getAllCharInfo():
#     list = readAllInfo()
#     with open('char.txt', 'w')as f:
#         for value in list:
# 判断是否为字母 :isalpha  判断是否为数字 ： isdigit
#             if value.isalpha():
#                 f.write(value + '\n')
#     f.close()
# getAllCharInfo()
# 第二种方式： 用ASCII
#   65-90  A-Z
# 97-122  a-z
# def getAllCharInfo():
#    list = readAllInfo()
#    with open('char1.txt','w')as f :
#         for value in list:
#           count = 0
#           for char in value:
#              if (ord(char) >=65 and ord(char) <=90  or ord(char) >=97 and ord(char) <=122):
#                     count +=1
#
#           if count ==10 :
#             f.write(value + '\n')
#    f.close()
# getAllCharInfo()
# 第三种方式
# def getAllCharInfo():
#     list = readAllInfo()
#     with open('char3.txt','w') as f:
#         for value in list:
#             isAllChar = True
#             for char in value:
#                 if char.isdigit():
#                     isAllChar = False
#                     break
#             if isAllChar == True:
#                 f.write(value + '\n')
#         f.close()
# getAllCharInfo()

# 声明方法4
# 读取txt文件里面的所有数据 如果该条数据包含数字和字母 那么创建一个txt文件 保存起来

# def getAllNumWithCharInfo():
#     list = readAllInfo()
#     with open('numwithchar.txt','w') as f:
#         for value in list:
#             isHasNum = False
#             isHasChar = False
#             for char in value:
#                 if char.isdigit():
#                     isHasNum = True
#                 else:
#                     isHasChar = True
#             if isHasChar == True and isHasNum == True:
#                 f.write(value +'\n')
#
#         f.close()
# getAllNumWithCharInfo()
