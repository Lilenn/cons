

import smtplib

from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail(object):
    def __init__(self):

        self.host = 'smtp.qq.com'
        self.port = '465'
        self.sender = '1797190195@qq.com'
        self.receive = "lilantian824@163.com"
        # self.receive = "1797190195@qq.com"
        self.password = "jktarqhsggqyhfhd"
        self.message = MIMEMultipart("related")
        self.message["From"] = self.sender
        self.message["To"] = self.receive

    # 发送数据
    def send_data(self,subject):
        self.message["Subject"] = subject
        # 添加文本和图片
        message_text = MIMEText('<h1>一加手机好看吗</h1><img src="cid:phone">','html','utf-8')
        self.message.attach(message_text)
        message_img = MIMEImage(open('1.jpg','rb').read())
        message_img.add_header('Content-ID','phone')
        self.message.attach(message_img)
        # 添加图片第二种
        message_img = MIMEText(open('1.jpg','rb').read(),'base64','utf-8')
        message_img["Content-Disposition"] = 'attachment;filename="yijia.jpg"'
        self.message.attach(message_img)

        #  添加xlsx文件
        message_xlsx = MIMEText(open('Taobao.xlsx','rb').read(),'base64','utf-8')
        message_xlsx["Content-Disposition"] = 'attachment;filename="taobao_phone.xlsx"'
        self.message.attach(message_xlsx)

        self.login()

    # 登录
    def login(self):

        try:
            client = smtplib.SMTP_SSL(self.host,self.port)
            result = client.login(self.sender,self.password)
            if result[0] == 235:
                print("登陆成功")
                client.sendmail(self.sender,self.receive,self.message.as_string())
                print("发送成功")
        except Exception as e :
            print("错误原因",e)




