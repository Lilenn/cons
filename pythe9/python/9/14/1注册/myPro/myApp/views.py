from django.shortcuts import render
from django.views import View
from .forms import RegisterForm
from .models import CustomUser
from django.http import JsonResponse
# Create your views here.

class Register(View):
    def get(self,request):

        return render(request,'regist.html')
    def post(self,request):
        # 获取请求对象里面所有的参数值
        # 使用registerform 是为了更方便的验证账号密码格式是否正确
        # 因为 registerform 里面每一个字段都设置了 限制条件
        regist_form = RegisterForm(request.POST)
        # vaild可用的
        # 如果 格式正确
        result = {}
        if regist_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            # filter 过滤  email1 字段 email2 值
            if CustomUser.objects.filter(email=email):

                result['code'] = 1101
                result['message'] = '改用户已经注册'
            else:
                user = CustomUser()
                user.email = email
                user.password = password
                user.username = email
                user.save()
                result['code'] = 200
                result['message'] = '恭喜用户注册成功'
            return JsonResponse(result)

        else:

            result['code'] = 301
            result['message'] = '账号密格式不正确，请检查'
            return JsonResponse(result)
