import pika

credit = pika.PlainCredentials(username='root',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.153',credentials=credit)
connection = pika.BlockingConnection(conn)

# 建立管道
channel = connection.channel()

# durable ：server关闭了队列依旧存在
channel.queue_declare(queue='task_queue',durable=True)

# delivery_mode=2 使消息持久化
message = 'test chijiuhua'
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2))
print('Send done! %s' % message)

connection.close()