# coding=utf-8
import requests
import os

file_path = os.getcwd().replace('\\', '/')
list1 = []
with open(file_path + '/addresscode', 'r') as f:
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        list1.append(line.strip('\n'))
        line = f.readline()

# with open(file_path + '/address', 'r+') as g:
#     list2 = g.readlines()

list3 = []
count = 0

for i in list1:
    payload = {'level': 'district', 'subdistrict': '0', 'showbiz': 'false', 'extensions': 'base',
               'key': '7d5f9ce0453960017477cc47846e9afb', 's': 'rsv3', 'output': 'json', 'keywords': i}
    r = requests.get("http://restapi.amap.com/v3/config/district", params=payload)
    # print(r.json().get("count"))
    if not int(r.json().get("count")):
        print(r.json())
        list3.append(str(i))
        print(list3)
    count = count + 1
    print(count)
print('结束')
print(list3)
