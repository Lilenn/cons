from django.shortcuts import render,HttpResponse,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .form import LoginForm,UserRegistrationForm,ProfileEditForm,UserEditForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import Profile,Contact
from django.contrib import messages
from django.http import JsonResponse
from action.utils import create_action
from action.models import Action
from myapp.models import Contact

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form  = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd["username"],
                                password = cd["password"])
            if user is None:
                return HttpResponse('登陆失败')
            else:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('登陆验证成功')
                else:
                    return HttpResponse('您的用户被禁用，请联系管理员解封。')

    else:
        form = LoginForm()
        return render(request,'mypro/login.html',{"form":form})

@login_required
def dashboard(request):
    #默认展示所有行为，不包含当前用户
    actions = Action .objects.exclude(user=request.user)
    # 关注的用户id列表
    following = Contact.objects.filter(user_from=request.user)
    following_ids = [user_to.id for user_to in following]
    if following_ids:
        #如果当前用户有关注的用户，展示被关注用户的行为
        actions = actions.filter(user_id__in=following_ids)
    actions = actions[:10]
    return render(request,"mypro/dashboard.html",{"section":"dashboard","actions":actions})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # 建立新数据对象，但是不写入数据库
            new_user = user_form.save(commit=False)
            # 设置密码
            new_user.set_password(user_form.cleaned_data['password'])
            # 保存user对象
            new_user.save()
            Profile.objects.create(user=new_user)
            create_action(new_user,'创建了新用户')
            return render(request,'mypro/register_done.html',{"new_user":new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'mypro/register.html',{"user_form":user_form})


@login_required
def edit(request):
    if request.method =='POST':
        # instance 指定对象是数据库中的当前登陆用户的那一行数据对象，如果不指定，那么就会新建记录而不是更新记录
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'个人信息修改成功')
        else:
            messages.error(request, '个人信息更新失败')
    else:
        user_form = UserEditForm()
        profile_form = ProfileEditForm()
    return render(request,'mypro/edit.html',{"user_form":user_form,
                                             "profile_form":profile_form})

@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request,'mypro/user_list.html',{"users":users,"section":'users'})

@login_required
def user_detail(request,username):
    user = get_object_or_404(User,username=username,is_active=True)
    contacts = Contact.objects.filter(user_to=user)
    followers = [ contact.user_from for contact in contacts]
    total_followers = len(followers)
    return render(request,'mypro/user_detail.html',{"user":user,"section":"users",
                                                    "followers":followers,
                                                    "total_followers":total_followers})

@login_required
@require_POST
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')

    if user_id and action:
        user = User.objects.get(id=user_id)
        if action == 'follow':
            Contact.objects.get_or_create(user_from=request.user,user_to=user)
            create_action(request.user,'关注了用户',user)
        else:
            Contact.objects.filter(user_from=request.user,user_to=user).delete()

        return JsonResponse({"status":'ok'})
    return JsonResponse({"status":'error'})