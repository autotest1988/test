import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
time.sleep(2)


driver.find_element_by_link_text("新闻").click()

time.sleep(3)

jq = '$("#pane-news > ul:nth-child(2) > li:nth-child(4) > a").click()'

driver.execute_script(jq)


# ele = WebDriverWait(driver=driver, timeout=10, poll_frequency=1).until(lambda x: x.find_element_by_xpath("//*[@id='col-lady']/div[1]/div/h2/a"))
# print(ele)


# target = driver.find_element_by_xpath("//*[@id='col-lady']/div[1]/div/h2/a")

# jq = "argument[0].scrollIntoView()"
#
# driver.execute_script(jq, target)
time.sleep(5)
driver.quit()