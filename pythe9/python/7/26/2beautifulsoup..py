# beautiful 美丽的
# soup  汤
# beautifulsoup 是python的第一个第三方库
# 和xpath作用一样 都是用来解析html数据
# 相比之下xpath的速度回更快一些
# xpath底层是用c来实现的
from bs4 import BeautifulSoup
# beautifulsoup 里面需要两个参数
# 一个为open方法 ，另一个为固定写法'lxml'
# open 方法里面需要两个参数
# 1.想要解析的数据
# 2.设置编码格式
bs = BeautifulSoup(open('index.html',encoding='utf-8'),'lxml')
print(bs)
# beautifulsoup 转化的为类对象
print(type(bs))
# 获取网页当中的title标签
print(bs.title)

# 获取head标签以及head标签内部的所有其他标签
print(bs.head)
# 获取网页当中的第一个a标签
print(bs.a)
# 总结：bs.xx
# 获取所有XX当中的第一个xx以及第一个XX里面的内容
# document 文档
# name 在此指的是获取当前内容的标签名 bs为一个整体 而不是某一个具体的标签
print(bs.name)
# 获取head的标签名
print(bs.head.name)
# 获取title的标签名
print(bs.title.name)
# attr
# attribute 属性
# 获取指定标签的所有属性
# 如果没有做特别处理 bs.xx永远获取的是所有XX中的第一个XX
print(bs.a.attrs)
# KeyError 只能从自己有的属性中找
print(bs.a['id'])
print(bs.a['href'])
# class和id不一样
# id必须是唯一的 一个标签只能有一个id
# class不是唯一的 不同的标签可以拥有同一个class
# 同一个标签页可以拥有多个class
print(bs.a['class'])
print(bs.html['lang'])
print(bs.a)

# delete 删除
del bs.a['id']
print(bs.a)
# 获取指定标签的文本内容
print(bs.a.string)
# string 获取的文本指的是本标签的文本
# 不包含子标签的文本
print(bs.div.string)

# 遍历--------------------------------
# contents 能够获取指定标签下的所有内容
print(bs.head.contents)
print(bs.body.contents)
# 获取所有内容当中的指定索引的内容
print(bs.div.contents[3])
# parent 父级
# 获取指定标签的父级标签 和父级标签内部的所有标签
head = bs.title.parent
print(head)
# tag 标记 标签
print(type(head))

res = bs.find_all('a')
print(res)
for value in res:
    print(value)
# id 是唯一的 通过id来找 只能找到一个 所以用find
# class不是唯一的 通过class来找 可能找到多个
print(bs.find(id="jd"))
print(bs.find_all(class_='shopping'))
# 找到所有符合条件当中的第一个
print(bs.find(class_='shopping'))
print(bs.find_all(id='jd'))

# ---------------select  选择-------------------
# 选择指定的标签
print(bs.select('title'))
# 当选择的队形有多个的时候 嫁过去所有的对象
print(bs.select('a'))
# .表示类名 #表示id
print(bs.select('.frist'))
print(bs.select('#jd'))
# 找到一个类名为now的div标签
print(bs.select('div.now'))
