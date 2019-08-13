#!/usr/bin/env python
from urllib import request, parse
import requests, hashlib
import time, datetime, random
import json
import re, os
import urllib3
from requests import Response
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 构建一个私密代理Handler，需要加上私密代理账户的用户名和密码
proxy_handler = request.ProxyHandler({'http': 'http://lum-customer-hl_cd1509f6-zone-static:rb5ql16q18z8@zproxy.lum-superproxy.io:22225'})
opener = request.build_opener(proxy_handler)

# 线上环境
# base_url = 'https://www.zbg.com'
# host = 'www.zbg.com'
# server_id = 'exchange_server_zbg'
# http_key = '71a80abe-9b82-41b2-8fec-1bb598523c3f'
# kline_path = 'https://kline.zbg.com/api/data/v1/ticker?marketId='
# sleep_time = 7

# 测试环境
base_url = 'http://179.zbg.com'
host = '179.zbg.com'
server_id = 'exchange-001'
http_key = '3a659879-8832-41a7-b542-79b73c53c73e'
kline_path = 'http://179kline.zbg.com/api/data/v1/ticker?marketId='
sleep_time = 1

# 新增委托单接口
API_ADD_ENTRUST = '/exchange/entrust/controller/website/EntrustController/addEntrust'

def get_user_id():
    # 随机生成一个8位数字符组成的数组 (7d3pzGPompc）
    ran_list = random.sample('1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM', 8)
    # 把数组组成字符串
    ran_str = ''.join(ran_list)
    user_id = '7a' + ran_str + 'g'
    return user_id

'''
def get_market_id_list():
    try:
        api_get_market_list = "/exchange/config/controller/website/marketcontroller/getByWebId"
        timestamp2 = str(int(time.time() * 1000))
        param2 = ''
        sig_str2 = server_id + timestamp2 + param2 + http_key
        signature2 = hashlib.md5(sig_str2.encode('utf-8')).hexdigest()
        header2 = {'Clienttype': '0', 'Serverid': server_id, 'Timestamp': timestamp2, 'Sign': signature2}
        r = requests.post(base_url + api_get_market_list, data=param2, headers=header2, verify=False)
        r1 = r.json()
        # print('获取市场列表接口请求结果：', r1['resMsg'])
        market_num = len(r1['datas'])
        # print('接口返回数据：\n', r1)
        market_id_list_1 = []
        for i in range(0, market_num):
            data_id = r1['datas'][i]['marketId']
            market_id_list_1.append(data_id)
        print('当前环境的市场名称对应的ID：', market_id_list_1)
        return market_id_list_1
    except Exception as message1:
        print('获取市场ID出错，报错信息如下：{}，将从热门市场中随机选择一个市场！；\n'.format(message1))
        market_id_list_2 = ['322', '321', '329', '336', '345', '356', '364', '374', '330', '333']
        return market_id_list_2

market_id_list = get_market_id_list()  # 获取市场列表
'''
# 推荐区市场列表
market_id_list = ['330', '331', '333', '336', '382', '329', '380', '386', '416', '415', '417', '321', '374', '364', '476', '466', '477', '5003', '5004', '5009', '5008']

def get_price(market_id):
    try:
        path = kline_path + market_id
        r = requests.get(url=path, verify=False)
        price_basic = float(r.json()['datas'][1])
        # print('盘口当前成交价是：{}'.format(price_basic), type(price_basic))
        return price_basic
    except Exception as message2:
        print('获取价格报错，错误信息是：{}'.format(message2))
        return round(random.uniform(1, 100), 2)

def get_amount(market_id):
    if market_id == '329':
        return round(random.uniform(0, 0.1), 4)
    else:
        return round(random.uniform(1, 100), 2)

def save_the_message(file_name, message):
    current_path = os.path.dirname(os.path.realpath(__file__))
    filename = open(current_path + '\\' + file_name, 'a', encoding='UTF-8')
    filename.write(message + "\n")
    filename.close()
    # print('检查文件是否被正常关闭', filename.closed)

def get_user_agent():
    user_agent = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201'
    ]
    return random.choice(user_agent)

n = 0
while True:
    n += 1
    User_id = get_user_id()                     # 下单用户userID
    market_id = random.choice(market_id_list)   # 随机选择一个市场id
    entrust_type = random.choice([0, 1])        # 要下单的类型，0 卖出 1 购买
    price = get_price(market_id)                # 盘口当前成交价
    amount = get_amount(market_id)              # 数量
    user_agent = get_user_agent()               # 浏览器类型

    try:
        text = requests.get('http://txt.go.sohu.com/ip/soip').text
        # print(text)
        ip = re.findall(r'\d+.\d+.\d+.\d+', text)[0]
        save_the_message('IP.txt', ip)  # 保存IP地址到文件中
        mes = '第{}次下单的公网IP地址是：{}'.format(n, ip)
        save_the_message('log.txt', mes)
        print(mes)
    except Exception as message:
        mes = '获取公网IP出错，报错信息是{}'.format(message)
        save_the_message('log.txt', mes)
        print(mes)

    try:
        params = {'marketId': market_id, 'amount': amount, 'price': price, 'rangeType': 0, 'type': entrust_type}
        param = json.dumps(params)
        timestamp = str(int(time.time() * 1000))
        sig_str = server_id + timestamp + param + http_key
        signature = hashlib.md5(sig_str.encode('utf-8')).hexdigest()
        header = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,vi;q=0.8,ko;q=0.7,be;q=0.6,ja;q=0.5",
            "Connection": "keep-alive",
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            "Host": host,
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": user_agent,
            'Clienttype': '0', 'Serverid': server_id, 'Userid': User_id, 'Timestamp': timestamp, 'Sign': signature
        }
        Response = requests.request(method='POST', url=base_url + API_ADD_ENTRUST, headers=header, json=params, verify=False)
        # print(r_sell.text, type(r_sell.text))
        time_now = datetime.datetime.now()
        result_sell = Response.json()['resMsg']
        mes = '浏览器类型：{}\n用户：{}，市场：{}，盘口价格：{}，下单数量：{}，时间：{}，结果:{}\n{}'.format(user_agent, User_id, market_id, price, amount, time_now, result_sell, '-'*100)
        save_the_message('log.txt', mes)
        print(mes)
        # time.sleep(sleep_time)
    except Exception as message3:
        mes = '下单报错，错误信息如下：{},5秒钟后重新请求！\n{}'.format(message3, '-'*100)
        save_the_message('log.txt', mes)
        print(mes)
        time.sleep(5)

