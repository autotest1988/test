from selenium import webdriver
import time;
b=webdriver.Chrome()
c = b.get('http://www.baidu.com')

b.find_element_by_xpath('//*[@id="kw"]').send_keys('python')

b.find_element_by_xpath('//*[@id="su"]').click()


time.sleep(5);


b.find_element_by_xpath('//*[@id="3"]/h3/a').click()

time.sleep(5)
handles = b.window_handles;
handle  = b.current_window_handle;


for i in handles:
    if i== handles:
        continue
    else:
        b.switch_to.window(i)

b.find_element_by_xpath('//*[@id="leftcolumn"]/a[18]').click()


# b.close();

b.quit();

