#coding=utf-8
from django.conf.urls import url


from CartApp import views

urlpatterns = [
    url(r'cart/',views.cart,name='cart'),
    # 闪购页面中添加商品到购物车
    url(r'^addToCart/',views.addToCart,name='addToCart'),
    # 闪购页面中将商品数量减一
    url(r'^subToCart/',views.subToCart,name='subToCart'),

    # 购物车页面中将商品数量加一
    url(r'^addCart/',views.addCart,name='addCart'),
    # 购物车页面中将商品数量减一或从购物车中删除
    url(r'^subCart/',views.subCart,name='subCart'),

    # 点击✔ 改变选中状态
    url(r'changeStatus/',views.changeStatus,name='changeStatus'),
    # 全选
    url(r'^allSelect/', views.allSelect, name='allSelect'),
]