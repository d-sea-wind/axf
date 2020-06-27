#coding=utf-8
import re
import uuid

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache

from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.utils.six import BytesIO

from UserApp.models import AxfUser

from UserApp.view_constaint import send_email



from axf import settings

# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'axf/user/register.html')
    if request.method == 'POST':
        # 读取页面中的用户注册信息
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # FILES用于接受二进制(图片)
        icon = request.FILES.get(('icon'))
        # 产生token
        token = uuid.uuid4()
        # 后台对密码加密
        password = make_password(password)

        # 用户注册信息存入数据库
        user = AxfUser()
        user.u_name = name
        user.u_password = password
        user.u_email = email
        user.u_icon = icon
        user.u_token = token
        # 保存数据
        user.save()
        # token的生存时间设置
        cache.set(token, user.id, timeout=1800)
        # 邮箱激活
        send_email(name, email, token)

        return redirect(reverse('axfuser:login'))


# 用户名字的后台验证
def checkName(request):
    # 获取js中name的值(就是页面文本框的内容)
    name = request.GET.get('name')
    # 获取数据库中的u_name的对象
    users = AxfUser.objects.filter(u_name=name)
    data = {
        'msg': '✔用户名字可以使用',
        'status': 200
    }
    if users.count() > 0:
        data['msg'] = '❌用户名字已经存在'
        data['status'] = 201
    return JsonResponse(data=data)


# 测试邮箱发送邮件(只做测试用)
def testmial(request):
    # 主题
    subject = '红浪漫洗浴'
    # 发送不含html标签的内容
    message = '充值1000送免费洗澡一次'
    context = {
        'name': '强',
        'url': 'https://www.baidu.com',
    }
    # 发送含html标签的内容(发送这个内容，上面的message失效)
    html_message = loader.get_template('active.html').render(context=context)
    from_email = '17855370071@163.com'
    recipient_list = ['17855370071@163.com']
    # message即使这个失效，但是还是占个坑位
    send_mail(subject=subject, message=message, html_message=html_message, from_email=from_email,
              recipient_list=recipient_list)

    return HttpResponse('ok')


# 激活账号
def activeAccount(request):
    # 获取激活时的token
    token = request.GET.get('token')
    # cache.set(token,user.id,timeout=60) 中对比token,有效返回user.id
    user_id = cache.get(token)
    # 判断user_id对象是否存在
    if user_id:
        user = AxfUser.objects.get(pk=user_id)
        user.u_active = True
        user.save()
        # 删除token防止多次激活
        cache.delete(token)
        return HttpResponse('激活成功')
    else:
        return HttpResponse('邮件已过期，请重新发送请求')

    # # 查询数据库中的u_token的对象
    # users = AxfUser.objects.filter(u_token=token)
    # # 判断该对象是否存在
    # if users.exists():
    #     user = users.first()
    #     user.u_active = 1
    #     user.save()
    #     return HttpResponse('激活成功')
    # else:
    #     return HttpResponse('哪凉快哪待着,你个负心汉，你是个假数据，你个骗子.')


def login(request):
    if request.method == 'GET':
        return render(request,'axf/user/login.html')
    if request.method == 'POST':
        # 用户输入的验证码
        imgcode = request.POST.get('imgcode')
        # 所有的验证码生成策略都会把验证码的值绑定到session上
        verify_code = request.session.get('verify_code')
        # 用正则来匹配验证码
        b = re.search(imgcode,verify_code,re.I)
        # 判断验证码是否正确
        if b:
            name = request.POST.get('name')
            users = AxfUser.objects.filter(u_name=name)
            # 验证用户名
            if users.count()>0:
                user = users.first()
                password = request.POST.get('password')
                # 验证密码
                if check_password(password,user.u_password):
                    # 验证激活状态
                    if user.u_active == True:
                        # 注意 session可以不可以绑定对象。
                        request.session['user_id'] = user.id
                        return redirect(reverse('axfmine:mine'))
                    else:
                        msg = '用户未激活'
                        context = {
                            'msg': msg
                        }
                        return render(request, 'axf/user/login.html', context=context)
                else:
                    msg = '密码错误'
                    context = {
                    'msg': msg
                    }
                    return render(request, 'axf/user/login.html', context=context)

            else:
                msg = '用户不存在'
                context = {
                    'msg':msg
                }
                return render(request,'axf/user/login.html',context=context)
        else:
            msg = '验证错误'
            return render(request,'axf/user/login.html',context=locals())

# 验证码
def get_code(request):
    # 初始化画布，初始化画笔
    mode = "RGB"
    size = (200, 100)
    red = get_color()
    green = get_color()
    blue = get_color()
    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)
    imagedraw = ImageDraw(image, mode=mode)
    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)
    verify_code = generate_code()
    request.session['verify_code'] = verify_code
    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50 * i, 0), text=verify_code[i], font=imagefont, fill=fill)
    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)
    fp = BytesIO()
    image.save(fp, "png")
    return HttpResponse(fp.getvalue(), content_type="image/png")

import random
def get_color():
    return random.randrange(256)

def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
    code = ""
    for i in range(4):
        code += random.choice(source)
    return code

# 退出
def logout(request):
    request.session.flush()
    return redirect(reverse('axfmine:mine'))