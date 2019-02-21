#coding=utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='9'
desired_caps['deviceName']='63607d41'
desired_caps['automationName']='uiautomator2'

# desired_caps['app']=r'C:\Users\Shuqing\Desktop\dr.fone3.2.0.apk'
desired_caps['appPackage']='com.tal.kaoyan'
desired_caps['appActivity']='com.tal.kaoyan.ui.activity.SplashActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['noKeyboard'] = True
desired_caps['Noreset'] = False

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(3)


def check_cancelBtn():
    print('check cancelBtn')

    try:
        cancelBtn = driver.find_element_by_id('android:id/button2')
    except NoSuchElementException:
        print('no cancelBtn')
    else:
        cancelBtn.click()

def check_skipBtn():
    print('check skipBtn')

    try:
        skipBtn = driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
    except NoSuchElementException:
        print('no skipBtn')
    else:
        skipBtn.click()
time.sleep(5)
check_cancelBtn()
check_skipBtn()

driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').clear()
driver.find_element_by_id('com.tal.kaoyan:id/login_email_edittext').send_keys('55555')

driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('zxw2018')
driver.find_element_by_id('com.tal.kaoyan:id/login_login_btn').click()

error_message="用户名或密码错误，你还可以尝试4次"
limit_message="验证失败次数过多，请15分钟后再试"


# message='//*[@text=\'{}\']'.format(error_message)
message='//*[@text="{}"]'.format(limit_message)

print(message)



toast_element =WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath("//*[contains(@text,'，')]"))
 # driver.find_element_by_xpath("//*[contains(@text,'，')]")

print(toast_element.text)