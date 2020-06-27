#coding=utf-8
from django.shortcuts import render

# Create your views here.
from HomeApp.models import AxfWheel, AxfNav, AxfMustBuy, AxfMainShow


def home(request):
    # 轮播图
    wheels = AxfWheel.objects.all()
    # 导航
    navs = AxfNav.objects.all()
    # 必购
    mustbuys = AxfMustBuy.objects.all()
    # 主要展示
    mainshows = AxfMainShow.objects.all()

    return render(request,'axf/main/home/home.html',context=locals())

