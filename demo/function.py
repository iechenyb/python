#!/usr/bin/python
import cmath
import time;  # 引入time模块
import calendar
import helloworld
# -*- coding: UTF-8 -*-
#单个参数
def printme(str):
     print(str);
     return str;
#两个参数
def sum(a,b):
      print(a+b)
      return a+b;
#数组参数
def deduplication(self, nums):#找出排序数组的索引

    
    for i in range(len(nums)):
        if nums[i]==self:
            return i
    i=0
    for x in nums:
        if self>x:
            i+=1
    return i


helloworld.hello('iechenyb 999');
helloworld.print_func('iechenyb');
cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:")
print(cal)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) 
 
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())) 
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

ticks = time.time()
print("当前时间戳为:", ticks)

print(cmath.sqrt(9))
dir(cmath)
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
 
print("tup1[0]: ", tup1[0])#逗号为连接符
print("tup2[1:5]: ", tup2[1:5])



list = []        ;  ## 空列表
list.append('Google') ;  ## 使用 append() 添加元素
list.append('Runoob');
print(list);


list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)
del list1[2]
print("After deleting value at index 2 : ")
print(list1)

# 输出 Python 的每个字母
for letter in 'Python':
   if letter == 'h':
      pass
      print('这是 pass 块')
   print('当前字母 :', letter)


#调用函数
arr = [1,2,3]

print(deduplication(5, [1,3,5,6]))
print(sum(1,2));    
printme('aaa');
print(printme('bbbb'));

