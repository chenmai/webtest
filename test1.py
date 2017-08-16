import requests
import json
import os

file_path = os.getcwd().replace('\\', '/')
list1 = []
with open(file_path + '/address', 'r') as f:
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        list1.append(line.strip('\n'))
        line = f.readline()

# print(len(list1))
# print(list1)
# list1=['慈溪市','奉化市']
for i in list1:
    payload = {'level': 'district', 'district': '0', 'showbiz': 'false', 'extensions': 'base',
               'key': '7d5f9ce0453960017477cc47846e9afb', 's': 'rsv3', 'output': 'json', 'keywords': i}
    r = requests.get("http://restapi.amap.com/v3/config/district", params=payload)
    print(i)
    if not int(r.json().get("count")):
        with open(file_path + '/error', 'w') as f:
            f.write(str(i) + '\n')
        print(i)
