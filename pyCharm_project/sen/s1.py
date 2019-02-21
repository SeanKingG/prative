#coding:utf-8

from selenium import webdriver
import  pprint

driver = webdriver.Chrome()
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

#常规

ele = driver.find_element_by_id('forecastID')
citys_info = ele.text
citys_info_list = citys_info.replace('℃','').split('\n')#转化成列表

citys = []
temps = []
city_temps = {}
tempLowest = 100

for info1 in citys_info_list:
    temp = tempLowest

    if '/' not in info1:#根据元素是否包含/判断元素是城市还是温度，并分别存到citys和temps列表
        citys.append(info1)
    else:
        info1_temps = info1.split('/')
        temp = min(int(info1_temps[0]),int(info1_temps[1]))
        temps.append(temp)

    if tempLowest > temp:#遍历的同时找出最低温
        tempLowest = temp

for city,temp in zip(citys,temps):#城市温度保存到字典，用温度做key，最低温度相同的城市保存在同一个列表
    if temp not in city_temps.keys():
        city_temps[temp] = [city]
    else:
        city_temps[temp].append(city)

pprint.pprint(city_temps)
#打印出最低温度，及最低温在字典中对应的值，并用逗号拼接
print("江苏最低的温度为{}℃，城市有{}".format(tempLowest,','.join(city_temps[tempLowest])))
driver.quit()

#CSS

# citys = driver.find_elements_by_css_selector('div#forecastID dt a')
# print(citys[2].text)
# temps = driver.find_elements_by_css_selector('div#forecastID b')
# print(temps[2].text)

#Xpath

# citys = driver.find_elements_by_xpath('//div[@id="forecastID"]/dl/dt/a')
# print(citys[2].text)
# temps = driver.find_elements_by_xpath('//div[@id="forecastID"]/dl/dd/a/b')
# print(temps[2].text)
