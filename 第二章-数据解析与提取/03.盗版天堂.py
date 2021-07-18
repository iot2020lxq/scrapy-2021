import requests

domain = "https://www.dy2018.com/"
resp = requests.get(domain,verify=False)#verify去掉安全认证
resp.encoding = "gb2312"
print(resp.text)

