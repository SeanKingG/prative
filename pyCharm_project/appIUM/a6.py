from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

desire_caps = {}
desire_caps['platformName'] = 'android'
desire_caps['platformVersion'] = '9'
desire_caps['deviceName'] = '111'
desire_caps['appPackage'] = 'io.manong.developerdaily'
desire_caps["appActivity"] = 'io.toutiao.android.ui.activity.LaunchActivity'
desire_caps['noReset'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub',desire_caps)


doc = driver.find_element_by_id('io.manong.developerdaily:id/tv_title')
time.sleep(2)
doc.click()
# doc_title = doc.find_element_by_class_name('android.widget.TextView')
time.sleep(2)
web_doc_title = driver.find_element_by_id('io.manong.developerdaily:id/tv_title')

try:#根据是否有web元素和标题
    # 是否和阅读标签页的标题是否一致，判断通过
    web_doc_title = driver.find_element_by_id('io.manong.developerdaily:id/tv_title')
    driver.find_element_by_class_name('android.webkit.WebView')
    driver.get_screenshot_as_file('a6_1.png')
except Exception as e:
    print('failed\n'+e)
else:
    if doc.text == web_doc_title.text:
        print(doc.text)
        print(web_doc_title.text)
        print('pass')

driver.find_element_by_class_name('android.widget.ImageButton').click()

try:#根据是否有阅读标签页的阅读元素
    # 判断是否返回成功
    driver.find_element_by_id('io.manong.developerdaily:id/tv_tab_title')
    driver.get_screenshot_as_file('a6_2.png')
except NoSuchElementException:
    print('failed back to read_tap')
else:
    print('pass')