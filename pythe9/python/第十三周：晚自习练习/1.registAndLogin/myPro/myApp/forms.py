from django import forms
from captcha.fields import CaptchaField
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True,error_messages={'invalid':'邮箱格式错误'})
    password = forms.CharField(min_length=6,required=True,error_messages={'min_length':'密码长度小于6位'})
    captcha = CaptchaField(required=True,error_messages={'invalid':'验证码输入错误'})