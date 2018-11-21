from django import forms
from captcha.fields import CaptchaField
import datetime
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True,error_messages={'invalid':"邮箱格式不正确"})
    password = forms.CharField(min_length=6,required=True,error_messages={'min_length':'密码长度不够'})
    captcha = CaptchaField(required=True,error_messages={'invalid':'验证码错误'})

class LoginForm(forms.Form):
    email = forms.EmailField(required=True,error_messages={'invalid':'郵箱格式不正確'})
    password = forms.CharField(min_length=6 ,required=True,error_messages={'min_length':'密碼長度少於6'})

class ForgetForm(forms.Form):
    email = forms.EmailField(required=True,error_messages={'invalid':'邮箱格式不正确'})

class ResetForm(forms.Form):
    password = forms.CharField(required=True,min_length=6,error_messages={'min_length':'密码长度小于6位'})
    again = forms.CharField(required=True,min_length=6,error_messages={'min_length':'密码长度小于6位'})
