from django.db import models

# Create your models here.
class Message(models.Model):
    # 设置一个自动增长的id作为主键
    m_id=models.AutoField(primary_key=True)
    # textfield和charfield都是文本样式基本上没有太大差别
    # 不过textfiled理论上是无线的
    # charfield需要指明长度
    m_name = models.TextField()
    m_email= models.CharField(max_length=200)
    m_address=models.CharField(max_length=200)
    m_message = models.TextField()