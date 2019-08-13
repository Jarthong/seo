from selenium import webdriver
from time import sleep
import threading
import _thread

# 设置需要刷访问量的网址
url_1 = 'https://www.zbg.com'
url_2 = 'https://finance.china.com/cydt/20000860/20190128/25347802.html'
url_3 = 'https://www.jianshu.com/p/8ec1f3d29f89?from=singlemessage'
url_4 = 'http://finance.lcxw.cn/xiangmu/2019-01-28/26150.html'
url_5 = 'https://baijiahao.baidu.com/s?id=1609649087905924476&wfr=spider&for=pc'
url_6 = 'https://www.toutiao.com/i6650643368319648259/?wxshare_count=2&pbid=6652274926509180420'

# 新标签页打开这个url
# dr = webdriver.Chrome()

# while 1 == 1:
#     dr.get(url_1)
#     # dr.close()
#     js = "window.open('https://finance.china.com/cydt/20000860/20190128/25347802.html')"
#     dr.execute_script(js)
#     # dr.close()
#     # sleep(3)





def request_1():
    dr1 = webdriver.Chrome()
    # dr1.get(url_1)
    # sleep(1)
    # #
    while 1 == 1:
        dr1.get(url_1)
        sleep(1)


def request_2():
    dr2 = webdriver.Chrome()
    # dr2.get(url_2)
    # sleep(1)

    while 1 == 1:
        dr2.get(url_2)
        sleep(1)

def request_3():
    dr = webdriver.Chrome()
    while 1 == 1:
        dr.get(url_3)
        sleep(1)

def request_4():
    dr = webdriver.Chrome()
    while 1 == 1:
        dr.get(url_4)
        sleep(1)

def request_5():
    dr = webdriver.Chrome()
    while 1 == 1:
        dr.get(url_5)
        sleep(1)

def request_6():
    dr = webdriver.Chrome()
    while 1 == 1:
        dr.get(url_6)
        sleep(1)

threads = []
t1 = threading.Thread(target=request_1())
threads.append(t1)
t2 = threading.Thread(target=request_2())
threads.append(t2)
print(threads)

if __name__ == '__main__':
    t1 = threading.Thread(target=request_1())
    t2 = threading.Thread(target=request_2())


    # while 1 == 1:
    #     for t in threads:
    #         t.setDaemon(True)
    #         t.start()

    # request_1()
    # request_2()
    # request_3()
    # request_4()
    # request_5()
    # request_6()
