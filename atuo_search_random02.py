from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import random

# 要搜索的网址，如百度、谷歌...
url = 'https://www.baidu.com/'

# 要搜索的关键字，以数组的形式填入
keyword_list = ['ZBG', 'ZBG新币', 'ZBG 比特币', 'ZBG btc', 'ZBG数字资产', 'ZBG数字货币', 'ZBG交易所', 'ZBG launchpad', '比特币 zbg']
keyword_twice = [['比特币', 'zbg'], ['btc', 'zbg']]

n = 0
while True:
    n += 1
    # 单次搜索-点击进入官网
    if n % 2 == 0:
        dr = webdriver.Chrome()
        keyword = random.choice(keyword_list)
        try:
            dr.get(url)
            dr.find_element_by_id('kw').clear()
            print('第%s次搜索关键字(单次搜索)：' %n, keyword)
            dr.find_element_by_id('kw').send_keys(keyword)
            dr.find_element_by_id('su').click()
            sleep(3)
        except Exception as message:
            print(message)
        if keyword != 'ZBG launchpad':
            try:
                WebDriverWait(dr, 5, 0.1).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, '全球领先的比特币(BTC)以太坊(ETH)'))).click()
                dr.switch_to.window(dr.window_handles[1])
                sleep(5)
            except Exception as message:
                print('-------元素获取超时,进入下一个循环-------,错误信息是：\n', message)
        else:
            pass
        try:
            dr.delete_all_cookies()
        except Exception as message:
            print('清除缓存报错，报错信息如下：', message)
        dr.quit()

    # 二次关联搜索：第一次搜索关键字，然后再关联另一关键字搜索
    else:
        dr = webdriver.Chrome()
        keyword = random.choice(keyword_twice)
        try:
            dr.get(url)
            dr.find_element_by_id('kw').clear()
            print('第%s次搜索关键字(二次搜索)：' %n, keyword)
            dr.find_element_by_id('kw').send_keys(keyword[0])
            dr.find_element_by_id('su').click()
            sleep(3)
            dr.find_element_by_id('kw').send_keys(' ' + keyword[1])
            dr.find_element_by_id('su').click()
            sleep(3)
        except Exception as message:
            print(message)
        try:
            WebDriverWait(dr, 5, 0.1).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, '全球领先的比特币(BTC)以太坊(ETH)'))).click()
            dr.switch_to.window(dr.window_handles[1])
            sleep(5)
        except Exception as message:
            print('-------元素获取超时,进入下一个循环-------,错误信息是：\n', message)
        try:
            dr.delete_all_cookies()
        except Exception as message:
            print('清除缓存报错，报错信息如下：', message)
        dr.quit()
