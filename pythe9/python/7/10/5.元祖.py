
# python里面容器的类型有几种
# 1.list
# 2.tuple
# 3.set
# 4.dict

# list 里面的元素是可变的  可以进行增删改
# tuple 里面的元素是不可改变的 只能查看 不能增删改(创建时记得添加元素）

tp1 = ()
tp2 = tuple()

tp1 = ((),[],{},1,2,3,'a','b','c',3.14,True)
print(tp1[:])
print(tp1[1::2])
print(tp1[5])
# AttributeError: 'tuple' object has no attribute 'remove'
# attribute 属性错误 object 对象
# 属性错误：元祖对象没有属性'remove'
# tp1.remove()
# print(tp1)

# 晚自习作业:重现8种错误









