import re

# print("---findall---")
# list = re.findall(r"[0-9]+","电话：17608414126,07393605229")
# print(list)


#迭代器:finditer
# print("---finditer---")
# it = re.finditer(r"[0-9]+","电话：17608414126,07393605229")
# for i in it:
#     print(i.group())



#seatch:找到一个就返回结果
# print("---search---")
# s = re.search(r"[0-9]+","电话：17608414126,07393605229")
# print(s.group())


#match:从头开始匹配，
#print("---match---")
# s = re.match(r"[0-9]+","电话：17608414126,07393605229")
# print(s)


#预加载正则表达式
# print("---compile---")
# obj = re.compile(r"[0-9]+")
# ret = obj.finditer("电话：17608414126,07393605229")
# for i in ret:
#     print(i.group())

s = '''
    <div id = 1>刘琳</div>
    <div id = 2>杨进远</div>
    <div id = 3>王恒景</div>
'''
obj = re.compile(r"<div id = (?P<id>[0-9]+)>(?P<name>.*?)</div>",re.S)
res = obj.finditer(s)
for r in res:
    print(r.group("id") + ":"+ r.group("name"))