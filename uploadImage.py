from selenium import webdriver
import time
import os

email = ""
password = ""

driver = webdriver.Chrome('C:/Users/choon/Downloads/chromedriver_win32/chromedriver')
main_window_handle = driver.current_window_handle

driver.get('https://weverse.io/')
time.sleep(5)

driver.find_element_by_class_name("ixJSsf").click()
signin_window_handle = None
while not signin_window_handle:
    for handle in driver.window_handles:
        if handle != main_window_handle:
            signin_window_handle = handle
            break

time.sleep(3)

driver.switch_to.window(signin_window_handle)

driver.find_element_by_name("username").send_keys(email)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_class_name("gtm-login-button").click()

driver.switch_to.window(main_window_handle)
time.sleep(3)

driver.get("https://weverse.io/weeekly/feed")
time.sleep(3)
driver.find_element_by_class_name("sc-oUoif").send_keys(os.getcwd()+"/images/screenshot.jpeg")
time.sleep(3)
driver.find_element_by_class_name("ql-editor").send_keys("7월도 지그재그~")
# element = driver.find_element_by_xpath("//body")
# element.send_keys("7월도 지그재그~")
# element.send_keys("지그재그_스트리밍 210721/11PM/nichyung/1번째")
driver.find_element_by_class_name("sc-qPwPv").click()
