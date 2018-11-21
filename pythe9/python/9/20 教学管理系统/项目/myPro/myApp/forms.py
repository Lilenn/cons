from django import forms

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'invalid': '邮箱格式不正确'})
    password = forms.CharField(min_length=6,required=True,error_messages={'min_length':'密码长度不够'})

class LoginForm(forms.Form):
    email = forms.EmailField(required=True,error_messages={'invalid':'邮箱格式不正确'})
    password = forms.CharField(min_length=6 ,required=True,error_messages={'min_length':'密碼長度少於6'})