

# 普通形参必须放在默认参数的前边
# 默认参数必须放在参数列表的队尾

def testA():
    return  200
def testB(argument):
    print(argument)
# 函数里面的参数可以为任意类型
testB(testA())

def test(a, *args):
    print(a)
    print(*args)
test(1,2,3,4,5,6)
