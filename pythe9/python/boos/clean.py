import pymongo
client = pymongo.MongoClient('localhost', 27017)
zhipin = client['zhipin']
zhipin_java = zhipin['zhipin_java']
zhipin_python = zhipin['zhipin_python']

from collections import Counter
from pyecharts import Bar,Line,Pie

import re
def get_zone():
    ''' 获取地区'''
    zone_list = []
    real_list = []
    for item in zhipin_java.find():
        text = item['person_info'][3:6]
        zone_list.append(text)
    for i in zone_list:
        j = re.sub(r' \d-','',i)
        real_list.append(j)
        while '' in real_list:
            real_list.remove('')
    return real_list
zone = dict(Counter(get_zone()))

# def del_key_1():
#     '''删除招聘次数为1的岗位'''
#     li = []
#     for key in job_dict.keys():
#         if job_dict[key] == 1:
#             li.append(key)
#     for i in li:
#         del job_dict[i]
#     print(job_dict)
# #
def get_salary():
     '''获取招聘的工资'''
     min_list = [] #起步工资
     max_list = [] #最高工资
     job_title = [] #岗位
     for item in zhipin_java.find():
         job_title.append(item['job_title'])
         salary = item['salary']
         min_list.append(int(salary.split('-')[0][:-1]))
         max_list.append(int(salary.split('-')[1][:-1]))
     return min_list,max_list,job_title