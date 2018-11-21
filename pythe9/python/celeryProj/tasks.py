from celery import Celery

app = Celery(__name__,broker='amqp://root:123456@192.168.52.153',
             backend='redis://192.168.52.153:6379/0')

@app.task
def add(x,y):
    return x + y