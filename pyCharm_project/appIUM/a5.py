from appium import webdriver
import time

desire_caps = {}
desire_caps['platformName'] = 'android'
desire_caps['platformVersion'] = '9'
desire_caps['deviceName'] = '127.0.0.1:21503'
desire_caps['appPackage'] = 'com.example.jcy.wvtest'
desire_caps["appActivity"] = 'com.example.jcy.wvtest.MainActivity'
desire_caps['noReset'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub',desire_caps)

contexts = driver.contexts
print(contexts)

driver.switch_to.context('WEBVIEW_com.example.jcy.wvtest')
driver.find_element_by_id('index-kw').send_keys('松勤')
driver.find_element_by_id('index-bn').click()

driver.switch_to.context('NATIVE_APP')

driver.find_element_by_id('com.example.jcy.wvtest:id/navigation_notifications').click()
driver.get_screenshot_as_file('web.png')