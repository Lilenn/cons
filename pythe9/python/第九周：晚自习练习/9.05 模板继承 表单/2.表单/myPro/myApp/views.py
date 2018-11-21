from django.shortcuts import render
from django.http import HttpResponse
from .forms import SumForm
# Create your views here.
def index(request):
    form = SumForm()
    return  render(request ,'index.html',{'form':form})

def add_form(request):
   if request.method == 'GET':
       # get方法获取表单的值，可以通过GET['XX']这种方式
       # IntegerField() 只接受数字类型 这种类型才是合法的
       # json['data']
       firstValue = request.GET['a1']
       secondValue = request.GET['b1']
       return HttpResponse(int(firstValue) + int(secondValue))
   else :
       # firstValue = request.POST['a1']
       # secondValue = request.POST['b1']
       # return HttpResponse(firstValue + secondValue)
       # 初始化一个forms对象 并且获取请求方式和请求内容
       form = SumForm(request.POST)
       # valid 可用;合法
       if form.is_valid():
           firstValue = form.cleaned_data['a1']
           secondValue = form.cleaned_data['b1']
           return HttpResponse(int(firstValue) + int(secondValue))
       else :
           # return HttpResponse('内容不合法')
           return render(request, 'index.html')


