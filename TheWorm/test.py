# -*-coding:utf-8-*-
import  codecs
import xlrd
import xlwt

global strin

strin='aaa'

def meth():
    global strin
    for num in range(0,5):
        strin =strin+str(num)+"hello word"
    print (strin)

def writeTest():
    filename = 'jsonFiles/temp.json'
    with codecs.open(filename, 'w') as file_object:
        file_object.write("你好你好")



data = xlrd.open_workbook('Excel/demo.xlsx')
data.sheet_names()
print("sheets：" + str(data.sheet_names()))
table = data.sheet_by_name('京东数据')
print (str(table.nrows))
print (str(table.ncols))
print("整行值：" + str(table.row_values(0)))
print("整列值：" + str(table.col_values(1)))
# print (strin)