#-*-coding:GBK -*-
import sys
import json
import codecs
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
global driver
global jsonf
global pageNum
driver = webdriver.Chrome()
driver.get("https://www.jd.com")



"""
��ȡ��ǰҳ����������ݣ��Ƚ���ȡ����ͨ��ƴ���ַ�������jsonf�ַ�����
"""
def parsePage():
    global driver
    global jsonf
    global pageNum
    print ("�����"+str(pageNum)+"ҳ,��ʼ��ȡ��ǰҳ������...")
    time.sleep(3)
    target = driver.find_element_by_id("J_bottomPage")  # ���ﶨλ��ʽֻҪ�ܶ�λ��Ԫ�ؾ��У������ַ�ʽ����
    driver.execute_script("arguments[0].scrollIntoView();", target)
    time.sleep(5)
    entry = driver.find_elements_by_xpath('//div[@class="gl-i-wrap"]')

    jsonf = jsonf+'"page'+str(pageNum)+'":['
    for index, singleEntry in enumerate(entry):
        link = singleEntry.find_element_by_class_name('p-name').find_element_by_tag_name('a').get_attribute('href')
        name = singleEntry.find_element_by_class_name('p-name').find_element_by_tag_name('a').find_element_by_tag_name('em').text
        price = singleEntry.find_element_by_class_name('p-price').find_element_by_tag_name('strong').find_element_by_tag_name('i').text
        comment = singleEntry.find_element_by_class_name('p-commit').find_element_by_tag_name('strong').find_element_by_tag_name('a').text
        jsonfile = {"name": name,
                    "price": price,
                    "link": link,
                    "comment": comment
                    }
        jsonString = json.dumps(jsonfile, ensure_ascii=False)
        if (index==len(entry)-1):
            jsonf = jsonf + jsonString + '\n'
            break
        jsonf=jsonf+jsonString+',\n'
    jsonf=jsonf+"]"
    print ("��ɵ�ǰҳ��������ȡ���ɹ���¼�뻺��...")
    pageNum = pageNum+1

"""""
��ת����һҳ��ÿ��ִ�������������Jsonf��ƴ�룬�ַ�
"""""
def nextPage():
    print ("��ת��һҳ...")
    global driver
    global jsonf
    jsonf=jsonf+','
    driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]').click()
    jsonf
    time.sleep(3)

def writeJsonFile(jsonFileName):
    print ('��ʼд����json�ļ�:'+jsonFileName+"...")
    global driver
    global jsonf
    filename = jsonFileName
    with codecs.open(filename, 'w') as file_object:
        # file_object.write(jsonf.encode('utf-8'))
        file_object.write(jsonf)
    print ("д�����...")

"""
@:param pageRange: ��ȡҳ����Χ
@:param keyWords: ��Ҫ�����Ĺؼ���
@:param jsonFileName: ��Ҫ����json�ļ�������
"""
def startEntry(pageRange,keyWords,jsonFileName):
    print ("��ʼ��ȡ����: �ؼ���:"+keyWords+",��ȡҳ����Χ:1~"+str(pageRange)+"ҳ")
    global driver
    global jsonf
    global pageNum
    pageNum = 1
    jsonf = '{'
    # driver.find_element_by_xpath('//*[@id="key"]').send_keys(keyWords.decode('gb18030'))
    driver.find_element_by_xpath('//*[@id="key"]').send_keys(keyWords)
    button = driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button')
    button.click()
    time.sleep(3)
    for index in range(0,pageRange):
        parsePage()
        if(index!=(pageRange-1)):
            nextPage()
    jsonf = jsonf + "}"
    writeJsonFile(jsonFileName)
    # print jsonf
    print("���������ȡ...")

def transferToExcel(address):
    print ("��ʼд��Excel...")

startEntry(1,'oppo','jsonFiles/oppo.json')


