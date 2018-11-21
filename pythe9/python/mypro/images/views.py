from django.shortcuts import render,redirect,get_object_or_404
from .forms import ImageCreateForm
from django.contrib import messages
from .models import Image
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST,require_http_methods
from django.http import JsonResponse
from action.utils import create_action
import redis
from django.conf import settings
# Create your views here.


r = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)


@login_required
def image_create(request):
    if request.method =='POST':
        form = ImageCreateForm(request.POST)
        if form.is_valid():
            #表单验证通过
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            #把当前用户附加到数据对象上
            new_item.user = request.user
            new_item.save()
            # 行为流 添加了图片动作
            create_action(request.user,'添加了图片',new_item)
            messages.success(request,'图片添加成功')
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(request.GET)
    return render(request,'images/create.html',{'section':'images',
                                                'form':form})

def image_detail(request,id ,slug):
    """
    :url: /images/detail/
    :param request:
    :param id: 图片的id
    :param slug: 图片的slug字段
    :return: {"image":object,"secton":string}
    """
    image = get_object_or_404(Image,id=id,slug=slug)
    # 浏览数+1
    # incr 将键对应的值加一，如果键不存在，自动创建key(初始值为0)然后将值加一
    # redis数据库的key常用冒号分割的字符串，这样的key名容易阅读，便于对应的具体对象和查找
    total_views = r.incr("image:{}:views".format(image,id))
    # 在有序集合image_ranking里，把image的分数加一
    r.zincrby('image_ranking',1,image.id)
    return render(request,'images/detail.html',{"image":image,
                                                'section':'images',
                                                "totla_views":total_views})

@login_required
@require_POST
def image_like(request):
    """

    :param request:
    :return:
    """
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            # 多对多中字段管理
            # 使用add和remove方法用来添加和删除多对多关系
            # add 方法即使传入已经存在的对象，也不会重复建立关系
            # remove方法即使传入不存在的数据对象，也不会报错
            if action == 'like':
                image.user_like.add(request.user)
                create_action(request.user,'喜欢了图片',image)
            else:
                image.user_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'error'})

@login_required
def image_list(request):
    images = Image.objects.all()
    return render(request,'images/image_list.html',{'images':images,"section":"images"})

@login_required
def image_ranking(request):
    #获得排名前十位的图片id列表
    image_ranking = r.zrange('image_ranking',0,-1,desc=True)[:10]
    #获取排名最高的图片然后排序
    most_viewd = Image.objects.filter(id__in=image_ranking)
    return render(request,"images/ranking.html",{"section":'images',
                                                 'most_viewd':most_viewd})

