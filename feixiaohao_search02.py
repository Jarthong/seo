from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import random
import datetime

url = 'https://www.feixiaohao.com/exchange/'
# url = 'https://www.feixiaohao.com/hotsearch'   # search/?word=zt&tabs=0
elements = ['coinResult']  # 'coinResult','exchangeResult'
words = 'zt'

n = 0
while True:
    n += 1
    time = datetime.datetime.now()
    print('第{}次访问，当前时间:{}'.format(n, time))
    try:
        dr = webdriver.Chrome()
        dr.maximize_window()
        element = random.choice(elements)
        try:
            dr.get(url)

        except Exception as message:
            print('打开网站报错，报错信息如下：\n', message)
            dr.quit()
            dr = webdriver.Chrome()
            dr.get(url)
            print('重新执行一次...')

        try:
            WebDriverWait(dr, 10, 0.1).until(EC.presence_of_element_located((By.TAG_NAME, 'input'))).send_keys(words)
            sleep(random.uniform(1, 4))
            WebDriverWait(dr, 10, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, element))).click()
            sleep(random.uniform(2, 4))
        except Exception as message:
            print('-------元素获取超时,进入下一个循环-------,错误信息是：\n', message)

        try:
            dr.switch_to.window(dr.window_handles[1])
            # 拉动滚动条
            num = random.uniform(800, 1500)
            print('拉动滚动条距离：', num)
            dr.execute_script('window.scrollTo(0, {});'.format(num))
            sleep(random.uniform(2, 6))
        except Exception as message:
            print('拉动滚动条出现报错，报错信息如下：', message)

        try:
            # 拉动滚动条
            num = random.uniform(20, 800)
            print('拉动滚动条距离：', num)
            dr.execute_script('window.scrollTo(0, {});'.format(num))
            sleep(random.uniform(1, 5))
        except Exception as message:
            print('拉动滚动条出现报错，报错信息如下：', message)

        # 清除浏览器cookies
        try:
            cookies = dr.get_cookies()
            # print(f"main: cookies = {cookies}")
            dr.delete_all_cookies()
        except Exception as message:
            print('清除浏览器cookies出现报错，报错信息如下：', message)

        dr.quit()
        # sleep(5)
    except Exception as message:
        print('打开浏览器出差，出错信息如下：\n', message)

