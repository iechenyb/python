#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 14:41
# @Author  : Sa.Song
# @Desc    : 
# @File    : read_xls.py
# @Software: PyCharm
import sys
from xlrd import open_workbook # xlrd用于读取xld
import xlwt  # 用于写入xls
workbook = open_workbook(r'F:\python\demo\file\user.xlsx')  # 打开xls文件
sheet_name= workbook.sheet_names()  # 打印所有sheet名称，是个列表
sheet = workbook.sheet_by_index(0)  # 根据sheet索引读取sheet中的所有内容
sheet1= workbook.sheet_by_name('Sheet1')  # 根据sheet名称读取sheet中的所有内容
print(sheet.name, sheet.nrows, sheet.ncols)  # sheet的名称、行数、列数
content = sheet.col_values(0)  # 第1列内容
print(content)
content = sheet.col_values(1)  # 第2列内容
print(content)
#获取行值
content = sheet.row_values(0)
print(content)

#循环遍历
print('循环遍历')
for i in range(sheet.nrows):
   # content = sheet.row_values(i)
    print(sheet.row_values(i))
