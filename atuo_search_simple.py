from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep


url = 'https://www.baidu.com/'
dr = webdriver.Chrome()
while True:
    try:
        dr.get(url)
        dr.find_element_by_id('kw').clear()
        dr.find_element_by_id('kw').send_keys('zbg')
        dr.find_element_by_id('su').click()
    except:
        print('网络连接断开-------等待重新连接---------')
    try:
        WebDriverWait(dr, 5, 0.1).until(EC.presence_of_element_located((By.XPATH, '//*[@id="1"]/h3/a'))).click()
        dr.switch_to.window(dr.window_handles[1])
        sleep(2)
        dr.close()
        dr.switch_to.window(dr.window_handles[0])
    except:
        print('-------元素获取超时-------进入下一个循环')

