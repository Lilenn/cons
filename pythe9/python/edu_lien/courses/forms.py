from django import forms
from django.forms.models import inlineformset_factory
from .models import Course,Module

# inlineformset_factory()内联表单工厂函数 实在普通表单集之上的一个抽象。
# 这个函数允许我们动态的通过与Course模型关联的module模型创建表单集
# fields 表示表单集中的每个表单的字段
# extra 设置每次表单集的表单数量
# can_delete为每个表单内包含一个布尔值字段，用户可以选中需要删除的表单
ModuleFormSet = inlineformset_factory(Course,Module,fields=['title','description'],extra=2,
                                      can_delete=True)
