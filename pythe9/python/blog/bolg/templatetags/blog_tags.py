from django import template
from bolg.models import Post
from django.db.models import Count

# 用来注册一个自定义的标签
register = template.Library()

@register.simple_tag
def total_posts():
    return Post.publishde.count()

@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=2):
    latest_posts = Post.publishde.order_by("-publish")[:count]
    return {"latest_posts":latest_posts}


@register.simple_tag
def get_most_comment_posts():
    return Post.publishde.annotate(total_comments=Count("comments")).order_by("-total_comments")[:2]

@register.filter
def posts_add(num,inc):
    return num + inc

@register.simple_tag
def show_all_unactive():
    all_unactive = Post.objects.filter(status="draft")
    return all_unactive
