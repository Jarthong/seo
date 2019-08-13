from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import random

url = 'https://www.feixiaohao.com/exchange/'
elements = ['coinResult', 'exchangeResult']

# while True:
#     dr = webdriver.Chrome()
#     dr.get(url)
#     element = random.choice(elements)
#     dr.find_element_by_tag_name('input').send_keys('ZBG')
#     dr.find_element_by_class_name(element).click()
#     dr.quit()

n = 0
while True:
    n += 1
    print('第%s次访问。。。' %n)
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
            WebDriverWait(dr, 10, 0.1).until(EC.presence_of_element_located((By.TAG_NAME, 'input'))).send_keys('ZBG')
            # sleep(2)
            WebDriverWait(dr, 10, 0.1).until(EC.presence_of_element_located((By.CLASS_NAME, element))).click()
            sleep(3)

        except Exception as message:
            print('-------元素获取超时,进入下一个循环-------,错误信息是：\n', message)
        dr.quit()
        # sleep(5)
    except Exception as message:
        print('打开浏览器出差，出错信息如下：\n', message)

