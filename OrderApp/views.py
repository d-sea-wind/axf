#coding=utf-8
from alipay import AliPay
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
# 下单页面
from CartApp.models import AxfCart
from CartApp.views import get_total_price
from OrderApp.models import AxfOrder, AxfOrderGoods
from axf.settings import APP_PRIVATE_KEY_STRING, ALIPAY_PUBLIC_KEY_STRING


def order_detail(request):
    # 获取order_id
    order_id = request.GET.get('order_id')
    order = AxfOrder.objects.get(pk=order_id)
    context = {
        'order': order,
        'total_price':order.axfordergoods_set.first().og_total_price
    }

    return render(request, 'axf/order/order_detail.html',context=context)


# 点击下单
def make_order(request):
    # 创建order对象-->为了ordergoods
    user_id = request.session.get('user_id')
    order = AxfOrder()
    order.o_user_id = user_id
    order.save()
    # 将购物车中选中的数据交给ordergoods的og_goods
    carts = AxfCart.objects.filter(c_user_id=user_id).filter(c_is_select=True)

    for cart in carts:
        # 创建ordergoods对象
        orderGoods = AxfOrderGoods()
        orderGoods.og_order = order
        orderGoods.og_goods = cart.c_goods
        orderGoods.og_goos_num = cart.c_goods_num
        orderGoods.og_total_price = get_total_price(user_id)
        orderGoods.save()

        cart.delete()

    data = {
        'msg': 'ok',
        'status': 200,
        'order_id': order.id
    }

    return JsonResponse(data=data)

# 支付
def testpay(request):
    alipay = AliPay(
        appid="2016101200665700",
        app_notify_url=None,  # 默认的通知路径
        app_private_key_string=APP_PRIVATE_KEY_STRING,
        # 支付宝公钥，不要使用自己的公钥！
        alipay_public_key_string=ALIPAY_PUBLIC_KEY_STRING,
        sign_type="RSA2",  #RSA 2
        debug=False  #FALSE(默认情况下)
    )

    subject = "兰蔻粉底"

    # 电脑网站支付，需要跳转到: https://openapi.alipaydev.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no="20161112",# 订单号
        total_amount=420,# 价格
        subject=subject,
        return_url="https://1000phone.com",
        notify_url="https://1000phone.com"  # 这个是可选择的
    )

    return redirect('https://openapi.alipaydev.com/gateway.do?' + order_string)