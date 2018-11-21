from django.core.mail import send_mail , EmailMultiAlternatives
import random
from django.conf import settings
from myApp.models import EmailRecord
def get_random_code(max_length = 16):
    str = 'QWERTYUIOPASDFGHJKLBNMqwertyuiopzxcvasdfghjklZXCVbnm1234567890'
    content = ''
    for x in range(max_length):
        content = content + random.choice(str)
    return content

def send_email(email,code=''):
    if len(code) == 0 or code == None:
        # 获取随机的激活码
        code = get_random_code()
    email_obj = EmailRecord()
    email_obj.code = code
    email_obj.email = email
    email_obj.save()

    email_subject = 'XX网账户激活通知'
    mail_content = '<h3>点击一下链接，激活账户：</h3><a href="http://localhost:8000/login/active/%s">http://localhost:8000/login/active/%s</a>' % (code,code)

    mail = EmailMultiAlternatives(email_subject,mail_content,settings.EMAIL_HOST_USER,['846077763@qq.com'])
    mail.content_subtype = 'html'
    res = mail.send()
    return res
