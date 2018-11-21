from django.shortcuts import render

from goods.models import CategoryModel, CategoryGoodsModel, GoodsModel
from cart.models import CartModel
# Create your views here.


def index(request):
    """主页"""
    # 拿出所有的分类
    category_list = CategoryModel.objects.all()
    # 分别取出分类下的最新的商品
    new_goods_dict = {} # 存储每个分类下的最新的商品
    for category in category_list:
        goods_list = CategoryGoodsModel.objects.filter(category_id=category.id).order_by("-goods_id")[:4]
        # 拿到查询出的所有的goods的id
        goods_ids = [goods.goods_id for goods in goods_list]
        print(goods_ids)
        goods_info_list = GoodsModel.objects.filter(id__in=goods_ids)
        print(goods_info_list)
        new_goods_dict[category] = goods_info_list

    # 从session中拿到user的id
    user_id = request.session.get("user_id", 0)
    cart_list = CartModel.objects.filter(user_id=user_id)
    cart_count = 0
    # 统计出购物车中所有的商品数量
    for cart in cart_list:
        cart_count += cart.count

    context = {
        "new_goods_dict": new_goods_dict,
        "cart_count": cart_count
    }
    print(context)
    return render(request, "goods/index.html", context)
