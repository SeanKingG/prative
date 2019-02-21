from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5'
desired_caps['deviceName'] = '127.0.0.1:21503'

desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] = 'com.ibox.calculators.SplashActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['noKeyboard'] = True
desired_caps['Noreset'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.implicitly_wait(5)

# 定义一个输入任意数字的函数
def num(num):
    for ele in str(num):
        driver.find_element_by_id('com.ibox.calculators:id/digit'+ele).click()
#定义按下等于按钮
def equaBtn():
    driver.find_element_by_id('com.ibox.calculators:id/equal').click()

time.sleep(5)
#进行（3+9）*5运算
num(3)
driver.find_element_by_id('com.ibox.calculators:id/plus').click()#按+号
num(9)
equaBtn()
driver.find_element_by_id('com.ibox.calculators:id/mul').click()#按乘号
num(5)
equaBtn()
#取结果
resultView = driver.find_element_by_id('com.ibox.calculators:id/cv')
result = resultView.find_elements_by_class_name('android.widget.TextView')
print(result[1].text)
#判断
if result[1].text == '60':
    print('pass')
else:
    print('fail')