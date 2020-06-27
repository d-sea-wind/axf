#coding=utf-8
from django.db import models

# Create your models here.
from MarketApp.models import AxfGoods
from UserApp.models import AxfUser


class AxfOrder(models.Model):
    # 关联用户表的用户id
    o_user = models.ForeignKey(AxfUser)
    # 下单时间
    o_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'order'

class AxfOrderGoods(models.Model):
    # 关联订单表o_order
    og_order =  models.ForeignKey(AxfOrder)
    # 关联商品表axfgoods
    og_goods = models.ForeignKey(AxfGoods)
    # 商品数量
    og_goos_num = models.IntegerField()
    # 订单商品总价
    og_total_price = models.FloatField()
    class Meta:
        db_table = 'ordergoods'
