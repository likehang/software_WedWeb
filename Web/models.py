from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from datetime import datetime

class City(models.Model):# 检索用，存城市名，城市内公司数
    city_name = models.CharField(max_length=10,default='BeiJing')
    shop_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id) + self.city_name

class flag(models.Model):#检索用，存标签
    flag_name = models.CharField(max_length=6,default='null')

    def __str__(self):
        return self.flag_name

class business_choices(models.Model):#检索用，存公司类型 （简写，完整描述）
    ab_name = models.CharField(max_length=5,default='NULL')
    ex_name = models.CharField(max_length=15,default='expand_name')

    def __str__(self):
        return self.ex_name

class server_choices(models.Model):#检索用， 存服务类型（简写，完整描述）
    ser_name = models.CharField(max_length=5,default='NULL')
    ex_ser_name = models.CharField(max_length=15,default="expand_server'name")

    def __str__(self):
        return str(self.id) + self.ex_ser_name

class ident_Kind(models.Model):#身份认证类型
    ident_name=models.CharField(max_length=20)
    length = models.IntegerField()

    def __str__(self):
        return self.ident_name

class UserProfile(models.Model):#客户信息
    belong_to = models.OneToOneField(to=User)#名字密码等
    profile_image = models.FileField(upload_to='store/userimg',default='images/matt.jpg',null=True,blank=True)
    email = models.EmailField(null=True,blank = True)
    ident_name = models.CharField(max_length=12,default='',null=True,blank = True)
    sex_s = {
        ('man','man'),
        ('woman','woman'),
    }
    sex = models.CharField(choices = sex_s,default='man' ,max_length=5)
    location = models.ForeignKey(to=City,null=True,blank = True)
    ident_kind = models.ForeignKey(to=ident_Kind,default=1)
    phone = models.CharField(max_length=11,default='')
    is_ident = models.BooleanField(default=False)
    ident = models.CharField(max_length=18,null=True,blank = True)
    is_C_man = models.BooleanField(default=False)
    is_W_man = models.BooleanField(default=False)

    def __str__(self):
        return self.belong_to.username
    
class Company(models.Model):#存公司
    name = models.CharField(max_length=30 , default='unnamed_company')#名字
    business_kind =models.ForeignKey(to=business_choices)#公司类型
    icon = models.ImageField(upload_to='store/icon')#图标
    introduction = models.TextField(max_length=255,default='null')#介绍
    phone= models.CharField(max_length=20,default = 'null',blank=True,null=True)#联系电话
    adress = models.ForeignKey(to=City)#所在城市
    ident = models.BooleanField(default = False)#审核状态
    isopen = models.BooleanField(default = False)#营业状态
    inward_phone = models.CharField(max_length=20)#内部电话
    manager = models.OneToOneField(to=UserProfile,blank=True,null=True)
    charge_time = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class C_S(models.Model):#存服务 
    belong = models.ForeignKey(to=Company)#所属公司
    topic = models.CharField(max_length=30 , default='unnamed_S|C')#主题
    public_like = models.PositiveIntegerField(default=0)#喜好程度
    icon = models.ImageField(upload_to='store/icon')#图标
    introduction = models.TextField(max_length=255,default='null')#介绍
    index_flag = models.CharField(max_length=20,default='',null=True,blank = True)
    service_kind = models.ForeignKey(to=server_choices)#服务种类
    minprice = models.DecimalField(max_digits=8,decimal_places=2,default = 0,null=True,blank=True)#价格999999.99
    maxprice = models.DecimalField(max_digits=8,decimal_places=2,default = 0,null=True,blank=True)#价格999999.99
    detail = models.TextField(max_length=255,default='null',null=True,blank = True)#细节参数
    create_time = models.DateField(auto_now_add=True)#创建日期
    graph_count = models.IntegerField(default=0)#包含图片数
    writed_time = models.DateField(auto_now=True)#修改日期

    def __str__(self):
        return self.topic

class Graph(models.Model):#服务例图
    belong = models.ForeignKey(to=C_S)#所属服务
    order_number = models.PositiveIntegerField(default=1)#图片顺序
    img = models.ImageField(upload_to='store/img')#存储的图
    flag = models.CharField(max_length=20,default='null')

    def __str__(self):
        return self.belong.topic+' '+ str(self.order_number)

class status(models.Model):#订单状态及下阶段
    status_level = models.IntegerField()
    status_name = models.CharField(max_length=10)
    next_1 = models.IntegerField(null=True,blank = True)
    next_2 = models.IntegerField(null=True,blank = True)

    def __str__(self):
        return str(self.status_level)+''+str(self.status_name)

class Order_list(models.Model):#存订单
    Username = models.ForeignKey(to=UserProfile)#用户名
    create_time=models.DateField(auto_now_add=True)#订单生成时间
    needlist = models.ForeignKey(to = C_S)#需要的服务
    status = models.ForeignKey(to = status , default=1)
    price = models.DecimalField(max_digits=8,decimal_places=2,default = 0,null=True,blank=True)#价格999999.99

    def __str__(self):
        return str(self.create_time)+' '+str(self.id)

class Fav(models.Model):#收藏
    fav_user = models.ForeignKey(to=UserProfile)
    fav_ser = models.ForeignKey(to = C_S)

    def __str__(self):
        return self.fav_user.belong_to.username