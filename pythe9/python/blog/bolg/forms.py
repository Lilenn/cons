from django import forms
from .models import Comment
# django使用两个类来创建表单
# forms.Form 用于生成标准的表单
# forms.ModelForm 用于从模型中生成表单

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=35)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name","email","body")
        # exclude 属性指定需要排除的字段
        # exclude = ("created")

