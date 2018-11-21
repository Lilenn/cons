from django.shortcuts import render
from  .models import People,Card
# Create your views here.
def index(request):

    # p1 = People(name = '大意',age=11 , sex=True)
    # p2 = People(name = '大耳',age=12 , sex=True)
    # p3 = People(name = '大伞',age=13 , sex=True)
    # p4 = People(name = '大寺',age=14 , sex=True)
    #
    # p1.save()
    # p2.save()
    # p3.save()
    # p4.save()
    #
    # c1 = Card(person=p3 , code='3333333' , address='地址3')
    # c2 = Card(person=p4 , code='4444444' , address='地址4')
    # c3 = Card(person=p2 , code='2222222' , address='地址2')
    # c4 = Card(person=p1 , code='1111111' , address='地址1')
    #
    # c1.save()
    # c2.save()
    # c3.save()
    # c4.save()

    return render(request,'first.html' ,{'content':'hello owrld'})

def select(request):

    c4 = Card.objects.get(address = '地址1')
    print(c4.code)
    print(c4.person.name)

    c3 = Card.objects.get(address = '地址2')
    print(c3.person.name)

    # 获取和card对象绑定的对象中的name字段
    c1 = Card.objects.get(person__name = '大伞')
    print(c1.address)

    # 获取和People对象绑定的对象中的address字段
    p1 = People.objects.get(card__address = '地址1')
    print(p1.name)

    return render(request,'first.html')

