# import selenium;
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# b = webdriver.Chrome()

# =========================鼠标事件================================
# b.get('http://maiziedu.com')
#
# ele1 = b.find_element_by_link_text('企业直通班')
#
# ActionChains(b).move_to_element(ele1).perform();
#
# ele2 = b.find_element_by_link_text('软件测试')
#
# ele2.click()

# =========================键盘事件================================
# b.get('http://www.baidu.com')
# b.maximize_window()
# ele2 = b.find_element_by_id('kw');
# ele2.send_keys('python123')
# from selenium.webdriver.common.keys import Keys
# import time
# time.sleep(5)
# ele2.send_keys(Keys.BACKSPACE)
# time.sleep(2)
# ele2.send_keys(Keys.BACKSPACE)
# time.sleep(2)
# ele2.send_keys(Keys.BACKSPACE)
# time.sleep(2)
#
# ele3 = b.find_element_by_link_text('python web开发')
# print(ele3.text)
# ele2.send_keys(Keys.CONTROL,'a')
# time.sleep(2)
# ele2.send_keys(Keys.CONTROL,'x')
# time.sleep(2)
# ele2.send_keys(Keys.CONTROL,'v')
# time.sleep(2)
#
# b.quit();

# =================窗口-对话框===================
# b.get('http://www.maiziedu.com')
# import time
# time.sleep(10)
# ele = b.find_element_by_id('textarea')
# print(ele.get_attribute('id'))
# time.sleep(5)
# ele.send_keys('hello')
# time.sleep(5)
# b.quit();

# =====================窗口-登陆窗口===================
# try
#     b.find_element_by_link_text('1243243')
#     print('88888')
# except:
#     print('000000')
