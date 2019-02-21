#coding:utf-8
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

desire_caps = {}
desire_caps['platformName'] = 'android'
desire_caps['platformVersion'] = '5'
desire_caps['deviceName'] = '127.0.0.1:21503'
desire_caps['appPackage'] = 'com.sqauto'
desire_caps["appActivity"] = 'com.sqauto.MainActivity'
desire_caps['noReset'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub',desire_caps)
#滑动开始点
ele0 = driver.find_element_by_id('cramp fast')
location0 = ele0.location
size0 = ele0.size
start_x = location0['x'] + int(size0['width'])*0.5
start_y = location0['y'] + int(size0['height'])
#滑动结束点
ele1 = driver.find_element_by_id('songqin recommend')
location1 = ele1.location
size1 = ele1.size
end_x = location1['x'] + int(size1['width'])*0.5
end_y = location1['y'] + int(size1['height'])

while True:#第一层循环，一直滑动，直到在界面同时找到口碑最佳和用户最爱
    try:#滑动，找口碑最佳和用户最爱
        driver.swipe(start_x, start_y/2, end_x, end_y/2)
        best_reputation = driver.find_element_by_id('best reputation')
        user_favorite = driver.find_element_by_id('user favorite')
    except NoSuchElementException:#没找到就pass 继续循环
        pass
    else:#找到元素，进行数据处理及break结束循环
        #找到界面所有元素
        eles = driver.find_elements_by_xpath('//android.widget.ScrollView/android.view.View/*')
        # print(len(eles))

        eles_text = []#存放界面可视元素
        for ele in eles:
            eles_text.append(ele.text)

        for ele_text in eles_text:#去除列表中的空元素
            try:
                eles_text.remove('')
            except ValueError:
                pass

        for ele_text in eles_text:#获取口碑最佳的元素的索引
            if ele_text == '口碑最佳':
                best_reputation_index = eles_text.index(ele_text)
                break
        #口碑最佳下第一个软件名的索引
        best_reputation_app_index = best_reputation_index + 1
        #根据数据结构，取口碑最佳到用户最爱之间的软件名
        while True:
            if eles_text[best_reputation_app_index] == '用户最爱':
                break
            print(eles_text[best_reputation_app_index])
            best_reputation_app_index += 2

        break
