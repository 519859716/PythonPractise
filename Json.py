#encoding=utf8

#将数组格式变成JSON格式数据：


import json


data = [{'a':1,'b':2,'c':3}]

json1 = json.dumps(data)

print json1

print type(json1)
#[{"a": 1, "c": 3, "b": 2}]  JSON 格式的数据。<type 'str'>

#使用json.loads 方法可以将JSON格式转换为python格式
json2 = json.loads(json1)
print json2
print type(json2)

print json.dumps({'a':'Rood','b':7},sort_keys=True,indent=1,separators=(',',':'))


