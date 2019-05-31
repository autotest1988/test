from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

'''
driver = webdriver.Chrome()
driver.get('http://sh.ganji.com/')

driver.find_element_by_link_text('租房').click()


time.sleep(5)

print(driver.window_handles)

print(driver.current_window_handle)
print(driver.title)

driver.switch_to.window(driver.window_handles[-1])
print(driver.title)

driver.switch_to.window(driver.window_handles[0])

print(driver.title)
driver.quit()
'''

'''
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
time.sleep(3)

setele = driver.find_element_by_link_text('设置')

ActionChains(driver).move_to_element(setele).perform()

driver.find_element_by_link_text('设置').click()

driver.find_element_by_link_text('搜索设置').click()
#方法1
# driver.find_element_by_id('nr').click()
#
# driver.find_element_by_xpath('//*[@id="nr"]/option[3]').click()


#方法2
time.sleep(2)
#
# ele = driver.find_element_by_id('nr')
#
# time.sleep(3)
#
# Select(ele).select_by_value('50').click()

driver.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()

time.sleep(2)
alert_ele = driver.switch_to.alert
alert_ele.accept()

'''

from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://www.baidu.com"
driver.get(url)

driver.implicitly_wait(3)

jq = '''
    $("#kw").val("")
    $("#kw").val("nihao")
    $("#su").click()
'''

driver.execute_script(jq)




