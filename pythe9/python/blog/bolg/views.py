from django.shortcuts import render,get_object_or_404
from .models import Post,Comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic import ListView
from .forms import EmailPostForm,CommentForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count

# Create your views here.

# FBV 函数视图
# CBV 类视图
# mixins 可服用的类模块

class PostListView(ListView):
    # model = Post
    # queryset 查询所有已发布的文章
    # 可以不用queryset，通过指定model=Post，会进行post.objects.all()查询获得所有的文章
    queryset = Post.publishde.all()
    # 设置posts为模板变量的名称，不过不设置， 默认的名称就是object_list
    context_object_name = "posts"
    paginate_by = 2
    template_name = "blog/post/list.html"
    #返回分页的变量的名称是page_obj



def post_list(request,tag_slug = None):
    posts = Post.publishde.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts,2) #每页显示两篇文章
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page参数不是一个整数，就返回第一页
        posts = paginator.page(1)
    except EmptyPage:
        # 如果页数超出总页数那就返回最后一页
        posts = paginator.page(paginator.num_pages)

    return render(request,"blog/post/list.html",{"posts":posts,"page":page,
                                                 "tag":tag})

def post_detail(request,year,month,day,slug):
    post = get_object_or_404(Post,slug=slug,status="publish",publish__year=year,
                             publish__month = month,publish__day = day)

    # 列出文章的所有活动的评论
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method =="POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # 通过表单直接创建新的数据对象，但是不保存在数据库中
            new_comment = comment_form.save(commit=False)
            # 设置外键为当前文章
            new_comment.post = post
            # 最后将评论写入数据库
            new_comment.save()
    else:
        comment_form = CommentForm()
    # 显示相近的tag列表
    # flat = True 让结果变成一个列表[1,2..]
    post_tags_id = post.tags.values_list("id",flat=True)
    similar_tags = Post.publishde.filter(tags__in=post_tags_id).exclude(id=post.id)
    # 使用count 对每个文章按照标签计数， 并且生成一个新的字段same_tags用于存放计数的结果
    similar_posts = similar_tags.annotate(same_tags=Count("tags")).order_by("-same_tags","-publish")[:2]
    return render(request,"blog/post/detail.html",{"post":post,
                                                   "comments":comments,
                                                   "new_comment":new_comment,
                                                   "comment_form":comment_form,
                                                   "similar_posts":similar_posts})

def post_share(request,post_id):
    # 通过id获取post对象
    post = get_object_or_404(Post,id=post_id,status = "publish")
    send = False
    if request.method == "POST":
    #     表单被提交
        form = EmailPostForm(request.POST)
        # 如果返回false，form.errors
        if form.is_valid():
            #验证表单通过
            cd = form.cleaned_data
            #发送邮件
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = "{} share reding".format(cd["name"])
            message = "read comments {},文章的连接是:{}".format(cd["comments"],
                                                        post_url)
            send_mail(subject,message,cd["email"],[cd["to"]])
    else:
        # 创建一个空白的form对象，展示在页面中是一个空白的表单供用户去填写
        form = EmailPostForm()
    return render(request,"blog/post/share.html",{"post":post,
                                                  "form":form,"send":send})

