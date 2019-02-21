from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = '63607d41'

desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] = 'com.ibox.calculators.SplashActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['noKeyboard'] = True
desired_caps['Noreset'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

# 定义一个输入任意数字的函数
def num(num):
    for ele in str(num):
        #print(ele)
        driver.find_element_by_xpath('//android.widget.Button[@text="{}"]'.format(ele)).click()
        #print(driver.find_element_by_xpath('//android.widget.Button[@text="{}"]'.format(ele)).text)
#定义按下等于按钮

def equaBtn():
    driver.find_element_by_xpath('//android.widget.Button[@text="{}"]'.format('=')).click()

time.sleep(5)
#进行（3+9）*5运算
num(3)
driver.find_element_by_xpath('//android.widget.Button[@text="{}"]'.format('+')).click()#按+号
num(9)
equaBtn()
driver.find_element_by_xpath('//android.widget.Button[@text="{}"]'.format('×')).click()#按乘号
num(5)
equaBtn()
#取结果
result = driver.find_element_by_xpath\
    ('//android.widget.RelativeLayout/android.widget.TextView[2]')

print(result.text)
#判断
if result.text == '60':
    print('pass')
else:
    print('fail')