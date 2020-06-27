#coding=utf-8
from django.shortcuts import render

# Create your views here.
from MarketApp.models import AxfFoodType, AxfGoods
from MarketApp.view_helper import ORDER_RULE_DEFAULT, ORDER_RULE_PRICE, ORDER_RULE_DESC, ORDER_RULE_NUM_ASC, \
    ORDER_RULE_NUM_DESC


def market(request):
    # 食物类型(左边的导航栏)
    foodtypes = AxfFoodType.objects.all()

    # 获取页面参数typeid
    typeid = request.GET.get('typeid', '104749')

    # 获取axf_foodtype的childtypenames字段
    childtypenames = AxfFoodType.objects.filter(typeid=typeid)[0].childtypenames
    # 全部分类:0#酸奶乳酸菌:103537#牛奶豆浆:103538#面包蛋糕:103540

    # 分割
    childtype_list = childtypenames.split('#')

    typename_list = []

    # 遍历
    for childtype in childtype_list:
        # 分割
        typename = childtype.split(':')
        # 拿到类似['全部分类','0']
        typename_list.append(typename)

    # 获取数据库中关于导航栏中的食物
    good_list = AxfGoods.objects.filter(categoryid=typeid)

    # 获取页面二级联动参数childcid
    childcid = request.GET.get('childcid',ORDER_RULE_DEFAULT)

    # 判断good_list中关于childcid的食物且childcid不等于'0'
    if childcid != ORDER_RULE_DEFAULT:
        good_list = good_list.filter(childcid=childcid)

    sort_list = [
        ['综合排序',ORDER_RULE_DEFAULT],
        ['销量升序',ORDER_RULE_NUM_ASC],
        ['销量降序',ORDER_RULE_NUM_DESC],
        ['价格升序',ORDER_RULE_PRICE],
        ['价格降序',ORDER_RULE_DESC]]

    # 获取页面中三联联动参数num
    num = request.GET.get('num',ORDER_RULE_DEFAULT)

    # 判断num值
    # 综合排序
    if num == ORDER_RULE_DEFAULT:
        good_list = good_list
    elif num == ORDER_RULE_NUM_ASC:
        # 销量升序
        good_list = good_list.order_by('productnum')
    elif num == ORDER_RULE_NUM_DESC:
        # 销量降序
        good_list = good_list.order_by('-productnum')
    elif num == ORDER_RULE_PRICE:
        # 价格升序
        good_list = good_list.order_by('price')
    else:
        # 价格降序
        good_list = good_list.order_by('-price')


    context = {
        'foodtypes': foodtypes,
        'good_list': good_list,
        'typeid': typeid,
        'typename_list': typename_list,
        'childcid': childcid,
        'sort_list': sort_list,
        'num': num
    }

    return render(request, 'axf/main/market/market.html', context=context)
