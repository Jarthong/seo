from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import random

# 要搜索的网址，如百度、谷歌...shiyixia
url = 'https://www.baidu.com/'

# 要搜索的关键字，以数组的形式填入
keyword_list = ['zbgcom', 'zbg.com', 'zbg交易所官网', 'zbg', 'zbg登录', '中币zbg官网下载', 'zbg交易所',
                '比特币交易平台zbg', 'zbg交易所网站', 'zbg官网']
dr = webdriver.Chrome()
n = 0
while True:
    n += 1
    try:
        dr.get(url)
        dr.find_element_by_id('kw').clear()
        keyword = random.choice(keyword_list)
        print('第%s次搜索关键字：' %n, keyword)
        dr.find_element_by_id('kw').send_keys(keyword)
        dr.find_element_by_id('su').click()
    except Exception as message:
        print(message)
    try:
        WebDriverWait(dr, 5, 0.1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="1"]/h3/a'))).click()
        dr.switch_to.window(dr.window_handles[1])
        sleep(1)
        dr.close()
        dr.switch_to.window(dr.window_handles[0])
    except Exception as message:
        print('-------元素获取超时,进入下一个循环-------,错误信息是：\n', message)
