#coding=utf-8
from django.conf.urls import url

from OrderApp import views

urlpatterns = [
    # 点击下单
    url(r'^make_order/',views.make_order,name='make_order'),
    # 下单页面
    url(r'^order_detail/',views.order_detail,name='order_detail'),
    # 支付
    url(r'^testpay/',views.testpay,name='testpay')
]