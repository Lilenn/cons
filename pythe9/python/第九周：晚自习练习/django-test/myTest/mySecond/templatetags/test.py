from django.template import Library
# 注册当前的数据
# 注册完以后，必须重启，否则程序可能会崩
register = Library()
@register.filter
def add(value):
    pass

