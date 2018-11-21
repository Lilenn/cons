from django.core.mail import send_mail ,EmailMultiAlternatives

from django.conf import settings
from myApp.models import EmailRecord
import random
def get_random_code(max_length=16):
    str  = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    content = ''
    for x in range(max_length):
        content  = content + random.choice(str)
    return content

def send_email(email,code='',email_type = 'register'):

    if email_type == 'register':
        if len(code) == 0 or code == None:
            # 获取随机的 激活码
            code = get_random_code()
            # 保存邮件信息
            email_obj = EmailRecord()
            email_obj.code = code
            email_obj.email = email
            email_obj.save()

        email_subject = 'XX网账户激活通知'
        mail_content = '<h3>点击以下链接，激活账户:</h3><a href="http://localhost:8000/login/active/%s">http://localhost:8000/login/active/%s</a>' %(code,code)

        mail = EmailMultiAlternatives(email_subject, mail_content, settings.EMAIL_HOST_USER, ['846077763@qq.com'])
        mail.content_subtype = 'html'
        res = mail.send()
        return res

    elif email_type == 'forget':

        email_subject = 'XX网账户重置密码'
        mail_content = '<h3>点击以下链接，重置密码:</h3><a href="http://localhost:8000/login/reset/%s">http://localhost:8000/login/reset/%s</a>' % (email,email)

        mail = EmailMultiAlternatives(email_subject, mail_content, settings.EMAIL_HOST_USER, ['846077763@qq.com'])
        mail.content_subtype = 'html'
        res = mail.send()
        return res

