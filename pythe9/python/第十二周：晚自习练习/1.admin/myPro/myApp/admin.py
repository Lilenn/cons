from django.contrib import admin
from .models import Author,Article
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','age']
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','type','public_date','author']

admin.site.site_header = '智游后台管理'
admin.site.site_title = '智游'
admin.site.register(Author,AuthorAdmin)
admin.site.register(Article,ArticleAdmin)