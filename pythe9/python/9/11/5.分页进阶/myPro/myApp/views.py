from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.http import HttpResponse
import random
from .models import Goods
# Create your views here.
def index(request):

    # for x in range(200):
    #     good = Goods(name='good%s'% x , des='该商品物美价廉，现在只需要{}元'.format(random.randint(10,100)))
    #     good.save()

    return HttpResponse('数据添加成功')

def select(request):

    good_list = Goods.objects.all()

    # 值3：当最后一页数据少于n条时，将数据并入上一页
    paginator = Paginator(good_list,12 , 3)

    try:
        # GET 请求方式  get() 获取指定key值指定的value值
        # 获取index的值 如果没有 则设置使用默认值1
        num = request.GET.get('index','1')
        number = paginator.page(num)
    except PageNotAnInteger:
        # 如果输入的页码数 不是整数 那么显示第一页数据
        number = paginator.page(1)
    except EmptyPage:
        # 如果页码数不在当前页码内，则显示最后一页
        # paginator.num_pages获取当前总页数
        # paginator.page()获取指定的某一页
        number = paginator.page(paginator.num_pages)

    print(paginator.num_pages)

    # 将当前页 页码 以及 当前页数据 传递到index.html
    return render(request,'index.html',{'page':number,'paginator':paginator})