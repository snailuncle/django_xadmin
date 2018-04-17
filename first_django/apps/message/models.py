from django.db import models

# Create your models here.
#数据库中的名称 message_usermessage
class UserMessage(models.Model):
    object_id=models.CharField(max_length=50,default='',primary_key=True,verbose_name='主键')
    name=models.CharField(max_length=20,null=True,blank=True,default='',verbose_name='用户名')
    email=models.EmailField(verbose_name='邮箱')
    address=models.CharField(max_length=100,verbose_name='联系地址')
    message=models.CharField(max_length=500,verbose_name="留言信息")

    class Meta:
        verbose_name="用户留言信息"
        # db_table='user_message'
        #排序
        # ordering='-object'
        #复数
        verbose_name_plural=verbose_name
