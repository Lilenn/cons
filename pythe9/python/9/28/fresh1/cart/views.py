from django.shortcuts import render,redirect
from django.http import JsonResponse
from user.utils import login_requird
from cart.models import CartModel

# Create your views here.

@login_requird
def cart(request):
    '''购物车 '''
    user_id = request.session['user_id']
    carts = CartModel.objects.filter(user_id=user_id)

    return render(request,'cart/cart.html',{'carts':carts})


@login_requird
def add(request,goods_id,count):
    '''添加到购物车视图，接受两个参数'''
    user_id = request.session['user_id']

    # 查询购物车中是否已经有这个商品在这个人的名下，如过有的话，数量增加，如果没有，就在购物车中新建一个商品
    carts = CartModel.objects.filter(user_id=user_id,goods_id=goods_id)
    if len(carts) >= 1:
        cart = carts[0]
        cart.count = cart.count + count

    else:
        cart = CartModel()
        cart.user_id = user_id
        cart.goods_id = goods_id
        cart.count = count
    cart.save()

    return redirect('/cart/')


@login_requird
def delete(request,cart_id):
    '''从购物车中删除某个商品'''
    cart = CartModel.objects.get(id=cart_id)
    cart.delete()
    # 后端尽量不传给前端bool类型的数据，后端也不接受前端传来的bool类型
    return JsonResponse({'success':1})

@login_requird
def updata(request,cart_id,count):
    '''更新购物车内商品的数量'''
    cart = CartModel.objects.get(id=cart_id)
    cart.count = count
    cart.save()
    return JsonResponse({'success':1})