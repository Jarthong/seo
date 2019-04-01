from selenium import webdriver
from time import sleep
import threading

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

# 为线程定义一个函数
def request_all(url):
    dr1 = webdriver.Chrome()
    while True:
        try:
            dr1.get(url)
            sleep(5)
        except:
            print('网络连接断开-------等待重新连接---------')

# 根据url数量，建立对应数量的线程，并调用request_all方法，循环访问网址
for i in url_all:
    print(i)
    t = threading.Thread(target=request_all, args=(i,))
    t.start()





