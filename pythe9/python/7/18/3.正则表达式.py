import re
# 正则表达式
# 正则表达式可以判断目字符串是否符合特定要求
# 比如： 判断是否为手机号。身份证号 邮箱号
# 1XXXxxxxxxx
# 地区号+出生日期+编号 X


"""
# digit
\d ：表示任意的一位数字
\d\d:表示任意的两位数字
# word
\w：表示任意的一个字母和数字
# space
\s：表示 空格

. :表示任意的内容  123 a,b,c,!@# 不单独使用 经常放到字符串后面
a.: 在a后边匹配任意内容  ad  ac  af
*:表示*前边的内容出现0次到多次
a.*：a  a1 ab  aaaa a111 abbbb
+ :表示+前边的内容出现一次到多次
a.+  : aa  ab  ax  am  an  abb
? :表示?前面的内容出现0次到一次
a.? : a  a1
^ : （脱字符）  表示以。。。开头
$ : 表示以。。。结尾
{n} :表示内容重复多次（n次） \d\d\d  = \d{3}
{n，m} 表示最少重复n次，最多重复m次
{n,}  : 表示最少重复n次
{,m} ： 表示最多重复m次
"""
# pattern模式
# compile 编译
# 后面写正则表达式的内容
# （）代表从目标字符串中获取的子串 
# 每一个（）就是一个group组
pattern = re.compile('(\d)(\w+)')
content = '123helloWorld'
# match 匹配
result = re.match(pattern , content)

if result :
    # 返回的是一个匹配的对象
    print(result)
    # 返回的是符合要求的全部内容
    print(result.group(0))
    print(result.group(1))
    print(result.group(2))
else:
    print('不符合')

pattern = re.compile('my')
result = re.match(pattern , 'myself')
print(result.group(0))
# match 匹配的是 内容的开始部分
# 作用等同于 startwith
result = re.match(pattern,'love myself')
print(result)

pattern = re.compile('lalala')
result = re.match(pattern,' lalala')
print(result)

pattern = re.compile('my')
result = pattern.match('myself')
print(result)

# 贪婪模式与非贪婪模式
# 正则表达式为贪婪模式 尽量找到符合要求的所有内容
# .* 称之为贪婪模式
content = 'aabbababa11b222'
pattern = re.compile('(a.*b)')
result = pattern.match(content)
print(result)
# .*?   : 称之为 非贪婪模式
# 从a 开始 往后 任意字符出现0次或多次 直到遇见第一个b 就结束
pattern = re.compile('(a.*?b)')
result = pattern.match(content)
print(result)
# 匹配任意字符开头 后面找到一个以b开头  以b结尾的内容
pattern = re.compile('.*?(b.*?b)')
result = pattern.match(content)
print(result)

# * + 同为贪婪模式
# *至少0次 至多无限次
# + 至少1次 至多无限次
content ='33bbb2233bbb'
pattern = re.compile('(a.+b)')
result = pattern.match(content)
print(result)

print('hello \n world')
# raw string 会将字符串里面的转义字符输出出来
print(r'hello \n world')

tilte = '123Hello world'
# pattern = re.compile(r'\d\d\d')
# 匹配连续三个数字
pattern = re.compile(r'\d{3}')
result = pattern.match(tilte)
print(result)

# 匹配全国固话  0371-66666666
pattern = re.compile(r'(\d{4})-(\d{8})')
result = pattern.match('0371-68686688')
print(result)
print(result.group(1))
print(result.group(2))

# | 或者 设置用于不同情况的正则
pattern = re.compile('((haha|heihei)balabala)')
result = pattern.match('hahabalabala')
result = pattern.match('heiheibalabala')
print(result)

# 找到字符串当中第一个符合正则的内容
# 注意：只找到第一个
pattern =re.compile(r'http')
# search 查找
result = pattern.search('www.jd.com,http://www.taobao.com')
print(result)

pattern = re.compile(r'you')
result = pattern.search('I love you , I miss you , I  hate you')
print(result)

pattern = re.compile(r'I')
result = pattern.search(' love you I')
print(result)
# findall  找到所有符合的内容
content = '12345,上山打老虎，老虎没打着，打只小松鼠，55555'
pattern = re.compile(r'\d{5}')

result = pattern.findall(content)
print(result)

content = '杨过对战金轮法王,郭靖观战'
# sub : 替换子串（字符串的一部分）
# \s：匹配空白的内容
pattern = re.compile(r'杨\s*过')
result = pattern.sub('吕布',content)
print(result)


pattern = re.compile(r'金轮法王')
result = pattern.sub('服部半藏',result)
print(result)

key_word = [
    (r'杨\s*过','吕布'),
    (r'金轮法王','服部半藏'),
    (r'郭靖','东方不败')
]
print('---------------------------------------')
for pattern , replace in key_word:
    pattern = re.compile(pattern)
    content = pattern.sub(replace,content)
print(content)

# 匹配手机号
pattern = re.compile(r'^((13[0-9])|(14[67])|(15[0-3|5-9])|(18[0|5-9]))\d{8}$')
result = pattern.match('14674239584')
print(result)



content = '567helloworld'
pattern = re.compile('\d{3}')
result = re.match(pattern, content)
print(result)

content = 'adfhhhkkl1229l0'
pattern = re.compile('(a.*?l)')
result = pattern.match(content)
print(result)

content = 'you are the only one I bilieve in'
pattern = re.compile('o')
result = pattern.findall(content)
print(result)


content = '真相永远只有一个，柯南说的'
pattern = re.compile(r'柯\s*南')
result = pattern.sub('新一',content)
print(result)