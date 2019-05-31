import math;

print('Hello Python！');

str1 = R'aaaaaaaaaaa\\\na===';
print(str1[1:3]);


'''
a= abs(-120);
b = math.ceil(4.1);
print(b);
'''



print(str1.replace('a','b',3));

list1 = ['tongtong','xiaoxigua',123,'ranran','xinxin'];
list2 = ['xixi','mengmeng'];
print(len(list1));
print(list1+list2)
print(list1*2);
del list1[2];
print(list1);




for x in list1+list2:
    print('list元素有：'+x)





if 'tongtong' in list1:
    print("Hello Tong")
else:
    print("Tong is coming soon！")