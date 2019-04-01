from selenium import webdriver
from time import sleep
import threading
import _thread

# 设置需要刷访问量的网址
url = 'https://www.jianshu.com/p/7bb600232df2'

# 新标签页打开这个url
dr = webdriver.Chrome()

while True:
    try:
        dr.get(url)
        # dr.close()
        # sleep(3)
    except Exception as message:
        print('可能网络连接断开,等待重新连接-----错误信息是：\n', message)



