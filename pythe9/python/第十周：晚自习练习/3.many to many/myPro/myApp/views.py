from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication,Book
# Create your views here.
def index(request):

    # p1 = Publication.objects.create(pname = '大象出版社',paddress = '河南')
    # p2 = Publication.objects.create(pname = '北京大学出版社',paddress = '北京')
    # p3 = Publication.objects.create(pname = '清华大学出版社',paddress ='河北')
    #
    # b1 = Book.objects.create(bname = '海底两万里',bauthor = '赵四')
    # b2 = Book.objects.create(bname = '金银岛',bauthor = '李三')
    # b3 = Book.objects.create(bname = '无人生还',bauthor = '推理女王')
    # b4 = Book.objects.create(bname = '福尔摩斯探案集',bauthor = '柯南道尔')
    # b5 = Book.objects.create(bname = '堂吉诃德',bauthor = '六六')
    # b6 = Book.objects.create(bname = '雾都孤儿',bauthor = '赵六')
    #
    # b1.publication.add(p1,p2,p3)
    # b2.publication.add(p1,p2)
    # b3.publication.add(p1,p2)
    # b4.publication.add(p2,p3)
    # b5.publication.add(p1,p3)
    # b6.publication.add(p3)
    return HttpResponse('数据添加成功')

def select(request):

    # 根据书名来查询出版社
    b1 = Book.objects.get(bname = '无人生还')
    b1_allPublication = b1.publication.all()
    for pub in b1_allPublication:
        print(pub.pname)
        print(pub.paddress)

    b2 = Book.objects.get(bname ='雾都孤儿')
    b2_allPublication = b2.publication.all()
    for pub in b2_allPublication:
        print('---------')
        print(pub.pname)
        print(pub.paddress)
        print('--------')

    # 根据出版社来查找书名
    p1 = Publication.objects.get(pname = '北京大学出版社')
    all_book = p1.book_set.all()
    for book in all_book:
        print(book.bname)
        print(book.bauthor)

    p2 = Publication.objects.get(pname = '大象出版社')
    all_book = p2.book_set.all()
    for book in all_book:
        print('==============')
        print(book.bname)
        print(book.bauthor)
        print('==============')
    return HttpResponse('数据查询成功')