from django.shortcuts import render
from django.views import View
from .forms import RegisterForm ,LoginForm,ForgetForm,ResetForm
from .models import UserProfile ,EmailRecord,ResetWithEmail
from django.contrib.auth.hashers import make_password ,check_password
from utils.email_send import send_email
from django.contrib.auth import authenticate

# Create your views here.
# def index(request):
#     return render(request ,'index.html')
# def regist(request):
#     return render(request ,'register.html')


class RegisterView(View):
    def get(self , request):
        register_form = RegisterForm()
        return render(request ,'register.html',{'register_form':register_form})
    def post(self ,request):
        # 验证账号密码的合法性
        register_form = RegisterForm(request.POST)
        # 如果所有内容合法
        if register_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            # 判断是否有相同的账号在 数据库中
            user = UserProfile.objects.filter(email=email)
            # 如果有
            if user:
                # 注册失败 返回注册界面 同时返回失败信息
                return render(request ,'register.html',{'register_form':register_form,
                                                        'msg':'该用户已经被注册'})
            # 账号密码合法 同时该用户未被注册
            user = UserProfile()
            user.email = email
            # make制作
            # make_password 将之前密码进行加密
            user.password = make_password(password)
            user.username = email
            user.is_active = 0
            user.save()

            send_email(email=email)
            # 注册成功的同时  发送邮件给对方 通知对方注册成功

            return render(request,'tips.html',{'title':'注册成功','url':'/login/login/'})
        # 数据不合法
        else :
            return render(request,'register.html',{'register_form':register_form})

class LoginView(View):
    def get(self ,request):
        return render(request ,'login.html')
    def post(self , requset):
        login_form = LoginForm(requset.POST)

        if login_form.is_valid():
            email  = requset.POST['email']
            password = requset.POST['password']

            # user = UserProfile.objects.get(email=email)
            # 驗證賬號密碼是否一致
            # user = authenticate(email=email,password=password)
            user = UserProfile.objects.get(email=email)
            result = check_password(password,user.password)

            if result :
                if user.is_active == 1 :
                    return render(requset ,'home.html')
                else :
                    code_obj = EmailRecord.objects.get(email=email)
                    code = code_obj.code
                    send_email(email,code)
                    return render(requset ,'login.html',{'login_form':login_form,'msg':'该账号尚未被激活，请前往邮箱进行激活'})

            else :

                return render(requset,'login.html',{'login_form':login_form,'msg':'账号密码不匹配，请核对'})

        else :
            return render(requset,'login.html',{'login_form':login_form})


class ActiveView(View):
    def get(self ,request,code):
        try:
            # 根据指定的激活码找对应的邮箱
            email_code = EmailRecord.objects.get(code=code)
        except Exception as e :
            # 如果邮箱没有被找到
            return render(request,'active_fail.html')
        else :
            # 如果邮箱被找到
            user = UserProfile.objects.get(email=email_code.email)
            user.is_active = 1
            user.save()
            return render(request ,'login.html')

    def post(self ,request ,code):
        pass
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
    def post(self,request):
        return render(request,'home.html')

class ForgetView(View):
    def get(self,request):
        return render(request,'forget.html')
    def post(self,request):
        email_obj = ForgetForm(request.POST)
        if email_obj.is_valid():
            # 获取邮箱
            email = request.POST['email']
            result = send_email(email,email_type='forget')

            if result == 1:
                # 确保数据库永远只有一条数据
                reset_email = ResetWithEmail.objects.filter(id=1)
                if reset_email:
                    reset_email[0].email = email
                    reset_email[0].save()
                else:
                    reset_email = ResetWithEmail()
                    reset_email.email = email
                    reset_email.save()

                return render(request,'tips.html',{'title':'邮件发送成功','url':'/login/reset/'})
            else:
                return render(request,'forget.html',{'msg':'出现未知错误，邮件发送失败'})
        else:

            return render(request,'forget.html',{'form':email_obj})

class ResetView(View):
    def get(self,request,reset):
        return render(request,'reset.html')
    def post(self,request,reset):
       pass

class ResetPageView(View):
    def get(self,request):
        return render(request,'reset.html')
    def post(self,request):
        reset_obj = ResetForm(request.POST)

        if reset_obj.is_valid():
            password = request.POST['password']
            again = request.POST['again']
            if password == again :
                # 取出该数据库里边的第一条数据
                email = ResetWithEmail.objects.get(id=1)
                user = UserProfile.objects.get(email=email.email)
                user.password = make_password(password)
                user.save()

                return render(request,'login.html')
            else:
                return render(request,'reset.html',{'msg':'两次密码不一致'})
        else:
            return render(request,'reet.html',{'reseta_form':reset_obj})

"""
使用验证码时候的问题
1.RuntimeError: Model class captcha.models.CaptchaStore doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
 在setttings里面进行注册app
2.Make sure you've included captcha.urls as explained in the INSTALLATION section on http://readthedocs.org/docs/django-simple-captcha/en/latest/usage.html#installation
 在项目里面urls进行设置
3.no such table
  重新模型迁移
"""
