import pika

credentials = pika.PlainCredentials(username='root',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.153',credentials=credentials)

connection = pika.BlockingConnection(conn)

channel = connection.channel()

# rabbitmq 消费端仍然使用此方法创建队列
# 这样做的意思就是：若没有就创建，目的是保证队列一定会有
channel.queue_declare(queue='task_queue',durable=True)

def callback(ch,method,properties,body):
    print('Recevie %s' % body)
    # 手动对消息进行确认
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 保证能够做完之后通知给server端
channel.basic_qos(prefetch_count=1)

# no_ack 默认值是false，需要对message进行确认
channel.basic_consume(callback,
                      queue='task_queue')

# 循环去消息队列取消息
channel.start_consuming()