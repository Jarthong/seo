from selenium import webdriver
from time import sleep
import xlrd

workbook = xlrd.open_workbook('Page_View.xlsx')
# 根据sheet索引或者名称获取sheet内容，sheet索引从0开始
sheet = workbook.sheet_by_index(0)
# 获取访问次数、每次访问时间间隔、每批访问网址个数
times = int(sheet.cell(1, 1).value)
time = int(sheet.cell(1, 2).value)
num = int(sheet.cell(1, 3).value)
# 获取Excel中url整列数据为数组,并删除第一个元素(Excel表第一个元素不是关键字）
url_cols = sheet.col_values(0)
url_cols.pop(0)
# 删除url数组中的空元素
for y in range(0, url_cols.count('')):
    url_cols.remove('')
print('即将访问以下网址：\n', url_cols, '\n总共访问次数：', times, '\n每次访问时间间隔：', time, '\n每次访问网站个数', num)
len_url = len(url_cols)

# 总共分成几段
if len_url % 5 == 0:
    subsection = len_url // 5
else:
    subsection = len_url // 5 + 1

n = 0
while n < times or times == -1:
    n += 1
    print('第%s次访问...' % n)
    # 每一次大循环中，把地址分批后打开
    m = 0
    while m < subsection:
        fist_num = int(m * num)
        last_num = int(m * num + num)
        # print('起始位，结束位:', fist_num, last_num)
        m += 1
        url_list = url_cols[fist_num:last_num]  # 数组切片含前不含后
        # print('第{}次第{}批打开的网址{}'.format(n, m, url_list))
        len_url_list = len(url_list)

        dr = webdriver.Chrome()
        dr.set_page_load_timeout(10)
        dr.set_script_timeout(10)
        # 每次打开一个浏览器进程的同时，开几个线程（窗口）
        for i in range(0, len_url_list):
            try:
                url = url_list[i]
                # 新开一个窗口，通过执行js来新开一个窗口
                js = 'window.open("{}");'.format(url)
                dr.execute_script(js)
                print('第{}次第{}批打开的第{}个网址：{}'.format(n, m, i+1, url))
            except Exception as message:
                print('可能网络连接断开,等待重新连接-----错误信息是：\n', message)
        print('等待%s秒后，清除浏览器缓存，并执行下一次访问...' % time)
        print('-'*100)
        sleep(time)

        # 清除浏览器cookies
        try:
            dr.delete_all_cookies()
        except Exception as message:
            print('清除浏览器cookies出现报错，报错信息如下：', message)
        dr.quit()
        if n == times:
            print('恭喜您！总共访问填入的网站%s次，执行完成！' % times)









