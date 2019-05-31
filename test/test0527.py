from selenium import webdriver
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time


k = PyKeyboard()
s = "hello,haha"
for i in s:
    k.tap_key(i)


# driver = webdriver.Chrome()
# driver.get("https://www.12306.cn/index/")
# time.sleep(10)
# js = 'document.getElementById("train_date").removeAttribute("readonly");' \
#      'document.getElementById("train_date").value="";' \
#      'document.getElementById("train_date").value="2019-10-28"'
#
# driver.execute_script(js)
# #
# # driver.find_element_by_id("train_date").clear()
# # driver.find_element_by_id('train_date').send_keys("2019-10-28")

