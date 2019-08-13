from selenium import webdriver
import xlrd, re
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

workbook = xlrd.open_workbook('badu_praise.xlsx')
# 根据sheet索引或者名称获取sheet内容，sheet索引从0开始
sheet = workbook.sheet_by_index(0)
# 获取指定单元格的值，再转换成整数
praise_times = int(sheet.cell(1, 1).value)  # 点赞次数
down_times = int(sheet.cell(1, 2).value)    # 点灭次数
praise_fre = int(sheet.cell(1, 3).value)    # 频率
answer_keyword = sheet.cell(1, 4).value     # 回答中的关键字
print('点赞次数：', praise_times, '\n点灭次数：', down_times, '\n点赞频率：', praise_fre)
print('点赞关键字：', answer_keyword)
# 获取整列数据为数组,并删除第一个元素(Excel表第一个元素不是url）
url_cols = sheet.col_values(0)
url_cols.pop(0)
print('点赞的网址：\n', url_cols)

dr = webdriver.Chrome()

n = 1
while n <= praise_times:
    n += 1
    print('点赞程序开始...')
    for i in url_cols:
        print('此次点赞的网址是：', i)
        try:
            dr.get(i)
        except Exception as message:
            print('打开网站报错，报错信息如下：\n', message)
            sleep(5)
            dr.refresh()

        try:
            text = dr.find_element_by_class_name('show-hide-dispute').text
            if '折叠回答' in text:
                sleep(0.5)
                dr.find_element_by_class_name('show-hide-dispute').click()
            else:
                pass
        except:
            pass
        try:
            text = dr.find_element_by_id('show-answer-hide').text
            if '更多回答' in text:
                sleep(0.5)
                dr.find_element_by_id('show-answer-hide').click()
            else:
                pass
        except:
            pass
        try:
            # 拉动滚动条
            dr.execute_script('window.scrollTo(800,0);')
        except Exception as message:
            print('拉动滚动条出现报错，报错信息如下：', message)
        try:
            # 获取回答元素数组
            answer_text_list = dr.find_elements_by_css_selector('div[accuse="aContent"]')
            len_num = len(answer_text_list)
            # 判断满足关键字的回答，进行点赞
            for j in range(0, len_num):
                answer_text = answer_text_list[j].text
                # print('-' * 100)
                # print(answer_text)
                # 判断关键字是否在回答的文本中，re.I不区分大小写，使用bool()返回布尔值，非空为True
                if bool(re.search(answer_keyword, answer_text, re.I)):
                    # dr.find_elements_by_class_name('icon-evaluate')[j].click()
                    WebDriverWait(dr, 5, 0.1).until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, 'icon-evaluate')))[j].click()
        except Exception as message:
            print('点赞出现报错，报错信息如下：', message)

    # 清除浏览器cookies
    try:
        cookies = dr.get_cookies()
        # print(f"main: cookies = {cookies}")
        dr.delete_all_cookies()
    except Exception as message:
        print('清除浏览器cookies出现报错，报错信息如下：', message)

m = 1
while m <= down_times:
    m += 1
    # print('等待%s秒后再进入下一个循环...' %praise_fre)
    # sleep(praise_fre)
    print('点灭程序开始...')
    for i in url_cols:
        print('此次点灭的网址是：', i)

        try:
            dr.get(i)
        except Exception as message:
            print('打开网站报错，报错信息如下：\n', message)
            print('网页卡死，重启浏览器...')
            dr.close()
            dr = webdriver.Chrome()
            dr.get(i)

        try:
            text = dr.find_element_by_class_name('show-hide-dispute').text
            if '折叠回答' in text:
                sleep(0.5)
                dr.find_element_by_class_name('show-hide-dispute').click()
            else:
                pass
        except:
            pass
        try:
            text = dr.find_element_by_id('show-answer-hide').text
            if '更多回答' in text:
                sleep(0.5)
                dr.find_element_by_id('show-answer-hide').click()
            else:
                pass
        except:
            pass
        try:
            # 拉动滚动条
            dr.execute_script('window.scrollTo(800,0);')
        except Exception as message:
            print('拉动滚动条出现报错，报错信息如下：', message)

        try:
            # 获取回答元素数组
            answer_text_list = dr.find_elements_by_css_selector('div[accuse="aContent"]')
            len_num = len(answer_text_list)
            # 判断满足关键字的回答，进行点灭
            for j in range(0, len_num):
                answer_text = answer_text_list[j].text
                # 判断关键字是否在回答的文本中，re.I不区分大小写，使用bool()返回布尔值，非空为True
                if bool(re.search(answer_keyword, answer_text, re.I)):
                    WebDriverWait(dr, 2, 0.1).until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, 'icon-evaluate-bad')))[j].click()
        except Exception as message:
            print('点赞出现报错，报错信息如下：', message)

    # 清除浏览器cookies
    try:
        cookies = dr.get_cookies()
        # print(f"main: cookies = {cookies}")
        dr.delete_all_cookies()
    except Exception as message:
        print('清除浏览器cookies出现报错，报错信息如下：', message)
