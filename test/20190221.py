from selenium import webdriver
import time

driver = webdriver.Chrome();

driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('python')

driver.find_element_by_id('su').click()

time.sleep(3)

search_window = driver.current_window_handle #定位当前页面

driver.find_element_by_xpath('//*[@id="2"]/h3/a').click()

time.sleep(20)

handles = driver.window_handles
print('1:')
print(handles)
print('2:')
print(driver.current_window_handle)
for handle in handles:
    if handle != driver.current_window_handle:
        print('3:')
        print('switch to second handle',handle)
        driver.switch_to.window(handle)
print('4:')
print(driver.current_window_handle)

driver.find_element_by_xpath('//*[@id="leftcolumn"]/a[19]').click()

time.sleep(5)

driver.quit()
