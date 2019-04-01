from selenium import webdriver
from time import sleep
import threading
import xlrd, re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

workbook = xlrd.open_workbook('UI_PV_baidu_jianshu_time.xlsx')
# 根据sheet索引或者名称获取sheet内容，sheet索引从0开始
sheet = workbook.sheet_by_index(0)
# 获取访问次数、每次访问时间间隔
num = int(sheet.cell(1, 1).value)
time = int(sheet.cell(1, 2).value)
# 获取Excel中url整列数据为数组,并删除第一个元素(Excel表第一个元素不是关键字）
url_cols = sheet.col_values(0)
url_cols.pop(0)
# 删除url数组中的空元素
for y in range(0, url_cols.count('')):
    url_cols.remove('')
print('即将访问以下网址：\n', url_cols, '\n总共访问次数：', num, '\n每次访问时间间隔：', time)
len_url = len(url_cols)

n = 0
m = 0
while n < num or num == -1:
    n += 1
    print('第%s次访问...' % n)
    dr = webdriver.Chrome()
    # print('此次访问的网址是：', url_cols[0])
    # dr.get(url_cols[0])

    for i in range(m, len_url):
        m = i
        if m != len_url:
            try:
                url = url_cols[i]
                # 新开一个窗口，通过执行js来新开一个窗口
                js = 'window.open("' + url + '");'
                dr.execute_script(js)
                print('此次访问的网址是：', url)
                # dr.get(url)

            except Exception as message:
                print('可能网络连接断开,等待重新连接-----错误信息是：\n', message)
        else:
            break
        print('等待%s秒后，清除浏览器缓存，并执行下一次访问...' % time)
        sleep(time)





    # 清除浏览器cookies
    try:
        cookies = dr.get_cookies()
        # print(f"main: cookies = {cookies}")
        dr.delete_all_cookies()
    except Exception as message:
        print('清除浏览器cookies出现报错，报错信息如下：', message)
    dr.quit()
    if n == num:
        print('恭喜您！总共访问填入的网站%s次，执行完成！' % num)
    # dr.close()




