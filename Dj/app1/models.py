from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class userinfo(models.Model):
    '''用户信息'''
    name = models.CharField(max_length=32, verbose_name="用户名称")
    pswd = models.CharField(max_length=64, verbose_name="用户密码")
    power = models.CharField(max_length=64, verbose_name="用户权限")
    class Meta:
        verbose_name_plural = '用户'
        verbose_name = "基本信息"
    def __str__(self):
        return self.name

class newmap(models.Model):
    '''图像基本信息'''
    imgdata = models.CharField(max_length=512,verbose_name="图像名称", blank=True)
    timdata = models.DateField(auto_now=False,verbose_name="检测时间")
    mapdata = models.CharField(max_length=512,verbose_name="图像地点", blank=True)
    class Meta:
        verbose_name_plural = '图像'
        verbose_name = "基本信息"
    def __str__(self):
        return self.imgdata

class imgout(models.Model):
    '''图像详细信息'''
    im = models.OneToOneField(newmap,on_delete=models.CASCADE)
    d1 = models.CharField(max_length=512, verbose_name="1类", default="0", blank=True)
    d2 = models.CharField(max_length=512, verbose_name="2类", default="0", blank=True)
    class Meta:
        verbose_name_plural = '详细信息'
        verbose_name = "图像名称"
    def __str__(self):
        return self.im.imgdata

class historyevent(models.Model):
    devid = models.CharField(max_length=256)
    maskinfo = models.CharField(max_length=256)
    evtime = models.CharField(max_length=256)
    hashcode = models.CharField(max_length=256)
    level = models.CharField(max_length=256)
    des = models.CharField(max_length=256)
    def __str__(self):
        return self.devid