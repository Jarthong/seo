#!/usr/bin/env python
from urllib import request, parse
import hashlib, time
# 构建一个私密代理Handler，需要加上私密代理账户的用户名和密码
proxy_handler = request.ProxyHandler({'http': 'http://lum-customer-hl_cd1509f6-zone-static:rb5ql16q18z8@zproxy.lum-superproxy.io:22225'})
opener = request.build_opener(proxy_handler)
# 测试环境  990（ID:7ezdaxgBgC8，Google:IHKWBKQZUHBHOBWI）,330（7gwUzgkdsdE）
base_url = 'http://179.zbg.com'
user_id = '7ezdaxgBgC8'
server_id = 'exchange-001'
http_key = '3a659879-8832-41a7-b542-79b73c53c73e'
secret = 'IHKWBKQZUHBHOBWI'
timestamp = str(int(time.time() * 1000))
param = ''
param_bytes = bytes(parse.urlencode(param), encoding='utf8')
sig_str = server_id + timestamp + param + http_key
signature = hashlib.md5(sig_str.encode('utf-8')).hexdigest()
header = {'Clienttype': '0', 'Serverid': server_id, 'Timestamp': timestamp, 'Sign': signature}
# 查询market列表
API_GET_MARKET_LIST = "/exchange/config/controller/website/marketcontroller/getByWebId"
req = request.Request(base_url + API_GET_MARKET_LIST, data=param_bytes, headers=header, method="POST")
request.install_opener(opener)
response = request.urlopen(req)
# response = opener.open(req)
text_bytes = response.read().decode("utf-8")  # 得到的返回数据是二进制数据'bytes'
print(text_bytes, type(text_bytes))

