#!/usr/bin/env python
from urllib import request, parse

# 构建一个私密代理Handler，需要加上私密代理账户的用户名和密码
proxy_handler = request.ProxyHandler({'http': 'http://lum-customer-hl_cd1509f6-zone-static:rb5ql16q18z8@zproxy.lum-superproxy.io:22225'})
opener = request.build_opener(proxy_handler)

# request.urlopen()不使用自定义代理,将使用本地公网IP
req2 = request.Request('http://lumtest.com/myip.json')
response2 = request.urlopen(req2)
text_bytes2 = response2.read().decode("utf-8")  # 得到的返回数据是二进制数据'bytes',加上decode('uft-8')则转换为字符串
print(text_bytes2, type(text_bytes2), '\n1', '-'*100)

# opener.open()将使用自定义代理，即上面构建的私密代理
req3 = request.Request('http://lumtest.com/myip.json')
response3 = opener.open(req3)
text_bytes3 = response3.read().decode("utf-8")
print(text_bytes3, type(text_bytes3), '\n2', '-'*100)

# 加上request.install_opener(opener)后，之后所有的request.urlopen()也会使用私密代理，即：将opener应用到全局
req = request.Request('http://lumtest.com/myip.json')
request.install_opener(opener)
response = request.urlopen(req)
text_bytes = response.read().decode("utf-8")
print(text_bytes, type(text_bytes), '\n3', '-'*100)






'''
import requests
import re
import hashlib
import time

# 测试环境  990（ID:7ezdaxgBgC8，Google:IHKWBKQZUHBHOBWI）,330（7gwUzgkdsdE）
base_url = 'http://179.zbg.com'
user_id = '7ezdaxgBgC8'
server_id = 'exchange-001'
http_key = '3a659879-8832-41a7-b542-79b73c53c73e'
secret = 'IHKWBKQZUHBHOBWI'

timestamp = str(int(time.time() * 1000))
param = ''
param_bytes = bytes(parse.urlencode(param), encoding='utf8')  #
sig_str = server_id + timestamp + param + http_key
signature = hashlib.md5(sig_str.encode('utf-8')).hexdigest()
header = {'Clienttype': '0', 'Serverid': server_id, 'Timestamp': timestamp, 'Sign': signature}

# 查询market列表
API_GET_MARKET_LIST = "/exchange/config/controller/website/marketcontroller/getByWebId"
req = request.Request(base_url + API_GET_MARKET_LIST, data=param_bytes, headers=header, method="POST")
response = request.urlopen(req)
text_bytes = response.read().decode("utf-8")  # 得到的返回数据是二进制数据'bytes'
print(text_bytes, type(text_bytes))
'''



