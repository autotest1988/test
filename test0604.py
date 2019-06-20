#复习
"""
l = [1, 2, 3, 4, 5]

l.append(6)
print(l)
l.remove(2)
print(l)

del l[2]


print(l)
l[2] = 8
print(l)

l.pop(-1)

print(l)

print(len(l))
l.append(0)
print(l)
l.sort()
print(l)
l.append(3)
print(l)
print(l.count(3))


s = 0
for i in range(10):
    s+=i
print(s)


#0-100中的奇数累加
s = 0
for i in range(1,100,2):
    if s > 1000:
        break
    else:
        pass
    s += i
    print(i)
print(s)
"""


"""
import random

key = random.randint(1,100)
print(key)
a = 1
b = 100
while 1:
    guess = int(input("请输入一个%s"%a + "到%s"%b + "之间的整数："))
    if guess > a and  guess < key:
        a = guess
        # print("请输入一个%s"%a + "到%s"%b + "之间的整数：")
    elif guess > key and guess < b:
        b = guess
        # print("请输入一个%s"%a + "到%s"%b + "之间的整数：")
    elif guess > b or guess < a:
        print("输入错误")
    elif guess == key:
        print("答对了")
        break
"""

"""
#冒泡排序
list1 = [3, 2, 1, 9, 10, 78, 6]
# key = 0
# for i in list1:
#     key1 = key + 1
#     for j in list1[key+1:]:
#         if i > j:
#             tmp = list1[key]
#             list1[key] = list1[key1]
#             list1[key1] = tmp
#         key1 += 1
#
#     key += 1
print(list1)
list_len = len(list1)
for i in range(list_len-1):
    for j in range(list_len-1-i):
        print(j)
        print("==========")
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
        print(list1)

print(list1)
"""
"""
#快速排序=====================================================？？？？？？

list1 = [3, 2, 1, 9, 10, 78, 6]
list1_len = len(list1)

"""
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
"""
#求出现次数最多的元素
def maxStr(a):
    tmp = 0
    for i in a:
        if a.count(i) > tmp:
            max_str = i
            tmp = a.count(i)
    return max_str

def bubbleSort(a):
    lenth = len(a)
    for i in range(lenth-1):
        for j in range(lenth-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# res = bubbleSort(a)
# print(res)

def quChong(a):
    print(a)
    # res = []
    # for i in a:
    #     if i not in res:
    #         res.append(i)
    res = list(set(a))
    return res

result = quChong(a)
print(result)
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(6)
# ele = driver.find_element_by_xpath("//*[@class='setting-text']")
# # ele = driver.find_element_by_link_text("设置")
# ActionChains(driver).move_to_element(ele).perform()
# ele1 = driver.find_element_by_link_text("搜索设置")
# ele1.click()
# time.sleep(2)
# ele2 = driver.find_element_by_name("NR")
# # Select(ele2).select_by_index(2)
# # Select(ele2).select_by_value("20")
# # Select(ele2).select_by_visible_text("每页显示50条")
# driver.find_element_by_xpath("//*[@id='nr']//option[2]").click()
# time.sleep(3)
# driver.find_element_by_link_text("保存设置").click()
# time.sleep(3)
# ele6 = driver.switch_to.alert
# print(ele6.text)
# ele6.accept()
s = driver.find_element_by_css_selector("#su").is_displayed()
print(s)

"""
#打印99乘法表
for i in range(1,10):
    if i == 1:
        print("1*1=1")
    else:
        for j in range(1, i+1):
            print("%s*%s=%s"%(j,i,i*j), end="   ")
        print("\n", end="")

#求三位数的水仙花数
count = 0
for i in range(99,1000):
    res = 0
    for j in str(i):
        res += int(j)*int(j)*int(j)
    if i == res:
        count += 1
        print(i)
print(count)
"""














