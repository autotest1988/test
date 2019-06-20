from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
ele = WebDriverWait(driver=driver, timeout=10, poll_frequency=1).until(lambda x:x.find_element_by_id("kw"))


title = "百度一下，你就知道"
result = EC.title_is(title=title)
print(result(driver))

res = EC.title_contains(title="百度")(driver)
print(res)


res1 = EC.presence_of_element_located(locator=('id', 'kw'))(driver)
print(res1)

res2 = EC.text_to_be_present_in_element(locator=("link text", "设置"), text_="设置1")(driver)
print(res2)
time.sleep(3)
driver.quit()


try:
    WebDriverWait(driver=driver, timeout=3, poll_frequency=1).until(lambda x:EC.text_to_be_present_in_element(locator=("link text", "设置"), text_="设11"))
    print("1111111111")
except TimeoutError:
    print("2222222")