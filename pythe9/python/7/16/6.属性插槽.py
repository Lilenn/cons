
name = '小明'
age = 16
print('{},{}'.format(name ,age))
print('{},{}'.format(age ,name))

class Poeple(object):
    def __init__(self, name='',age =''):
        self.name = name
        self.age = age
p = Poeple('赵云',27)
print(p.name)
print(p.age)
# 给对象添加一个属性
p.fond = '学习'
print(p.fond)
# 无则添加 有则修改
dic = {}
dic['name'] = '小兰'
print(dic['name'])


class Persor(object):
    # slots插槽
    # 表示 只支持本类添加[]里面的包含属性
    __slots__ = ['name ','age']
    def __init__(self, name ='',age =''):
        self.name = name
        self.age = age
p1 = Persor('样件',300)
print(p1.name)
print(p1.age)
p1.dog = '哮天犬'
print(p1.dog)