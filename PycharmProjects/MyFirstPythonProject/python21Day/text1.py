#!/usr/bin/python
# -*- coding:utf8 -*-

'''对已有的计算0-100的while循环进行改造，通过增加continue语句，使得只计算奇数的和'''

sum = 0  #奇数的话，从0开始就好
x = 0
while True: #进入while循环，若不加限制条件，会无限循环
    x = x + 1 #枚举所有的正整数
    if x > 100: #当x枚举到100时，
        break  #跳出循环
    if x % 2 == 0: #又当x除以2，余数为0时，（判断为偶数）
        continue #不继续循环，进入下一循环
    sum = sum + x #求和
print(sum)


'''对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。

'''
#方法一：
for x in range(1,9):
    for y in range (x+1,10): #取y比x至少大1，一直到10的枚举
        print (str(x)+ str(y))

#方法二：
for x in [1,2,3,4,5,6,7,8,9]:
    for y in [1,2,3,4,5,6,7,8,9,0]:
        if x<y :
            print (x*10 + y)


'''根据dict中的内容，一一打印出来'''
#方法一：
d = {'Adam':95 , 'Lisa':85 , 'Bart':59}
for key in d :
    print (key,':',d[key])

#方法二：
d = {'Adam':95 , 'Lisa':85 , 'Bart':59}
for k,v in d.items():
    print (k,':',v)
