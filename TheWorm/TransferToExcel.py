# -*-coding:GBK -*-
import json
import codecs
import xlrd
from xlutils.copy import copy


def tran(address, keyWords):
    print("��ʼת��....")
    read_file = 'Excel/demo.xls'
    workbook = xlrd.open_workbook(read_file, formatting_info=False)
    new_book = copy(workbook)
    sheet = new_book.add_sheet(keyWords)
    # sheet = new_book.get_sheet(0)
    sheet.write(0, 0, "��Ʒ����")
    sheet.write(0, 1, "�۸�")
    sheet.write(0, 2, "�������")
    sheet.write(0, 3, "��������")
    colsPointer = 1;

    with codecs.open(address, 'r')as fp:
        json_data = json.load(fp)
        # print (type(json_data))
        data = xlrd.open_workbook('Excel/demo.xlsx')
        for pageSingle in json_data:
            for entry in json_data[pageSingle]:
                name = entry['name'].replace("\n", "")
                link = entry['link']
                price = entry['price']
                comment = entry['comment']
                sheet.write(colsPointer, 0, name)
                sheet.write(colsPointer, 1, price)
                sheet.write(colsPointer, 2, link)
                sheet.write(colsPointer, 3, comment)
                print("��Ʒ����:", name)
                print("��ַ:", link)
                print("�۸�:", price)
                print("����:", comment)
                print("------------------")
                colsPointer += 1
    new_book.save("Excel/demo.xls")


tran("jsonFiles/oppo.json", "oppo")
print("ת��Excel��������")
