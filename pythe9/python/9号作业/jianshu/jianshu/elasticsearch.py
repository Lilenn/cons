from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document,Text,Keyword,Date,Integer
from datetime import datetime
# from .spiders.jianShu import

# 定义一个默认的es的client
connections.create_connection(hosts=["localhost"])

class Article(Document):
    title = Text(analyzer="ik_max_word")
    body = Text(analyzer="ik_max_word")
    tag = Keyword()
    publish_from = Date()
    vote = Integer

    class Index:
        name = "blog4"
        settings = {
            "number_of_shards":2
        }

# Article.init()

# 添加数据
article = Article(meta={"id":1},title="hello es" , body="hello es,还在报错么",
                  publish_from=datetime.now(),tag=["elasticsearch"])
article.save()