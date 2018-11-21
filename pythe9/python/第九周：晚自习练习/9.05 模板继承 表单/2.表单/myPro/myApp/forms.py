# forms.py 是django里面用来生成form表单的一个文件
# 在这个文件里面可以实现form表单的定义
# 我们可以让这个文件作用于html里面
# 以达到丰富html页面的效果
# 比如，设置表单内容类型或者合法性检查

# <form action="" method=''>
#     <label></label>
#     <input type='text'>
#     <input type='number'>
#     <button type='submit'>
# </form>
# 使用forms会自动为我们生成label标签以及input标签
# 但是form标签以及button标签需要自己来写

from django import forms

class SumForm(forms.Form):
    a1 = forms.IntegerField(label='num1')
    b1 = forms.IntegerField(label='num2')