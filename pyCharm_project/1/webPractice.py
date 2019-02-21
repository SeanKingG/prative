# import time
#
# from selenium import webdriver
# driver = webdriver.Chrome()
# # driver.get('http://www.baidu.com')
# #
# # element_keyword = driver.find_element_by_id('kw')
# # element_keyword.send_keys('秦时明月')
#
# # element_search_button = driver.find_element_by_id('su')
# #
# # element_search_button.click()
# # driver.quit()
#
# # driver.get('http://weather.sina.com.cn/china/guangdongsheng/')
# # ele_all = driver.find_element_by_id('wd_city')
# # first = ele_all.find_element_by_name('43-48-32-38-30-31')
# # href = ele_all.get_attribute('href')
# # outerHtml = ele_all.get_attribute('outerHTML')
# # innerHtml = ele_all.get_attribute('innerHTML')
# # print(first.text)
# # driver.quit()
# from bs4 import BeautifulSoup
# driver.get('http://weather.sina.com.cn')
# #等待：sleep
# import time
# time.sleep(2)#全局等待时间
# # driver.implicitly_wait(3)
# # driver.implicitly_wait(0)#局部等待时间
#
# # driver.find_element_by_link_text('广西').click()
# time.sleep(3)
# driver.find_element_by_css_selector('a[href * = "guangxizizhiqu"]').click()
# city1 = driver.find_element_by_css_selector('div#wd_city :eth-child(2)')
# print(city1.text)
from selenium import webdriver
import pprint


# 指定是chrome 的驱动
# 执行到这里的时候Selenium会去到指定的路径将chrome driver 程序运行起来

driver = webdriver.Chrome()

# get 方法 打开指定网址
driver.get('http://www.baidu.com')
# pprint.pprint(driver.get_cookies())
print(driver.get_cookies())

# 查找到那个搜索输入栏网页元素，返回一个表示该元素的WebElement对象。
element_keyword = driver.find_element_by_id("kw")

# 输入字符
element_keyword.send_keys('松勤')

# 找到搜索按钮
element_search_button = driver.find_element_by_id("su")
# 点击该元素
element_search_button.click()



# 最后，driver.quit让浏览器和驱动进程一起退出。不然会有好几个实例一起运行

# driver.quit()

