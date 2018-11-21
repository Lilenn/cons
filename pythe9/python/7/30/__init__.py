# csv : comma sepreated value 逗号分隔值
import csv

rows = [['张三',14],['李四',24],['王五']]
# 写入
with open('test1.csv','w',newline='')as csv_file:
    # 获取一个csv对象进行写入
    writer = csv.writer(csv_file)
    for row in rows:
        # 写入一行数据
        writer.writerow(row)
# 读取
with open('test1.csv','r')as read_csv:
    # 获取一个csv对象进行内容读取
    reader = csv.reader(read_csv)
    print(reader)

    print([row for row in reader])

def write_data():
    columns = int(input('请输入总列数'))
    col_list = []
    while True:
        # for n in columns:
        #     result = input('请输入第{}列数据'.format(n + 1))
        #     col_list.append(result)
        col_list.append([input('请输入第{}列数据'.format(n + 1))for n in range(columns)])
        is_continute  =input('是否继续？Y/N')

        if is_continute !='Y':
            break

    with open('test2.csv','w',newline ='') as csv_file:
        writer = csv.writer(csv_file)
        for row in col_list:
            writer.writerow(row)
# write_data()

data_dic = [{'name':'张三','age':'15'},{'name':'李四','age':'25'}]
with open('dict.csv','w',newline='')as csv_file:
    keys = []
    for key in data_dic[0].keys():
        print(key)
        keys.append(key)
    # fieldnames 设置文本的标题
    writer = csv.DictWriter(csv_file,fieldnames=keys)
    # 开始和写入标题
    writer.writeheader()
    for dict in data_dic:
        writer.writerow(dict)

with open('dict.csv','r') as csv_file:
    reader = csv.DictReader(csv_file)
    print([row for row in reader])