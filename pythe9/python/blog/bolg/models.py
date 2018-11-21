from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
# 数据架构 data schema
# schema 是一个数据库名词，一般指的是数据在数据库的组织模式或者说是架构
# Create your models here.
# queryset 查询结果集对象


# post.objects.my_manager（） 提供一个新方法
# post.my_manager.all()

# 创建模型管理器
class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager,self).get_queryset().filter(status="publish")


class Post(models.Model):
    STATUS_CHOICES = (("draft","草稿"),("publish","发布"))
    title = models.CharField(max_length=300,verbose_name="标题")
    slug = models.SlugField(max_length=200,unique_for_date="publish")
    # related_name 设置从user到post的反向关联关系，用bolg_post为这个
    # 反向关联关系命名
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blog_posts")
    body = models.TextField()
    # timezone.now 包含时区的时间对象
    publish = models.DateTimeField(default=timezone.now)
    # auto_now_add 表示当创建一行数据的时候，自动用创建数据的时间填充
    created = models.DateTimeField(auto_now_add=True)
    # auto_now 表示每次更新数据的时候，都会用当前的时间填充
    updatad = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default="draft")

    class Meta:
        db_table = "blog" # 表名
        ordering = ("-publish",)

    def __str__(self):
        return self.title

    objects = models.Manager() # 默认的管理器
    publishde = PublishManager() #自定义的管理器
    tags = TaggableManager()#taggit的模型管理器

    # 创建超链接到具体的数据对象
    def get_absolute_url(self):
        return reverse("blog:post_detail",args=[self.publish.year,
                                                self.publish.month,
                                                self.publish.day,
                                                self.slug])


class Comment(models.Model):
    # 评论 post.comment_set
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'comment'
        ordering = ('created',)

    def __str__(self):
        return "comment title {} on {}".format(self.name,self.post)

