from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('http://www.51job.com')
driver.implicitly_wait(10)

#获取当前显示的城市
city = driver.find_element_by_css_selector("#work_position_click  [type='button']")
city.is_selected()
if city.get_attribute('value') != '杭州':#判断显示的城市是否是杭州
    city.click()

    eles = driver.find_elements_by_css_selector('#work_position_click_multiple_selected span')
    for ele in eles:
        time.sleep(2)
        ele.click()


    # work_stations = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em')
    # for work_station in work_stations:
    #     #遍历热门城市，把城市选为杭州
    #     if work_station.text == '杭州' and work_station.get_attribute('class') != 'on':
    #         work_station.click()
    #
    #     if work_station.text != '杭州' and work_station.get_attribute('class') == 'on':
    #         time.sleep(1)
    #         work_station.click()

    driver.find_element_by_id('work_position_click_bottom_save').click()
    driver.findelementby


# driver.find_element_by_id('kwdselectid').send_keys('python')
# driver.find_element_by_css_selector('.ush button').click()
#
# jobs_info = driver.find_elements_by_css_selector('div.dw_table div.el')#把职业列表的每一行用列表保存
# for job_info in jobs_info:
#     infos = job_info.find_elements_by_tag_name('span')#每一行的每一列用列表保存
#     print('{}|{}|{}|{}|{}'.format(infos[0].text,infos[1].text,infos[2].text,infos[3].text,infos[4].text))
#
#
# driver.quit()

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException,TimeoutException
