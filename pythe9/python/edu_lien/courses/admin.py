from django.contrib import admin
from .models import Subject,Course,Module

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    prepopulated_fields = {"slug":("title",)}


class ModuelInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title','subject','created')
    list_filter = ('created','subject')
    search_fields = ('title','ovreview')
    prepopulated_fields = {"slug":('title',)}
    inlines = [ModuelInline]