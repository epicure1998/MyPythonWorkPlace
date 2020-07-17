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
爬取当前页面的所有数据，先将爬取数据通过拼接字符串存入jsonf字符串中
"""
def parsePage():
    global driver
    global jsonf
    global pageNum
    print ("进入第"+str(pageNum)+"页,开始爬取当前页面数据...")
    time.sleep(3)
    target = driver.find_element_by_id("J_bottomPage")  # 这里定位方式只要能定位到元素就行，用那种方式都行
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
    print ("完成当前页面数据爬取，成功过录入缓存...")
    pageNum = pageNum+1

"""""
跳转到下一页，每次执行完这个函数在Jsonf中拼入，字符
"""""
def nextPage():
    print ("跳转下一页...")
    global driver
    global jsonf
    jsonf=jsonf+','
    driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]').click()
    jsonf
    time.sleep(3)

def writeJsonFile(jsonFileName):
    print ('开始写入至json文件:'+jsonFileName+"...")
    global driver
    global jsonf
    filename = jsonFileName
    with codecs.open(filename, 'w') as file_object:
        # file_object.write(jsonf.encode('utf-8'))
        file_object.write(jsonf)
    print ("写入完成...")

"""
@:param pageRange: 爬取页数范围
@:param keyWords: 需要搜索的关键字
@:param jsonFileName: 需要存入json文件的名称
"""
def startEntry(pageRange,keyWords,jsonFileName):
    print ("开始爬取数据: 关键词:"+keyWords+",爬取页数范围:1~"+str(pageRange)+"页")
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
    print("完成数据爬取...")

def transferToExcel(address):
    print ("开始写入Excel...")

startEntry(1,'oppo','jsonFiles/oppo.json')


