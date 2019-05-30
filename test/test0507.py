# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
#
#
# def get_ele_times(driver,times,func):
#     return WebDriverWait(driver,times).until(func)
#
# def open_browser():
#     return webdriver.Chrome();
#
# def test():
#     b = open_browser()
#     b.get('https://www.baidu.com');
#     b.maximize_window();
#     ele1 = get_ele_times(b, 30, lambda a:b.find_element_by_xpath('//*[@id="u1"]/a[7]'))
#     print(ele1.text)
#     ele1.click();
#
#     ele_acc = b.find_element_by_id('account');
#
#     ele_acc.click()
#     ele_acc.send_keys(account);
#
#     ele_pwd = b.find_element_by_id('pwd')
#     ele_pwd.clear()
#     ele_pwd.send_keys(pwd)
#
#     b.find_element_by_id('submit').clear()
#
#     b.quit();
#
#
#     b.switch_to.alert.accept();


# 元组tuple
def testTpu():
    return 'a', 'b', 'c'


# 元组tuple
def testTpu1():
    return ('a', 'b', 'c', 'd', 'e')

# 列表list
def testList():
    return [1,2,3,4,5]

# 字典dict
def testDic():
    return {'a': 1, 'b': 2, 'c': 3};

def sendValues(ele_dict,tuplea):
    # send_keys   tuplea是元素,ele_dict是具体的data
    for i in

        tuplea[1].send_keys(ele_dict['userid'])



def testtpule():
    res = testTpu();
    print(type(res))
    print(isinstance(res, tuple))
    print()

    print(type(testTpu1()))
    print(isinstance(testTpu1(),tuple))
    print(testTpu1())
    print(testTpu1()[0])     #访问元组tuple
    print(testTpu1()[1:4])  #访问元组tuple


    print(type(testList()))
    print(isinstance(testList(),list))
    print(testList())
    print(testList()[0])    #访问list
    print(testList()[1:4])  #访问list

    print(type(testDic()))
    print(isinstance(testDic(),dict))
    print(testDic())
    print(testDic()['a'])    #访问字典里的值

if __name__ == '__main__':
    # testtpule();
    dic = testDic();
    if 'ab' in dic:
        print('right')
    else:
        print('wrong')
