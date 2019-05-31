def listfunc():
    """
    列表测试
    索引从0开始
    :return:
    """
    list1 = ['Google', 'Runoob', 1997, 2000]

    # 访问列表
    print(list1[0])
    print(list1[1:2])

    # 列表更新
    list1[2] = 2001

    # 删除列表元素
    del list1[2]

    # 在列表末尾追加新的元素
    list1.append('hello')



def tuplefunc():
    """
    元组测试
    与列表不同之处在于，元组内的元素不能修改；元组使用(),不使用()也可以,而列表使用[]
    元组只有一个元素时，需要在元素后面添加逗号


    :return:
    """


def dicfunc():
    """
    字典测试
    :return:
    """

    dic1 = {key1:value1, key2:value2}

    del dic1[key1]
    dic1.clear()
    del dic1



def setfunc():
    """
    集合测试
    :return:
    """
    # 创建一个空集合
    set()
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

    basket.add('hahaha')
    basket.remove('apple')
    # 计算集合长度
    len(basket)
    # 清空集合
    basket.clear()


class Father():
    def fangzi(self):
        print("这是爸爸的房子")
    def chezi(self):
        print("这是爸爸的车子")

class Mother():
    def gongsi(self):
        print("这是妈妈的公司")

class Son(Father, Mother):
    def fangzi(self):
        super(Son, self).fangzi()
        super(Son, self).gongsi()
        print("这是儿子的房子")


if __name__ == '__main__':
        son = Son()
        son.fangzi()
        son.chezi()
        son.gongsi()

        from selenium import webdriver
        from selenium.webdriver.common.by import By


        from selenium.common import exceptions

        d = webdriver.Chrome()
        d.get("http://www.baidu.com")
        d.find_element(By.ID, 'kw').send_keys('python')
