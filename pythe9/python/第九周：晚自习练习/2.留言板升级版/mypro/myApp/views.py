from django.shortcuts import render,reverse
import requests
# Create your views here.
from .models import Message
from django.http import HttpResponse
def add(request):
    # 如果请求方式四GET 那么当前网页是通过在浏览器中输入网址
    # 进来的
    if request.method == 'GET':
        # reverse()函数可以对url进行反向映射
        # 之前是通过url地址找到指定的网页
        # 现在通过reverse()函数根据url名字来找到url地址
        # add为urls.py中写到的url的name值
        url = reverse('add')
        return render(request,'add.html',{'url':url})
    elif request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        message = request.POST['message']

        message_model = Message()
        message_model.m_name=name
        message_model.m_email = email
        message_model.m_address = address
        message_model.m_message = message

        message_model.save()

        allinfo =Message.objects.all()
        return render(request,'showall.html',{'allinfo':allinfo})
def showAll(request):
    allinfo = Message.objects.all()
    return render(request,'showall.html',{'allinfo':allinfo})
def update(request):
    # 如果通过修改按钮或者通过网址的方式进入的更新页面
    # 那么默认进入页面的请求方式为get
    if request.method=='GET':
        url=reverse('update')
        return render(request,'update.html',{'url':url})
    elif request.method == 'POST':
        _id = request.POST['id']
        m_name = request.POST['name']
        m_email = request.POST['email']
        m_address = request.POST['address']
        m_message = request.POST['message']
        message_update = Message.objects.get(m_id=_id)
        message_update.m_name = m_name
        message_update.m_email = m_email
        message_update.m_addess = m_address
        message_update.m_message=m_message
        message_update.save()

        return HttpResponse('修改成功')
def select(request):
    if request.method=='GET':
        url =reverse('select')
        return render(request,'select.html',{'url':url})
    elif request.method=='POST':
        id_num=request.POST['id']
        message_select = Message.objects.get(m_id=id_num)
        return render(request,'select.html',{'message_select':message_select})
def delate(request):
   if request.method == 'GET':
       url = reverse('delate')
       return render(request,'delate.html',{'url':url})
   elif request.method == 'POST':
       name = request.POST['name']
       message_delate = Message.objects.filter(m_name=name)
       message_delate.delete()
       return HttpResponse('删除成功')