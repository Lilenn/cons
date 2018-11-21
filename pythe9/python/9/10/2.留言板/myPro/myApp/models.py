from django.db import models

# Create your models here.
class Message(models.Model):

    m_id = models.AutoField(primary_key=True)
    # TextField和 CharField 都是文本样式 基本上没有太大区别
    # 不过
    # textfield 理论上是无限长的
    # charfield 需要指定长度
    m_name = models.TextField()
    m_email = models.CharField(max_length=50)
    m_address = models.CharField(max_length=50)
    m_message = models.TextField()
