from django.shortcuts import render
from django.views import View
from .forms import RegisterForm
from .models import UserProfile
from django.contrib.auth.hashers import make_password
from utils.email_send import send_email
# Create your views here.
class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form})
    def post(self,request):
        # 验证账号密码合法性
        register_form = RegisterForm(request.POST)
        # 如果内容合法
        if register_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            # 判断是否有相同的账号在 数据库中
            # filter 过滤器
            user = UserProfile.objects.filter(email=email)
            # 如果账户存在
            if user:
                return render(request,'register.html',{'register_form':register_form,'msg':'该用户已经被注册'})

            # 账号密码合法 同时未被注册

            user = UserProfile()
            user.email = email
            # make_password 将之前的密码进行加密
            user.password = make_password(password)
            user.username = email

            send_email(email=email)
            user.save()

            # 注册成功的同时 发送邮件给对方 通知对方进行账号激活
            return render(request,'tips.html')

        # 数据不合法
        else:
            return render(request,'register.html',{'register_form':register_form})
