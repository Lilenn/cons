
import smtplib

from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SenderEmail(object):
    def __init__(self):

        self.host = 'smtp.qq.com'
        self.port = '465'
        self.sender = '846077763@qq.com'
        self.recever = '846077763@qq.com'
        self.password = 'beebxxduyevxbfgb'
        self.message = MIMEMultipart('related')
        self.message['From'] = self.sender
        self.message['To'] = self.recever

    def send_data(self,subject):
        self.message['Subject'] = subject
        # 添加文本和图片
        message_text = MIMEText('<h2 style="color:yellowred">就算不会写，也要浪到飞起</h2><img src="cid:big">','html','utf-8')
        self.message.attach(message_text)
        message_img = MIMEImage(open('1.jpg','rb').read())
        message_img.add_header('Content-ID','big')
        self.message.attach(message_img)

        # 添加图片第二种方式
        # message_img =  MIMEImage(open('1.jpg','rb').read(),'base64','utf-8')
        # message_img['Content-Disposition'] = 'attachment;filename="lang.jpg"'
        # self.message.attach(message_img)

        # 添加文件
        message_xlsx = MIMEText(open('taobao.csv','rb').read(),'base64','utf-8')
        message_xlsx['Content-Disposition'] = 'attachment;filename="Taobao.xlsx"'
        self.message.attach(message_xlsx)

    def login(self):

        try:
            client = smtplib.SMTP_SSL(self.host,self.port)
            result = client.login(self.sender,self.password)
            if result[0] == 235:
                print('登陆成功')
                client.sendmail(self.sender,self.recever,self.message.as_string())
                print('发送成功')
        except Exception as e:
            print('错误原因',e)




