from django.template import Library
# 注册当前的数据
# 注册完以后，必须重启，否则程序可能会崩
register = Library()
# 注册过滤器
@register.filter
def add(value):
    pass
@register.filter
def girl_des(value):

    has = '没有'
    if value['hasKuang'] == True:
        has = '有'
    return '我女朋友叫做' + value['name'] + ' ，身高' + value['height'] + 'cm , 家里边' + has + '矿'