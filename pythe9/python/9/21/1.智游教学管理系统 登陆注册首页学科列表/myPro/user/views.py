from django.shortcuts import render,redirect
from django.views import View
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate
import json
# 验证登录的装饰器
from django.contrib.auth.decorators import login_required
# Create your views here.

class RegisterView(View):
    """注册"""
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']

        if len(username) == 0 or len(password) == 0:
            return render(request,'register.html',{'msg':'账号和密码不能为空'})
        if UserModel.objects.filter(username = username):
            return render(request,'register.html',{'msg':'用户已将注册'})
        user = UserModel()
        user.username = username
        """密码加密"""
        password = make_password(password)
        user.password = password
        user.save()
        return render(request,'login.html')
class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        # 取值成功 返回user对象 不成功或者没有数据 返回none
        # encoded = make_password(password)
        # 获取user对象
        # user = UserModel.objects.get(username=username)
        # 验证密码
        # bool_value = check_password(password, user.password)
        # print('====', bool_value)

        user = authenticate(username=username,password=password)

        # if UserModel.objects.filter(username=username,password=password):

            # user = UserModel.objects.get(username = username)
            # 获取当前登陆的对象
        if user:
            login(request,user)

            return redirect('/subject/')
        else:
            return render(request,'login.html',{'msg':'账号或者密码错误'})


class LogOutView(View):
    def get(self,request):
        # 抹除登录 从request中删除user对象
        logout(request)
        return redirect('/user/login/')

# 函数视图
@login_required
def test_json(request):
    if request.method == 'POST':
        json_id = request.method['json_id']
        a = request.POST['a']
        b = request.POST['b']
        print(a,b,json_id)
    return HttpResponse(json.dumps({'a':'ok'}),content_type='application/json')
def page_not_found(request):
    return render(request,'404.html',status=404)
def page_error(request):
    return render(request,'404.html',status=500)