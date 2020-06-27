#coding=utf-8
from django.core.mail import send_mail
from django.template import loader


def send_email(name,email,token):
    # 主题
    subject = '红浪漫洗浴'
    # 发送不含html标签的内容
    message = '充值1000送免费洗澡一次'
    context = {
        'name': name,
        'url': 'http://127.0.0.1:8000/axfuser/activeAccount/?token='+str(token),
    }
    # 发送含html标签的内容(发送这个内容，上面的message失效)
    html_message = loader.get_template('active.html').render(context=context)
    from_email = '17855370071@163.com'
    recipient_list = [email]
    # message即使这个失效，但是还是占个坑位
    send_mail(subject=subject, message=message, html_message=html_message, from_email=from_email,
              recipient_list=recipient_list)