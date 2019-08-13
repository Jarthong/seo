#!/usr/bin/env python
print('If you get error "ImportError: No module named \'six\'" install six:\n'+\
    '$ sudo pip install six');
print('To enable your free eval account and get CUSTOMER, YOURZONE and ' + \
    'YOURPASS, please contact sales@luminati.io')

import sys
print('打印', sys.version_info)

if sys.version_info[0]==2:
    import six
    from six.moves.urllib import request
    opener = request.build_opener(
        request.ProxyHandler(
            {'http': 'http://lum-customer-hl_cd1509f6-zone-static:rb5ql16q18z8@zproxy.lum-superproxy.io:22225'}))
    print(opener.open('http://lumtest.com/myip.json').read())

if sys.version_info[0] == 3:
    import urllib.request
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler(
            {'http': 'http://lum-customer-hl_cd1509f6-zone-static:rb5ql16q18z8@zproxy.lum-superproxy.io:22225'}))
    print(opener.open('http://lumtest.com/myip.json').read())


'''
# 使用搜狐来获取IP地址
import urllib.request
import re
request = urllib.request.Request('http://txt.go.sohu.com/ip/soip')
response = opener.open(request)
text_bytes = response.read()  # 得到的返回数据是二进制数据'bytes'
print(text_bytes, type(text_bytes))
text = text_bytes.decode('utf-8')  # 将字节转换成字符
ip = re.findall(r'\d+.\d+.\d+.\d+', text)[0]
mes = '公网IP地址是：{}'.format(ip)
print(mes)
print(text)
'''