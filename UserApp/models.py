#coding=utf-8
from django.db import models

# Create your models here.
class AxfUser(models.Model):
    u_name = models.CharField(max_length=128)
    u_password = models.CharField(max_length=256)
    u_email = models.CharField(max_length=64)
    # 图片
    u_icon = models.ImageField(upload_to='icons')
    # u_token
    u_token = models.CharField(max_length=256)
    # 邮箱激活
    u_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'axf_user'
