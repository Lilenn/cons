
class DataManager(object):
    def get_total_page(self):
        print('获取总页码数')

class Spider():
    def __init__(self):
        # 1.创建一个dataMnange 对象
        # 2.该对象为Spider的属性
        self.dataManger = DataManager()
    def start_spider(self):
        self.dataManger.get_total_page()

s= Spider()
s.start_spider()
d = DataManager()
d.get_total_page()
