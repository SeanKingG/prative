
# from selenium import webdriver
# executable_path = r"d:\webdriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path)
# driver.get("http://www.baidu.com")
# element_keyword = driver.find_element_by_id('kw')
# #element_keyword.send_keys('秦时明月')
# element_search_button = driver.find_element_by_name('tj_trnews')
# element_search_button.click()
# #input('egeghejh')
# #driver.quit()

list_a = [1,2,3,4,5,6,7,8,9]

from functools import reduce
x = [1,2,3,4,5]
y = [1,2,3,4]
z = reduce(lambda x,y:x*y, x)

print(z)

