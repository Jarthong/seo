from selenium import webdriver
from selenium.common.exceptions import TimeoutException

from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

url = 'https://zhidao.baidu.com/question/681663276577227492.html?fr=iks&word=%C8%CB%B9%A4%D6%C7%C4%DC&ie=gbk'
url2 = 'https://zhidao.baidu.com/question/1761173321301311228.html'
url3 = 'https://zhidao.baidu.com/question/572616689.html?fr=iks&word=%C8%CB%B9%A4%D6%C7%C4%DC&ie=gbk'
dr = webdriver.Chrome()
# dr.get()

# sleep(2)
# dr.refresh()

# 我想爬取某网页，该网页加载速度特别慢，所以设置超时时间强制加载
time_out = 2
dr.set_page_load_timeout(time_out)  # 设定页面加载限制时间
dr.set_script_timeout(time_out)
while True:
    try:
        print('打开网站：', url2)
        dr.get(url2)
    except TimeoutException:
        print('加载页面%s秒后超时' %time_out)
        try:
            dr.execute_script('window.stop()')  # 超时后停止加载
        except:
            continue
            # print('continue之后的代码')



# 然后报错，后面的代码都无法执行了,报错信息如下
# selenium.common.exceptions.TimeoutException: Message:Timeout
'''
# dr.find_element_by_class_name('ikonw-qb-new-icon').click()
# dr.find_element_by_class_name('icon-evaluate').click()

# 点击折叠
dr.find_element_by_class_name('show-hide-dispute').click()

# 点击更多回答
# sleep(2)
# dr.find_element_by_id('show-answer-hide').click()

# 点击展开全部
sleep(2)
dr.find_element_by_class_name('wgt-answers-showbtn').click()

# 获取点赞元素组
elements_list = dr.find_elements_by_class_name('icon-evaluate')
print(elements_list)

# 获取回答元素组
# answer_text_list = dr.find_elements_by_class_name('answer-text')[0].text
# answer_text_list2 = dr.find_elements_by_class_name('answer-text')[1].text
answer_text_list = dr.find_elements_by_css_selector('div[accuse="aContent"]')
len_num = len(answer_text_list)
print(answer_text_list)
print('数组个数：', len_num, type(len_num))

# print(answer_text_list)
# print(answer_text_list2)

for i in range(0, len_num):
    answer_text = answer_text_list[i].text
    print('-'*100)
    print(answer_text)
    # if '人工智能' in answer_text:
    #     # dr.find_elements_by_class_name('icon-evaluate')[i].click()
    #     WebDriverWait(dr, 2, 0.1).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'icon-evaluate')))[i].click()


# best_text = dr.find_element_by_class_name('best-text').text



# for i in elements_list:
#     i.click()

# print(best_text)
# print(answer_text)




# 清除浏览器cookies
cookies = dr.get_cookies()
# print(f"main: cookies = {cookies}")
dr.delete_all_cookies()

while True:
    dr.get(url)
    # dr.find_element_by_xpath('//*[@id="evaluate-3015363667"]').click()
    # dr.find_element_by_css_selector('.ikonw-qb-new-icon icon-evaluate ').click()
    # dr.find_element_by_css_selector('input[class="ikonw-qb-new-icon icon-evaluate "]')
    dr.find_element_by_class_name('ikonw-qb-new-icon icon-evaluate icon-evaluate').click()
    # dr.find_element_by_class_name('ikonw-qb-new-icon').click()
    # text = dr.find_element_by_class_name('answer-text mb-10 line').text()
    # print(text)




    # 清除浏览器cookies
    cookies = dr.get_cookies()
    # print(f"main: cookies = {cookies}")
    dr.delete_all_cookies()
    
    
    
                sleep(2)
            try:
                text = dr.find_element_by_class_name('wgt-answers-showbtn').text
                if '展开全部' in text:
                    dr.find_element_by_class_name('wgt-answers-showbtn').click()
                else:
                    pass
            except:
                pass
'''