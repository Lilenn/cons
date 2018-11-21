

# str = ''
# str =""
# str = ''''''
# str = """"""
""""
python里面的多行注释 用这种方式
其实质 就是一个大的字符串
"""
# 字符串：一串字符链接在一起，称之为字符串
# 字符：
# 再有基本数据类型的其他语言里面：char 声明的是字符  string生命的是字符串
# char
# string
# 在引号里面写的内容 不管是什么都是一个字符串
# content = 'a'

content = ''
content = 'hello world'
# -------------------------字符串切片操作----------------------------------
# 字符串也是一个容器  可以存放任意一个字符
# 容器里面所有的元素都有一个编号
# 编号从0开始
print(content[0])
# IndexError: string index out of range
# 索引错误：字符串超出了范围
# 解决办法：查看字符串的范围 索引要小于长度
# 晚自习作业：1.写一篇博客 记录所有的错误信息 （CSDN 博客）
# print(content[21])
# 从获取指定索引开始到结束的字符串内容（包含指定索引的开始的位置）
print(content[3:])
# 获取开始到指定索引的内容（不包括指定索引的这个位置）
print(content[:3])
#
print(content[3:6])
# ：前面是开始额位置，如果不写  默认为 0
# ：后面 为结束位置 如果不写 默认到结尾
print(content[:-1])
print(content[1:-1])
# 倒叙   hello world
print(content[::-1])
# 值1：从哪开始
# 值2：到哪结束
# 值3：每次往后隔几位 默认是1
# el ol
print(content[1::2])
# 以上操作都没有真正的改变字符串的内容
# 如果要改变，需要这样写
content = content[1::4]
print(content)

# ---------------------------------------find-----------------------------------------------------
content = 'hello world'
# 查看content里面有没有指定的字符串
# 如果返回-1 则表示没有找到指定的内容
# 如果返回其他值 表示找到 返回的值问该字符在字符串当中的索引
# 晚自习作业2：不能使用find方法，自己模拟find方法的实现过程
      # 判断字符窜当中有没有包含指定字符 如果有，
#     返回其在字符串当中的位置，如果没有返回-1
# -1
result = content.find('h')
print(result)
# 大小写在ASCII码中值不一样






# ---------------------------------------index------------------------------------------------

content = 'hello world'
# ValueError: substring not found
# 值错误：子字符串未找到
result = content.index('r')
print(result)

# ---------------------------------------count------------------------------
content = 'hello world'
# 获取指定字符在字符串当中的个数
result = content.count ('zhang')
print(result)

# --------------------------------------replace------------------------------------
# 替换 将L 替换成T  hetto wortd
content = 'hello world'
result = content.replace('l','t')
print(result)

# --------------------------------------splite-------------------------------------------
# 分割    ['he', '', 'o wor', 'd']
content = 'hello world'
result = content.split('l')
print(result)

# -------------------------------------大小写转换---------------------------------------
content = 'hello world'
# hello world 字符全部小写  只能转化英文字母的大小写
print(content.lower())
# 字符全部大写  HELLO WORLD
print(content.upper())
# 首字母大写，其余小写  Hello world
print(content.capitalize())
# 转化成小写  支持utf-8 hello world
print(content.casefold())

# -------------------------------------start ,end--------------------------------------------
content = 'hello world'
# start,end 会返回一个bool
# startswith:以W为开头  False  错误
# endswith:y=以D为结尾  True   正确
print(content.startswith('w'))
print(content.endswith('d'))

# ------------------------------------maketrans----------------------------------------

content = '习近平近日来智游某基地进项参观并发表重要讲话'
# 制作规则：将智游替换成XX
# 让content遵守这个规则  习近平近日来XX某基地进项参观并发表重要讲话
s = str.maketrans('智游','XX')
content = content.translate(s)
print(content)



# ctrl +shift+ r  全文指定替换
# ctrl + f 查找