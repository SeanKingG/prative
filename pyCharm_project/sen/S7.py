from selenium import webdriver
import win32com.client
import time
driver = webdriver.Chrome()
driver.get('https://tinypng.com/ ')

driver.find_element_by_css_selector('.target figure').click()

time.sleep(1)
shell = win32com.client.Dispatch("WScript.Shell")
shell.Sendkeys(r'C:\Users\Administrator\Desktop\S6.png'+'\r')
