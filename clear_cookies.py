from selenium import webdriver

dr = webdriver.Chrome()
dr.get('https://www.baidu.com')

# 清除浏览器cookies
try:
    cookies = dr.get_cookies()
    # print(f"main: cookies = {cookies}")
    dr.delete_all_cookies()
except Exception as message:
    print('清除浏览器cookies出现报错，报错信息如下：', message)

dr.close()
dr = webdriver.Chrome()
dr.get('https://www.baidu.com')
