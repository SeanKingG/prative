#coding:utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(' http://www.51job.com')
#进入高级搜索
driver.find_element_by_css_selector('.more').click()
#输入Python
driver.find_element_by_css_selector('.ipt  #kwdselectid').send_keys('python')
#找到表示当前城市元素
city = driver.find_element_by_css_selector('#work_position_click input')
#把城市定为杭州
if city != '杭州':
    city.click()
    citys_selected = driver.find_elements_by_css_selector('.tin span em')
    for city_selected in citys_selected:
        time.sleep(1)
        city_selected.click()
    driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()
    driver.find_element_by_id('work_position_click_bottom_save').click()
#去掉因输入python自带生成的列表
driver.find_element_by_class_name('b_key').click()
#选职能类别
driver.find_element_by_id('funtype_click').click()
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()
driver.find_element_by_id('funtype_click_bottom_save').click()
#选区域
driver.find_element_by_css_selector('div#cottype_list span.i_arrow').click()
driver.find_element_by_css_selector("div.ul span[title='外资（欧美）']").click()
#选工作年限
driver.find_element_by_css_selector('#workyear_list span').click()
driver.find_element_by_css_selector('.ul span[title="1-3年"]').click()
#点击搜索按钮
driver.find_element_by_css_selector('span.p_but:nth-child(1)').click()
#得到招聘信息
infos = driver.find_elements_by_css_selector('#resultList .el')
#处理招聘信息打印
for info in infos:
    info_units = info.find_elements_by_tag_name('span')
    info_list = list(info_unit.text for info_unit in info_units)
    print('|'.join(info_list))


