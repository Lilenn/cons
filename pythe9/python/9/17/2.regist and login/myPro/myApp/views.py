from django.shortcuts import render
from django.views import View
from .forms import RegisterForm,LoginForm
from .models import UserProfile,EmailRecord
from utils.email_send import send_email
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    return render(request,'index.html')
def regist(request):
    return render(request,'register.html')

class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form})
    def post(self,request):
        # 验证账号密码的合法性
        register_form = RegisterForm(request.POST)
        # 如果所有内容合法
        if register_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
        # 判断是否有相同账号在数据库中
            user = UserProfile.objects.filter(email=email)
            # 如果有
            if user :
                # 注册失败 返回注册界面 同时返回失败信息
                return render(request,'register.html',{'register_form':register_form,'msg':'该用户已经被注册'})

            # 账号密码合法 同时未被注册
            user = UserProfile()
            user.email = email
            # make_password 将之前的密码进行加密
            user.password = make_password(password)
            user.username = email
            user.is_active = 0
            user.save()

            # 注册成功的同时 发送邮件给对方 通知对方注册成功
            send_email(email=email)
            return render(request,'tips.html')
        # 数据不合法
        else:
            return render(request,'register.html',{'register_form':register_form})

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST['email']
            passowrd = request.POST['password']

            # 验证账号密码是否一致
            # user = authenticate(email = email,passowrd = passowrd)
            user = UserProfile.objects.get(email=email)
            result = check_password(passowrd,user.password)
            if result:
                if user.is_active == 1:
                    return render(request, 'home.html')
                else:
                    code_obj = EmailRecord.objects.get(email = email)
                    code = code_obj.code
                    send_email(email,code)
                    return render(request,'login.html',{'login_form':login_form,'msg':'该账号尚未被激活，请前往邮箱进行激活'})
            else:
                return render(request,'login.html',{'login_form':login_form,'msg':'账号密码不匹配，请核对'})
        else:
            return render(request,'iogin.html',{'login_form':login_form})
class ActiveView(View):
    def get(self,request,code):
        # 根据指定的激活码找到指定的邮箱
        try:
            email_code = EmailRecord.objects.get(code = code)
        except Exception as e:
            # 如果邮箱没有找到
            return render(request,'active_fail.html')
        else:
            # 如果邮箱被找到
            user = UserProfile.objects.get(email=email_code.email)
            user.is_active = 1
            user.save()
            return render(request,'login.html')

    def post(self,request,code):
        pass