from django.shortcuts import render,reverse
from  .models import Message
from django.http import HttpResponse
# Create your views here.
def add(request):
    # 如果请求方式是get，那么当前网页是通过在浏览器中输入网址进来的
    if request.method == 'GET':
        # reverse函数可以对url进行反向映射
        # 之前是通过url地址找到指定网页
        # 现在是通过reverse函数根据url名字来找到url地址
        # add为urls.py中写道的url的name值
        url = reverse('add')
        return render(request , 'add.html',{'url':url})
    elif request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        message = request.POST['message']

        message_modle = Message()
        message_modle.m_name = name
        message_modle.m_email = email
        message_modle.m_address = address
        message_modle.m_message = message

        message_modle.save()
        allInfo = Message.objects.all()
        return render(request , 'showAll.html',{'allInfo':allInfo})

def showAll(request):
    allInfo = Message.objects.all()
    return render(request,'showAll.html',{'allInfo':allInfo})

def updata(request):
    # 如果通过修改按钮或者通过网址的方式进入更新的页面
    # 那么默认进入页面的请求方式为get
    if request.method == 'GET':
        url = reverse('updata')
        return render(request,'updata.html',{'url':url})
    elif request.method == 'POST':

        _id = request.POST['id']
        m_name = request.POST['name']
        m_email = request.POST['email']
        m_address  = request.POST['address']
        m_message = request.POST['message']

        message_updata = Message.objects.get(m_id = _id)
        message_updata.m_name = m_name
        message_updata.m_email = m_email
        message_updata.m_address = m_address
        message_updata.m_message = m_message

        message_updata.save()

        return HttpResponse('更新成功')
def delete(request):
    if request.method == 'GET':
        url = reverse('delete')
        return render(request,'delete.html',{'url':url})
    elif request.method == 'POST':
        d_id = request.POST['id']

        Message.objects.get(m_id = d_id).delete()

        return HttpResponse('删除成功')

