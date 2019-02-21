from  selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://vip.ytesting.com/loginController.do?login2')
driver.find_element_by_id('userName').send_keys('K201811190787')
driver.find_element_by_id('password').send_keys('1205767706')

# http://localhost:8066/mgr/login/login.html