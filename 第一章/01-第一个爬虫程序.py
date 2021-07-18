from urllib.request import urlopen
import requests

url="http://www.baidu.com"
res = urlopen(url)

with open("mybaidu.html",mode="w",encoding="utf-8") as f:
    f.write(res.read().decode("utf-8"))
print("over")
