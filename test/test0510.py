from  selenium import webdriver
import  time

option = webdriver.ChromeOptions()

option.add_argument(r'--user-data-dir=C:\Users\PC\AppData\Local\Google\Chrome\User Data\Default')


driver = webdriver.Chrome(chrome_options=option)

driver.get('http://www.baidu.com');

driver.quit()
