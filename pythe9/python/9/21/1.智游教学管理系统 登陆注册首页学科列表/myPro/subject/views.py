from django.shortcuts import render,redirect,render_to_response
from django.views import View
from .models import SubjectModel
from user.models import UserModel
from django.contrib.auth.decorators import login_required
# 导入类视图装饰器/
from django.utils.decorators import method_decorator
# Create your views here.

# render 和 render_to_response 区别：
# render把request作为参数直接传给了html页面，
# render_to_response里不能使用全局对象request里面的属性

def index(request):
    # print(dir(request))
    if request.method == 'POST':
        # 处理post请求
        pass
    subjects = SubjectModel.objects.all()
    return render(request, 'subject/home.html', {'subjects': subjects})

class SubjectList(View):
    # 类视图这样写
    @method_decorator(login_required)
    def get(self,request):
        # 根据number排序
        subjects = SubjectModel.objects.all().order_by('number')
        return render(request,'subject/home.html',{'subjects':subjects})
    def post(self,request):
        return render(request,'subject/home.html')

class DetailView(View):
    def get(self,request):
        # if request.user is None:
        #     return redirect('login')
        subject_id = request.GET['subject_id']
        subject = SubjectModel.objects.get(id = subject_id)
        if subject.creater and subject.updater:
            user = UserModel.objects.get(id=subject.creater)
            user1 = UserModel.objects.get(id=subject.updater)
            return render_to_response('subject/detail.html',{'subject':subject,'user':user,'user1':user1})
        else:
            return render_to_response('subject/detail.html',{'subject':subject})

class EditView(View):
    @method_decorator(login_required)
    def get(self,request):
        subject_id = request.GET['subject_id']
        subject = SubjectModel.objects.get(id=subject_id)
        return render_to_response('subject/edit.html',{'subject':subject})
    def post(self,request):
        subject_id = request.POST['subject_id']
        name = request.POST['name']
        amount = request.POST['amount']
        days = request.POST['days']
        number = request.POST['number']
        assurance = request.POST['assurance']
        remark = request.POST['remark']
        user = request.user
        subject = SubjectModel.objects.get(id=subject_id)
        if subject:
            subject.name = name
            subject.amount = amount
            subject.days = days
            subject.assueance = assurance
            subject.remake = remark
            subject.number = number
            subject.updater = user.id
            subject.save()
        return redirect('/subject/')

class AddView(View):
    def get(self,request):
        return render(request,'subject/add.html')
    def post(self,request):

        name = request.POST['name']
        amount = request.POST['amount']
        days = request.POST['days']
        number = request.POST['number']
        assurance = request.POST['assurance']
        remark = request.POST['remark']

        # 把request里面的user赋值给自定义的user
        user = request.user

        subject = SubjectModel()
        subject.name = name
        subject.amount = amount
        subject.days = int(days)
        subject.number = int(number)
        subject.assueance = assurance
        subject.remake = remark

        subject.creater = user.id

        subject.save()

        return redirect('/subject/')

class Delete(View):
    def get(self,request):
        subject_id = request.GET['subject_id']
        subject = SubjectModel.objects.get(id=subject_id)
        user = request.user
        print(user.id)
        print('=========')
        print(subject.creater)
        # 比较登录用户和创建者是否是同一人
        if subject and subject.creater == user.id:
            print('++++++++++++')
            subject.delete()
        return redirect('/subject/')
