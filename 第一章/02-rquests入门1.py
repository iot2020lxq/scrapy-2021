import requests

wd = input("请输入关键字：")

url=f"http://www.baidu.com/s?wd={wd}"
dic={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}
resp = requests.get(url,dic)
resp.encoding = 'utf-8'
print(resp.text)
resp.close()
