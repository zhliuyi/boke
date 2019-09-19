from django.db import models

# Create your models here.

class LoginUser(models.Model):
    #id不需要写
    email=models.EmailField()
    password=models.CharField(max_length=32)
    username=models.CharField(max_length=32,null=True,blank=True)
    phone_number=models.CharField(max_length=11,null=True,blank=True)
    photo=models.ImageField(upload_to="images",null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(null=True,blank=True,max_length=4)
    address=models.TextField(null=True,blank=True)
    #null针对数据库，表示可以为空，即在数据库的存储中可以为空
    #blank针对表单中该字段可以不填，但是对数据库没有影响