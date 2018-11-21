#   0   1    2
# ['a','b','c']
info = '今天是星期四 Hello World'
print(info[7])
# 获取指定内容  切片操作
# 值1：开始位置 （包括该位置）
# 值2：结束位置  （不包括该位置）
print(info[3 : 5])
# IndexError: string index out of range
# 索引错误：字符换索引超出范围
# print(info[100])
# 当范围超出边界的时候
# 直接获取从指定开始到字符串结束的部分
print(info[3:100])

info = '2018七月七,我在智游吃炸鸡'
# 获取从指定位置到结束位置的内容
print(info[3:])
# 反序截取字符串
print(info[:-3])
# 相当于直接获取info的整个内容
print(info[:])
print(info[:3])

# 昨天问题
num = '100'
if num.isdigit() :
    # '1'  '2'  '100'
    num = int(num)
else:
    # '-1' , '-1000'  1000
    num = num[1:]
    print(num)
    num = int(num)
    num = num * -1
    print(num)

# 晚上作业:
#     '-123abc567' 转化数字 123567
#     不管数字和字母字母组合 出来的结果就是数字
# if 如果包含a
#     去掉a
# if 如果包含b
#     去掉b
#  去掉第四个 第五个  第六个

# --------------------find------------------------
content = '张三李四王二麻子'
result = content.find('李四')
print()
print(result)
# 不存在 -1 存在是0
if result == -1 :
    print('不存在')
else :
    print('存在')

# -------------------------index-----------------------
info = '好好学习，天天向上'
# ValueError: substring not found
# 在整个info范围内找
result = info.index('学习')
# 在编号5与7之间找
# result = info.index('学习',5,7)
print(result)

# ---------------------count--------------------
info = 'hello world'
# 总数 获取指定子元素的个数
result = info.count('l')
print(result)

info = '程序员，设计师，工程师'
# replate 替换
# 值1：旧值
# 值2：新值
info = info.replace('，','/')
print(info)

# --------------------------------split--------------------------
url = 'http://www.baidu.com/image.jpg'
print(url[21:])
# split 分割
result = url.split('/')
print(result)
print(result[-1])

info = 'hello world'
# 首字母大写
print(info.capitalize())
# 全部首字母大写
print(info.title())

url = 'taobao.com'
# 如果url不是以XXXX开头
if not url.startswith('https://www.'):
    url = 'https://www.' + url
print(url)

name = '小明'
# not不是必须要和if组合在一起
if not name.endswith('欧巴'):
    name = name + '欧巴'
print(name)

info = 'Hello World'
# 全部变成小写
info = info.lower()
print(info)
# 全部变成大写
info = info.upper()
print(info)

message = '习近平近日来智游参观并作出重要指示'
# 指定规则
s = str.maketrans('智游','某游')
# translate翻译  根据规则进行翻译
print(message.translate(s))

'!@#$%asdsfghfgj32324356576#&#$%^&*()_dsfgh'
str = 'asdaSfawf5645646csfcc45634fd,./,;566654Fdcf'
index = 0
str1 = []
while index<len(str):
    if str[index] >="0" and str[index]<="9":
        str1 += str[index]
    index += 1
print(str1)


a = '123567'
for i in '-123abc567':
    if i.isdigit():  #'1' '2'
        a += i
a = int(a)   #123567
print(a)

s = input('请随便输入：')
for i in range(0, len(s)):
    if s[i].isdigit():
        print(s[i])
    else:
        pass


index = input('请随便输入')
for index in index :
     if index.isdigit():
         index = int(index)
         print(index,end='')

code = "selectLine.style.transform = 'rotate(' +  (selectLine.angel + 360 / allNames.length ) + 'deg)"
code = "selectLine.style.transform = 'rotate(' +  (selectLine.angel + 360 / allNames.length ) + 'deg)"
code = code.replace("(",".")
code = code.split(".")
for x in code:
    if x.startswith("s"):
         print(x)

num = ''
code = "selectLine.style.transform = 'rotate(' +  (selectLine.angel + 360 / allNames.length ) + 'deg)"
# code = code.lower()
for info in code:
    if not (97<=ord(info)<=123 or 65<=ord(info)<=90):
        num += ' '
    else:
        num += info
num = num.split()
print(num)
lists = []
for info in num:
    if info[0] == 's':
        lists.append(info)
print(lists)


