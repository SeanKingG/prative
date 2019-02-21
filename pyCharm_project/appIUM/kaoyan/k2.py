from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['paltformVersion'] = '4'

desired_caps['appPackage'] = 'com.tal.kaoyan'
desired_caps['appActivity'] = 'com.tal.kaoyan.ui.activity.SplashActivity'
desired_caps['noReset'] = 'True'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(4)

def check_cancelBtn():
    print('check cancelBtn')

    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('no cancelBtn')
    else:
        cancelBtn.click()

def check_skipBtn():
    print('check skipBtnn')

    try:
        skiipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no skipBtn')
    else:
        skiipBtn.click()

check_cancelBtn()
check_skiipBtn()
