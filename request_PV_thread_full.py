import requests, threading, random, re
from time import sleep
import socket

# 设置需要刷访问量的网址,以数组的形式填入
url_all = [
           # 'https://www.zbg.com',
           # 'https://baijiahao.baidu.com/s?id=1609649087905924476&wfr=spider&for=pc',
           # 'https://finance.china.com/cydt/20000860/20190128/25347802.html',
           # 'https://www.jianshu.com/p/8ec1f3d29f89?from=singlemessage',
           # 'https://www.toutiao.com/i6650643368319648259/?wxshare_count=2&pbid=6652274926509180420',
           # 'http://hn.ifeng.com/a/20190128/7192825_0.shtml',
           # 'http://baijiahao.baidu.com/builder/preview/s?id=1625249878259755442',
           'https://www.weibo.com/ttarticle/p/show?id=2309404334554310670163',
           'https://www.weibo.com/ttarticle/p/show?id=2309404281984699522791&mod=zwenzhang'
           ]

# 模拟浏览器，需要使用Header，常用的User-Agent，供随机选择
user_agent = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0"]

# 定制请求头
def headers_all(User_Agent):
    headers = {'User-Agent': User_Agent}
    return headers

# 封装访问网站的方法
def request_all(url):
    user_agent_random = random.choice(user_agent)
    headers = headers_all(user_agent_random)
    try:
        r = requests.get(url=url, headers=headers)
        r_code = r.status_code
        print(url, '访问状态码：', r_code)
    except Exception as message:
        print(message)
        print('连接失败的网址是：', url)

if __name__ == '__main__':
    n = 0
    while True:
        n += 1
        print('访问次数累计：%s' %n)
        # 查询公网地址
        try:
            text = requests.get('http://txt.go.sohu.com/ip/soip').text
            # print(text)
            ip = re.findall(r'\d+.\d+.\d+.\d+', text)
            print('此次公网IP：', ip[0])
        except:
            print('网络连接断开-------等待重新连接---------')

        # 根据url数量，建立对应数量的线程，并调用request_all方法，访问网址
        for i in url_all:
            t = threading.Thread(target=request_all, args=(i,))
            t.start()




