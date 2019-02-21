from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
driver.maximize_window()
#设置始发城市
start_city = driver.find_element_by_id('fromStationText')
start_city.click()
start_city.clear()
start_city.send_keys('南京南'+'\n')
#设置终点站
des_city = driver.find_element_by_id('toStationText')
des_city.click()
des_city.clear()
des_city.send_keys('杭州东'+'\n')
#查询
driver.find_element_by_id('query_ticket').click()
# #选择日期
# time.sleep(3)
# driver.find_element_by_xpath("//div[@id='date_range']/ul/li[2]").click()
# #选择出发时间段
# start_time = driver.find_element_by_css_selector('#cc_start_time')
# start_city.click()
# driver.find_element_by_xpath('//select/option[3]').click()


