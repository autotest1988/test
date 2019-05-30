# 鼠标悬停事件
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

ele = driver.find_element_by_link_text('设置')

ActionChains(driver).move_to_element(ele).perform()

driver.find_element_by_link_text('搜索设置').click()

time.sleep(5)

driver.find_element_by_link_text('保存设置').click()

time.sleep(10)

driver.switch_to.alert.accept()

time.sleep(10)

driver.quit()
'''


'''
# 键盘事件
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('python1')

time.sleep(2)

driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)

time.sleep(2)

driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')

time.sleep(5)

driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

time.sleep(5)

driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')

time.sleep(5)

driver.find_element_by_id('su').click()

time.sleep(5)

driver.quit()

'''

# ifrme切换

from selenium import webdriver
import  time
driver = webdriver.Chrome()
driver.get('https://mail.126.com/')
time.sleep(5)

# frame = driver.find_element_by_tag_name("iframe")
# print(type(frame))

# e = driver.find_element_by_id("x-URS-iframe1557740767295.987")
# print(e)


# e1 = driver.find_element_by_xpath(r'//*[@id="x-URS-iframe1557740767295.987"]')
# print(e1)


driver.switch_to.frame(0)
email_ele = driver.find_element_by_name('email').send_keys("haha")

driver.switch_to.parent_frame()//返回上一级iframe
driver.switch_to.default_content()//回到主界面


time.sleep(5)

driver.quit()