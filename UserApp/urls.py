#coding=utf-8
from django.conf.urls import url

from UserApp import views

urlpatterns = [
    # 注册
    url(r'^register/',views.register,name='register'),
    # 用户名验证
    url(r'^checkName/',views.checkName),
    #  测试邮箱发送邮件(只做测试用)
    url(r'^testmail/',views.testmial),
    # 激活账号
    url(r'^activeAccount/',views.activeAccount),
    # 登录
    url(r'^login/',views.login,name='login'),
    # 验证码
    url(r'^get_code/',views.get_code),
    # 退出
    url(r'^logout/',views.logout,name='logout')
]