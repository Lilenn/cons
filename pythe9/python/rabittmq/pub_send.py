import pika
import sys

credentials = pika.PlainCredentials(username='root',password='123456')
conn = pika.ConnectionParameters(host='192.168.52.153',credentials=credentials)
connection = pika.BlockingConnection(conn)

# 有多个设备连接到交换机，那么这交换机把消息发送给那个设备，是根据交换机的类型决定的
# 交换机的类行有: direct/topic/fanout
# fanout 这个类型是所有的设备都收到消息,这个就是广播
channel = connection.channel()
# 这里定义一个名为fanout类型的exchange
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

print(sys.argv)
message = sys.argv[1] if len(sys.argv) > 1 else 'info:logs'

# 将消息发送到名为logs的exchange中
# 因为是fanout类型的exchange,所以不需要制定routing_key
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print('Send %s' % message)

connection.close()