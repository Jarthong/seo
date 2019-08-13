from selenium import webdriver
import xlrd, re, requests, random
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

workbook = xlrd.open_workbook('youtub.xlsx')
# 根据sheet索引或者名称获取sheet内容，sheet索引从0开始
sheet = workbook.sheet_by_index(0)
# 获取指定单元格的值
# url = sheet.cell(1, 0).value
url_all = sheet.col_values(0)
url_all.pop(0)
# 删除url数组中的空元素
for x in range(0, url_all.count('')):
    url_all.remove('')
num_len = len(url_all)
print(num_len, type(num_len))

num = int(sheet.cell(1, 1).value)
time = int(sheet.cell(1, 2).value)
# print('观看视频的网址是：', url, '\n观看次数：', num, '\n每次观看时间（秒）：', time)
print('观看视频的网址是：', url_all, '\n观看次数(所有视频总共加起来的次数)：', num, '\n每次观看时间（秒）：', time)

dr = webdriver.Chrome()

n = 0
while n < num:
    n += 1
    try:
        text = requests.get('http://txt.go.sohu.com/ip/soip').text
        # print(text)
        ip = re.findall(r'\d+.\d+.\d+.\d+', text)
        print('当前公网IP：', ip[0])
    except:
        print('网络连接断开-------等待重新连接---------')
    print('第%s次观看视频开始...' % n)
    url_random = random.choice(url_all)
    print('此次观看的网址是：', url_random)
    try:
        dr.get(url_random)
    except Exception as message:
        print('打开网站报错，报错信息如下：\n', message)
        print('重新执行一次...')
        dr.close()
        dr = webdriver.Chrome()
        dr.get(url_random)

    # dr.find_element_by_class_name('ytp-large-play-button').click()
    sleep(time)

    try:
        cookies = dr.get_cookies()
        print(f"main: cookies = {cookies}")
        dr.delete_all_cookies()
    except Exception as message:
        print('清除浏览器cookies出现报错，报错信息如下：', message)
