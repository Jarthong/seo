from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import threading

url = 'https://www.baidu.com/'
# keyword_list = ['zbgcom', 'zbg.com', 'zbg交易所官网', 'zbg', 'zbg登录', 'zbg交易所',
#                 '比特币交易平台zbg', 'zbg交易所网站', 'zbg官网']
keyword_list = ['zbg.com', 'zbg官网', 'zbg', 'zbg交易所']

def request_all(keyword):
    dr = webdriver.Chrome()
    while True:
        try:
            dr.get(url)
            dr.find_element_by_id('kw').clear()
            dr.find_element_by_id('kw').send_keys(keyword)
            dr.find_element_by_id('su').click()
        except:
            print('网络连接断开------等待重新连接----------')
        try:
            WebDriverWait(dr, 5, 0.1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="1"]/h3/a'))).click()
            dr.switch_to.window(dr.window_handles[1])
            sleep(3)
            dr.close()
            dr.switch_to.window(dr.window_handles[0])
        except:
            print('-------元素获取超时-------进入下一个循环')

if __name__ == '__main__':
    for i in keyword_list:
        print('搜索的关键字如下：', i)
        t = threading.Thread(target=request_all, args=(i,))
        t.start()


