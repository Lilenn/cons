from django.shortcuts import render
from django.http import HttpResponse
# 引入django中自带的分页模块
from django.core.paginator import Paginator
# Create your views here.
from .models import Data
def index(request):
    # d1 = Data(name='张三')
    # d2 = Data(name='李四')
    # d3 = Data(name='王五')
    # d4 = Data(name='赵六')
    # d5 = Data(name='冯七')
    # d6 = Data(name='孙八')
    # d7 = Data(name='郑九')
    #
    # d1.save()
    # d2.save()
    # d3.save()
    # d4.save()
    # d5.save()
    # d6.save()
    # d7.save()

    result = Data.objects.all()
    # 设置分页信息
    # 值1：当前所有数据的个数
    # 值2：每页显示多少条数据
    p = Paginator(result , 3)
    print('商品个数',p.count)

    print('总页数',p.num_pages)

    print('页码范围',p.page_range)

    # 页码从1开始
    print('获取第一页',p.page(1))

    all = p.page(1).object_list
    # print(all)
    for data in all:
        print(data.name)
    print('第一页所有数据',all)

    for data in p.page(2).object_list:
        print(data.name)
    print('获取第2页数据')

    # 获取 当前页的页码
    print(p.page(2).number)

    page2 = p.page(2)

    # 是否有上一页
    print(page2.has_previous())
    # 是否有下一页
    print(page2.has_next())
    # 除了本页是否有其他页
    print(page2.has_other_pages())
    # 获取上一页页码
    print(page2.previous_page_number())
    # 获取下一页页码
    print(page2.next_page_number())

    # 指定页面内部元素的第一个索引
    print(page2.start_index())
    # 指定页面的内部元素的最后一个索引
    print(page2.end_index())
    return HttpResponse('hello world')