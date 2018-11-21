from django.shortcuts import render
from django.views import View
from .forms import RegisterForm ,LoginForm
from .models import UserProfile,Subject
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import login
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request,'base.html')

class RegisterView(View):
    def get(self , request):
        register_form = RegisterForm()
        return render(request ,'register.html',{'register_form':register_form})
    def post(self ,request):
        # 验证账号密码的合法性
        register_form = RegisterForm(request.POST)
        # 如果所有内容合法
        if register_form.is_valid():
            email= request.POST['email']
            password = request.POST['password']
            # 判断是否有相同的账号在 数据库中
            user = UserProfile.objects.filter(email=email)
            # 如果有
            if user:
                # 注册失败 返回注册界面 同时返回失败信息
                return render(request ,'register.html',{'register_form':register_form,'msg':'该用户已经被注册'})
            # 账号密码合法 同时该用户未被注册
            user = UserProfile()
            user.email = email
            # make制作
            # make_password 将之前密码进行加密
            user.password = make_password(password)
            user.username = email
            user.save()
            return render(request,'tips.html',{'title':'注册成功','url':'/login/'})
        # 数据不合法
        else :
            return render(request,'register.html',{'register_form':register_form})

class LoginView(View):
    def get(self ,request):
        return render(request ,'login.html')
    def post(self , requset):
        login_form = LoginForm(requset.POST)
        # 判断账号是否合法
        if login_form.is_valid():
            email  = requset.POST['email']
            password = requset.POST['password']
            user = UserProfile.objects.get(email=email)
            result = check_password(password, user.password)
            # 判断账号密码是否一致
            if result:

                user = UserProfile.objects.get(email=email)
                login(requset,user)

                return render(requset, 'subject.html')
            else:
                return render(requset, 'login.html', {'login_form': login_form, 'msg': '账号密码不匹配，请核对'})
        else :
            return render(requset,'login.html',{'login_form':login_form})

def subject(request):
    allInfo = Subject.objects.all()
    return render(request,'subject.html',{'allinfo':allInfo})

class AddView(View):
    def get(self,request):
        return render(request,'add.html')
    def post(self,request):
        data = Subject()
        name = request.POST['name']
        amount = request.POST['amt']
        days = request.POST['day']
        assurance = request.POST['asc']
        remark = request.POST['ps']
        id = request.POST['solt']

        allInfo = []

        # 存入数据库
        data.name = name
        data.amount = amount
        data.days = days
        data.assurance = assurance
        data.remark = remark
        data.id =id
        data.save()

        allInfo.append(data)
        return render(request,'tips.html',{'allinfo':allInfo,'url':'/subject/','title':'添加成功'})

class ChangeView(View):
    def get(self,request):
        return render(request,'change.html')
    def post(self,request):
        return render(request,'subject.html')

class DetailView(View):
    def get(self,request,code):
        return render(request, 'detail.html')
    def post(self,request,code):
        info = Subject.objects.get(id=code)
        print(info)
        return render(request, 'detail.html', {'info': info})


