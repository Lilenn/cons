import pika
import uuid

class FibonacciRpcClint():
    def __init__(self):
        # 创建连接
        credentials = pika.PlainCredentials(username='root', password='123456')
        conn = pika.ConnectionParameters(host='192.168.52.153', credentials=credentials)
        self.connection = pika.BlockingConnection(conn)
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        # 设置回调
        self.channel.basic_consume(self.on_response,
                                   no_ack=True,
                                   queue=self.callback_queue)
        # self.channel.queue_declare(queue='rpc_queue')

    def on_response(self,ch,method,properties,body):
        if self.corr_id == properties.correlation_id:
            self.response = body

    def call(self,n):
        # 设置响应和回调的通道id
        self.response = None
        self.corr_id = str(uuid.uuid4())

        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(reply_to=self.callback_queue,
                                                                   correlation_id=self.corr_id),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()

        return self.response
fib = FibonacciRpcClint()
response = fib.call(20)
print(response)
