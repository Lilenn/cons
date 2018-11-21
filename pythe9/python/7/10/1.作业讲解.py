# 1.计算1-100之和。

sum = 0
for i in range(101):
  sum = sum +i
print(sum)

# 2.计算n 的n次方
i = 3
x = 1
if i == 0:
  print(0)

else:
    for a in range(i):
      x = x* i
      print(x)

# 3.鸡兔同笼，其中头共有32头，96条腿，问鸡兔各几只？
for ji in range(33):
  for tu in range(33):
    if ji + tu == 32 and ji*2 + tu*4 ==96:
      print('鸡，兔各有{} {}只'.format(ji , tu ))

ji = 0
tu = 0
for index in range(33):
  tu += 1
  ji = 32 - tu
  if ji *2 + tu *4 ==96:
    print(ji ,tu )

# 4.有一百匹马，一百担货物，大马一只可以驼三担，中码可以驼两担，两只小马可以托一dan，问各有几只马？


# item = DouyuItem()
#         x = json.loads(response.text)
#         for img in x['data']:
#             src = img['room_src']
#
#             item['src'] = [src]
#
#             yield item
#         for y in range(2,501):
#             url = 'http://api.douyucdn.cn/api/v1/getverticalRoom?limit=20&offset=' + str(y)
#
#             yield scrapy.Request(url=url,callback=self.parse)
