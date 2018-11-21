import pika

# 验证用户名和密码
credentials = pika.PlainCredentials(username='root',password='123456')
# 连接到队列服务器
# 这里是通过远程连接到ip，要保证rabbitmq使用的端口是开放的
conn = pika.ConnectionParameters(host='192.168.52.153',credentials=credentials)
# 启用对库进行阻塞，同步操作进行简单的使用
connection = pika.BlockingConnection(conn)

# 声明一个管道
channel = connection.channel()
# 创建一个队列,设置队列的名字，如果rabbitmq服务器有队列那就不管，如果没有就自动创建出来
channel.queue_declare(queue='hello')

# 使用默认的交换机发送信息，exchange为空就是使用默认的
channel.basic_publish(exchange='',
                      routing_key='hello' #queue的名字，也叫路由键，写明将消息发往那个队列
                      ,body='Hello World!') # body就是消息的详细内容

print('Send Done! Body=hello world!')
connection.close()