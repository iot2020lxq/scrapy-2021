import requests
import re
import csv

#服务器渲染
url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}
res = requests.get(url,headers = headers)
res.encoding = "utf-8"
page_content = res.text
# print(page_content)
#解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<title>.*?)</span>.*?'
                 r'<span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp',re.S)
it = obj.finditer(page_content)

with open('data.csv',mode = 'w',encoding='utf-8') as f:
    csvFile = csv.writer(f)
    for i in it:
        dic = i.groupdict()
        dic['year'] = dic['year'].strip()
        csvFile.writerow(dic.values())
        print(i.group('title') + "---" + i.group('year').strip())
print("over")