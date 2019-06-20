#coding:utf-8
from selenium import webdriver
import unittest
import time


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.driver = webdriver.Chrome()

    def setUp(self):
        print("setUp")
        self.driver.get("http://www.baidu.com")

    def get_login_username(self):
        try:
            t = self.driver.find_element_by_css_selector("#userMenu>a").text
            print(t)
            return t
        except:
            return ""

    def is_alert_exist(self):
        try:
            time.sleep(2)
            t = self.driver.switch_to.alert
            result = t.text
            t.accept()
            return result
        except:
            return ""

    def test_01(self):
        time.sleep(2)
        self.driver.find_element_by_id("account").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_id("submit").click()
        time.sleep(2)
        result = self.get_login_username()
        print("获取的结果:%s" % result)
        self.assertTrue(result == "admin")


    def test_02(self):
        time.sleep(2)
        self.driver.find_element_by_id("account").send_keys("admin123")
        self.driver.find_element_by_id("password").send_keys("")
        self.driver.find_element_by_id("submit").click()
        time.sleep(2)
        self.is_alert_exist()
        result = self.get_login_username()
        print("获取的结果:%s" % result)
        self.assertTrue(result == "admin")

    def tearDown(self):
        print("tearDown")
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
        cls.driver.quit()



if __name__ == "__main__":
    unittest.main()