
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class Tcall():
    def __init__(self, a):
        print(a)

    def __call__(self, *args, **kwargs):
        for i in args:
            print(i)

if __name__ == "__main__":
        a = (1, 2, 3, 4, 5, 'a', 'b')
        tcall = Tcall("hello")
        tcall(a)
        # driver = webdriver.Chrome()
        # driver.get("http://www.baidu.com")
        # result1 = EC.title_is("百度")(driver)
        # print(result1)

        locator = ('id','kw')
        # result2 = EC.presence_of_element_located(locator)(driver)
        # print(result2)
        # result2.send_keys("加油")

        # result3 = WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(locator))
        # print(result3)
        # assert result

        # locator1 = (By.ID, "su")
        # result4 = WebDriverWait(driver, timeout=10).until(EC.text_to_be_present_in_element_value(locator1, "百度xxx"),"StaleElementReferenceException")
        # print(result4)

        # driver.get("https://www.jianshu.com/p/c4473018807c")
        #
        # time.sleep(5)
        #
        # jsScript = "window.scrollTo(0, document.body.scrollHeight)"
        #
        # driver.execute_script(jsScript)
        #
        # time.sleep(3)
        #
        # jsScript1 = "window.scrollTo(0, 0)"
        #
        # driver.execute_script(jsScript1)
        #
        # time.sleep(5)
        #
        # element = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[4]')
        #
        # jsScript2 = "arguments[0].scrollIntoView()"
        #
        # driver.execute_script(jsScript2,element)

        print("你好，我是%s，我今年%s岁了"%('哈哈',5))


         