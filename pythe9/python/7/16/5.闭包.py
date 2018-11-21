
def outSide(a,b):
    def inside():
        return  a+b
    return inside
print(outSide(10,11))
result = outSide(10,11)
print(result())

# 外层函数包含内层函数 同时内层函数使用内层函数的参数
# 并且将内层函数返回出去 这种结构称之为闭包
# 1。函数包裹函数
# 2。内层函数使用外层函数的参数
# 3,。内层函数当成返回值