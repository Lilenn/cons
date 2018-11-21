from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Publication,Book
def add(request):

    # p1 = Publication(pname = "大象出版社",paddress='河南')
    # p2 = Publication(pname='北京大学出版社',paddress='北京')
    # p3 = Publication(pname='清华大学出版社',paddress='河北')
    #
    # p1.save()
    # p2.save()
    # p3.save()
    #
    # b1 = Book(bname='海底两万里',bauthor='赵四')
    # b2 = Book(bname='金银岛',bauthor='李三')
    # b3 = Book(bname='无人生还',bauthor='推理女王')
    # b4 = Book(bname='福尔摩斯探案集',bauthor='柯南道尔')
    # b5 = Book(bname='堂吉诃德',bauthor='六六')
    # b6 = Book(bname='雾都孤儿',bauthor='赵六')
    #
    # b1.save()
    # b2.save()
    # b3.save()
    # b4.save()
    # b5.save()
    # b6.save()
    #
    # b1.publication.add(p1,p2,p3)
    # b2.publication.add(p1,p2)
    # b3.publication.add(p1,p2)
    # b4.publication.add(p2,p3)
    # b5.publication.add(p1,p3)
    # b6.publication.add(p3)

    # 多对多关系，两个表不直接产生联系
    # 而是将两个表之间的关系记录在中间表上
    # 中间表无需创建，自动生成

    return HttpResponse('添加数据成功')

def select(request):

    b1 = Book.objects.get(bname = '福尔摩斯探案集')
    # 获取上边书籍的所有出版社
    b1_allpublication = b1.publication.all()
    for pub in b1_allpublication:
        print(pub.pname)
        print(pub.paddress)

    # 通过出版社查找书籍
    p1 = Publication.objects.get(pname = '清华大学出版社')
    all_book = p1.book_set.all()
    for book in all_book:
        print('--========')
        print(book.bname)
        print(book.bauthor)
    return HttpResponse('查询成功')