
#字符串拼接 +
name = '张三'
fond = '喝酒'
print(name + '喜欢' + fond)

# JS
# %s 占位符 计算机里面常见的一个符号
# 作用是 相当于一个变量
print('我的姓名是%s' % name)
print('我的姓名是%s , 我的爱好是%s' % (name , fond))

# format 格式
content = 'Python9期'
# .format()里面直接写值或者写变量
print('我们是{}的学员'.format('大数据'))
# code 代码
print('我们是{},我们喜欢{}'.format('CodingMan','Coding'))
