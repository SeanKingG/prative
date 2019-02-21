from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get('https://www.vmall.com/')
driver.maximize_window()
driver.implicitly_wait(5)
#获取当前句柄
initial_handle = driver.current_window_handle
#进入官网
driver.find_element_by_css_selector("a[href='http://consumer.huawei.com/cn/']").click()
#获取所有句柄，进入官网窗口
all_webHandles = driver.window_handles
driver.switch_to.window(all_webHandles[1])
#判断主菜单是否符合预期
actual_results1 = driver.find_elements_by_css_selector('div.left-box>ul>li>a')
except_resules1 = ['智能手机','笔记本','平板','智能穿戴','智能家居','更多产品','软件应用','服务与支持']
for actual_result,except_resule in zip(actual_results1, except_resules1):
    if actual_result.text == except_resule:
        print('pass')
    else:
        print('Fail!\n'+'预期结果是：'+except_resule+',实际结果是：'+actual_result.text)
#回到初始窗口，鼠标移到 笔记本&平板
driver.switch_to.window(initial_handle)
notebook = driver.find_element_by_css_selector('#zxnav_1 .category-item-bg')
ActionChains(driver).move_to_element(notebook).perform()
#判断 笔记本&平板 是否符合预期
actual_results2 = driver.find_elements_by_css_selector('#zxnav_1 .category-panels-1 ul a span')
except_resules2 = ['平板电脑','笔记本电脑','笔记本配件']
for actual_result,except_resule in zip(actual_results2,except_resules2):
    if actual_result.text == except_resule:
        print('pass')
    else:
        print('Fail!\n'+'预期结果是：'+except_resule+',实际结果是：'+actual_result.text)



