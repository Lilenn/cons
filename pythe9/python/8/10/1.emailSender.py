# smtp  simple mail transfer protocol 简单右键传输协议
# lib library
import smtplib
# 因为需要使用这个模块，所以当前py文件名字不能写成email.py
import email
# MIMEText 多用于邮件扩充协议
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# 设置邮箱的域名
HOST = 'smtp.qq.com'
# 设置邮件标题
SUBJECT = '今天是2018年8月10日，是我18岁生日'
# 注意发件人的邮箱必须先设置开启smtp协议
FROM = '846077763@qq.com'
# 设置收件人的邮箱（可以一次性发送给多个人）
TO = '846077763@qq.com,2017348458@qq.com'
# related 表示使用内嵌资源的形式，将邮件发送给对方
# 邮件信息
message = MIMEMultipart('related')

# ----------------------------------发送文本-------------------------------
# 发送邮件主体到对方的邮箱中
# 参数
# 1.发送的内容 内容必须为字符串
# 2.内容的类型，文本类型默认为plain
# 3.编码的格式 使用utf-8进行编码
message_html1 = MIMEText('今天是星期五，猴开森','plain','utf-8')
#当内容的类型设置为<h2></h2> 的形式时，文本类型默认为 html
message_html = MIMEText('<h2 style="color:red;font-size:50px">学习使我快乐</h2><img src="cid:small">','html','utf-8')
# 将邮件内容装入到邮件信息当中去
message.attach(message_html)

# --------------------------------------发送图片------------------------------------
# rb 读取二进制文件
image_data = open('2.png','rb')
# 设置读取获取的二进制数据
message_images = MIMEImage(image_data.read())
# 关闭刚才打开的文件
image_data.close()
# message_images.add_header('Content-ID','small')
message_html = MIMEText('<h2 style="color:red;font-size:50px">学习使我快乐</h2><img src="cid:small">','html','utf-8')
# 添加图片文件到邮件信息当中去
message.attach(message_images)

# -------------------------------------发送图片的第二种方式-----------------------------
message_image = MIMEText(open('1.gif','rb').read(),'base64','utf-8')
message_image['Content-disposition'] = 'attachment;filename="happy.gif"'
message.attach(message_image)
# -------------------------------------添加文件------------------------------------
# 将一个xlsx文档作为内容发送到对方的邮箱。
# 读取excel文件时， 是以rb形式进行读取，是一个二进制内容
# 对二进制文件需要设置，默认编码形式
# 对于MIMEText来说，默认的编码形式为base64
# 如果对于二进制文件来说，没有设置base64进行编码，则附件就会呈现乱码
message_xlsx = MIMEText(open('table.xlsx','rb').read(),'base64,','utf-8')
# 设置文件在附件当中的名字
message_xlsx['Content-Disposition'] = 'attachment;filename = "test1111.xlsx"'
message.attach(message_xlsx)

# 设置邮件发件人
message['From'] = FROM
# 设置邮件收件人
message['To'] = TO
# 设置邮件标题
message['Subject'] = SUBJECT
# 获取简单邮件传输协议证书
email_client = smtplib.SMTP_SSL()
# 设置发件人邮箱的域名和端口 端口为465
email_client.connect(HOST,'465')
# 密码千万不要写邮箱的密码而是授权码
result = email_client.login(FROM,'beebxxduyevxbfgb')

print('登陆结果',result)
# adderess 地址
# 发送邮件
# message = MIMEMultipart('related') message 为MIMEMultipart的一个对象
# msg 后面的结果必须是一个字符串
email_client.sendmail(from_addr=FROM,to_addrs=TO.split(','),msg=message.as_string())
# 关闭邮件发送客户端
email_client.close()
