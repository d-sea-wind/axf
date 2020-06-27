#coding=utf-8
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from CartApp.models import AxfCart


# 定义计算总计的方法
def get_total_price(user_id):
    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)
    total_price = 0
    for cart in carts:
        total_price = total_price + cart.c_goods_num * cart.c_goods.price
    return '%.2f' % total_price

def cart(request):
    # 获取session中的user_id
    user_id = request.session.get('user_id')
    # 登录帐号后跳转到购物车页面
    if user_id:
        # 查找当前登录的用户的购物车
        carts = AxfCart.objects.filter(c_user_id=user_id)
        # 当前用户存在没选中的商品取反 ===> 全选
        is_all_select = not AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=False).exists()
        context = {
            'carts': carts,
            'total_price': get_total_price(user_id),
            'is_all_select': is_all_select,
        }
        return render(request, 'axf/main/cart/cart.html', context=context)
    else:
        # 没登录跳转到登录页面
        return redirect(reverse('axfuser:login'))

# 闪购页面中将商品添加购物车
def addToCart(request):
    # 获取session中的user_id
    user_id = request.session.get('user_id')
    data = {
        'msg': 'ok',
        'status': 200
    }
    # 判断是否登录
    if user_id:
        # 获取goodsid
        goodsid = request.GET.get('goodsid')
        # user_id和goodsid联合查询
        carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_goods_id=goodsid)
        if carts.count() > 0:
            cart = carts.first()
            cart.c_goods_num = cart.c_goods_num + 1
        else:
            cart = AxfCart()
            cart.c_goods_id = goodsid
            cart.c_user_id = user_id
        cart.save()
        data['c_goods_num'] = cart.c_goods_num
    else:
        data['msg'] = '未登录'
        data['status'] = 201
    return JsonResponse(data=data)

# 闪购页面中将商品数量减一
def subToCart(request):
    # 获取session中的user_id
    user_id = request.session.get('user_id')
    data = {
        'msg': 'ok',
        'status': 200
    }
    # 判断是否登录
    if user_id:
        # 获取goodsid
        goodid = request.GET.get('goodid')
        # user_id和goodsid联合查询
        carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_goods_id=goodid)
        if carts.count() > 0:
            cart = carts.first()
            cart.c_goods_num = cart.c_goods_num - 1
            data['c_goods_num'] = cart.c_goods_num
            cart.save()
            if cart.c_goods_num == 0:
                cart.delete()
    else:
        data['msg'] = '未登录'
        data['status'] = 201
    return JsonResponse(data=data)

# 购物车页面中将商品数量加一
@csrf_exempt
def addCart(request):
    data = {
        'msg': 'ok',
        'status': 200,
    }
    # 获取js中$.post中的cartid
    cartid = request.POST.get('cartid')
    # 获取数据库cart对象
    cart = AxfCart.objects.get(pk=cartid)

    cart.c_goods_num = cart.c_goods_num + 1
    cart.save()
    data['c_goods_num'] = cart.c_goods_num

    # 获取session中的user_id
    userid = request.session.get('user_id')
    data['total_price'] = get_total_price(userid)
    return JsonResponse(data=data)

# 购物车页面中将商品数量减一或从购物车中删除
@csrf_exempt
def subCart(request):
    data = {
        'msg': 'ok',
        'status': 200,
    }
    # 获取js中$.post中的cartid
    cartid = request.POST.get('cartid')
    # 获取数据库cart对象
    cart = AxfCart.objects.get(pk=cartid)
    # 商品数量大于1
    if cart.c_goods_num > 1:
        cart.c_goods_num = cart.c_goods_num - 1
        cart.save()
        data['c_goods_num'] = cart.c_goods_num
    else:
        # 商品数量等于1,删除
        cart.delete()
        data['status'] = 204
    # 获取session中的user_id
    userid = request.session.get('user_id')
    data['total_price'] = get_total_price(userid)

    return JsonResponse(data=data)

# 点击✔ 改变选中状态
def changeStatus(request):
    data = {
        'msg': 'ok',
        'status': 200
    }
    # 获取cart.js中的cartid
    cartid = request.GET.get('cartid')
    cart = AxfCart.objects.get(pk=cartid)
    # 点击以下去反
    cart.c_is_select = not cart.c_is_select
    cart.save()

    data['c_is_select'] = cart.c_is_select
    # 获取session中的user_id
    user_id = request.session.get('user_id')
    # 当前用户存在没选中的商品取反 ===> 全选
    is_all_select = not AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=False).exists()
    data['is_all_select'] = is_all_select
    # 总价
    data['total_price'] = get_total_price(user_id)

    return JsonResponse(data=data)

# 全选
def allSelect(request):
    # 获取cart.js中cartidlist
    cartidlist = request.GET.get('cartidlist')
    # 按照#进行分割
    cartid_list = cartidlist.split('#')
    # 按照列表中的cartid查询
    carts = AxfCart.objects.filter(id__in=cartid_list)
    # 获取session的user_id的值
    user_id = request.session.get('user_id')

    data = {
        'msg': 'ok',
        'status': 200,
    }

    for cart in carts:
        cart.c_is_select = not cart.c_is_select
        cart.save()

    data['total_price'] = get_total_price(user_id)

    return JsonResponse(data=data)
