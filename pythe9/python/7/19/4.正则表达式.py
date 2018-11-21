import re

content ="""
today is hot ,I
want sleep, I
want go home
"""
pattern = re.compile(r'.*?I(.*?)sleep')
result = pattern.search(content)
print(result)
# re.S 忽视换行符号
pattern = re.compile(r'.*?I(.*?)sleep',re.S)
result = pattern.search(content)
print(result)


