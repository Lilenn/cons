from django import forms
from captcha.fields import CaptchaField

class RegisterForm(forms.Form):
    email = forms.EmailField(required = True,error_messages={'invalid':"邮箱格式不正确"})
    password = forms.CharField(min_length=6,required=True ,error_messages={'min_length':"密码长度不够"})
    captcha = CaptchaField(required=True,error_messages={'invalid':'验证码错误'})

class LoginForm(forms.Form):
    email = forms.EmailField(required=True,error_messages={'invalid':'邮箱格式不正确'})
    password = forms.CharField(min_length=6,required=True,error_messages={'min_length':'密码长度少于6位'})