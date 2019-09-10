#! /usr/bin/env python
# -*- coding:utf8 -*-
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import xlrd

# 获取当前页面文章标题
def get_title(driver):
    title_list = []
    for i in range(0, 10):
        # text = dr.find_element_by_css_selector('a[uigs="article_title_{}"]'.format(str(i))).text
        text = WebDriverWait(driver, wait_time, gap_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[uigs="article_title_{}"]'.format(str(i))))).text
        title_list.append(text)
    return title_list

# 点击下一页
def click_next_page(driver):
    try:
        driver.execute_script('window.scrollTo(0, 800);')
        WebDriverWait(driver, wait_time, gap_time).until(EC.presence_of_element_located((By.ID, 'sogou_next'))).click()
    except Exception as message:
        print('-'*100, '\n点击下一页出错，或者已经没有下一页可以点击了，请检查可以浏览页数的权限！报错信息如下：\n', message)

def judge(driver):
    m = 0
    while m < pages:
        m += 1
        # sleep(5)
        title_text_list = get_title(driver)
        print('-'*100, '\n第{}页中有以下文章：'.format(m))
        for x in title_text_list:
            print(x)
        for i in range(0, 10):
            title_text = title_text_list[i]
            if title in title_text:
                # 由于上一步的执行中已经进行了元素等待，这里也可不用等待
                # driver.find_element_by_css_selector('a[uigs="article_title_{}"]'.format(str(i))).click()
                WebDriverWait(driver, wait_time, gap_time).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[uigs="article_title_{}"]'.format(str(i))))).click()
                print('-' * 100, '\n第{}页中有要查看的文章！查看{}秒后将进入下一个循环。。。'.format(m, page_time))
                dr.switch_to.window(dr.window_handles[1])
                sleep(page_time/2)
                num = random.uniform(1000, 10000)
                # print('拉动滚动条距离：', num)
                dr.execute_script('window.scrollTo(0, {});'.format(num))
                sleep(page_time/2)
                return  # 退出两个循环

            elif m == pages:
                print('-'*100, '\n前{}页中没有要查看的文章，请检查填写的文章标题是否正确（注意符号：一般是英文符号）!'.format(pages))
                exit()  # 退出整个程序
            elif i == 9:
                click_next_page(driver)
            else:
                pass

if __name__ == '__main__':
    url = 'https://weixin.sogou.com'
    # keyword = 'zbg'
    # title = '新一线交易所真实数据曝光,ZBG日活超Gate、MXC稳定、Biki数据存疑?'
    # times = 12      # 访问次数
    # pages = 2       # 检查前面多少页的文章
    # page_time = 5   # 文章页面阅读停留时间
    time_out = 20   # 页面加载超时等待时间
    wait_time = 10  # 元素等待超时时间
    gap_time = 0.5  # 元素检查间隔时间

    workbook = xlrd.open_workbook('sougou_weixin_search.xlsx')
    # 根据sheet索引或者名称获取sheet内容，sheet索引从0开始
    sheet = workbook.sheet_by_index(0)
    # 获取指定单元格的值，再转换成整数
    times = int(sheet.cell(1, 2).value)      # 访问次数
    pages = int(sheet.cell(1, 3).value)      # 检查前面多少页的文章
    page_time = int(sheet.cell(1, 4).value)  # 文章页面阅读停留时间
    print('访问次数：{}\n检查前面多少页的文章:{}\n文章页面阅读停留时间:{}'.format(times, pages, page_time))
    # 获取关键字整列数据为数组,并删除第一个元素(Excel表第一个元素不是关键字）
    keyword_cols = sheet.col_values(0)
    keyword_cols.pop(0)
    # 删除url数组中的空元素
    for x in range(0, keyword_cols.count('')):
        keyword_cols.remove('')
    print('搜索的关键字：\n', keyword_cols)
    # 获取标题整列数据为数组,并删除第一个元素
    title_cols = sheet.col_values(1)
    title_cols.pop(0)
    for y in range(0, title_cols.count('')):
        title_cols.remove('')
    print('文章标题：\n', title_cols)
    len_title = len(title_cols)

    m = 0
    while m < times or times == -1:
        m += 1
        random_num = random.randint(0, len_title-1)
        # print('随机数：', random_num)
        keyword = keyword_cols[random_num]
        title = title_cols[random_num]
        dr = webdriver.Chrome()
        dr.set_page_load_timeout(time_out)
        dr.set_script_timeout(time_out)
        try:
            dr.get(url)
            WebDriverWait(dr, wait_time, gap_time).until(EC.presence_of_element_located((By.ID, 'query'))).clear()
            WebDriverWait(dr, wait_time, gap_time).until(EC.presence_of_element_located((By.ID, 'query'))).send_keys(keyword)
            WebDriverWait(dr, wait_time, gap_time).until(EC.presence_of_element_located((By.CLASS_NAME, 'swz'))).click()
            # WebDriverWait(dr, wait_time, gap_time).until(EC.presence_of_element_located((By.ID, 'query'))).send_keys(Keys.ENTER)
        except Exception as message:
            print('打开网址报错，可能是网络断开（一般是切换IP导致）！报错信息如下：\n', message)
        try:
            judge(dr)
        except Exception as message:
            print('查看文章报错！报错信息如下：\n', message)
        try:
            dr.delete_all_cookies()
        except Exception as message:
            print('清除浏览器cookies出现报错，报错信息如下：', message)
        dr.quit()





