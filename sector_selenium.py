from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import numpy as np
import time

driver = webdriver.Chrome('C:\project\data_ana\chromedriver.exe')
driver.get("https://kssc.kostat.go.kr:8443/ksscNew_web/kssc/common/ClassificationContent.do?gubun=1&strCategoryNameCode=001&categoryMenu=007&addGubun=no")
driver.implicitly_wait(5)

df = pd.read_csv('C:\\project\\data_ana\\sector.csv', encoding = 'utf-8')
df = df.to_numpy()
not_sorted = []
sorted = []

for i in range(len(df)):
    search_box = driver.find_element_by_xpath('//*[@id="strCategoryCodeName"]')
    search_box.send_keys(df[i][1])
    driver.find_element_by_xpath('//*[@id="ClassificationContentForm"]/div/table/tbody/tr/th[9]/span').click()
    time.sleep(0.8)
    try:
        sort_num = driver.find_element_by_xpath('//*[@id="ksscSearchCommonForm"]/div/table/tbody/tr[1]/td[2]').text
        print(sort_num)
        sort_num = sort_num[0:2]
        sorted.append([df[i][1], sort_num])

    except:
        not_sorted.append(df[i][1])
    
    search_box.clear()

sorted = np.array(sorted)
sorted = pd.DataFrame(sorted)
sorted.to_csv('C:\\project\\data_ana\\대분류.csv', encoding = 'utf-8')
not_sorted = np.array(not_sorted)
not_sorted = pd.DataFrame(not_sorted)
not_sorted.to_csv('C:\\project\\data_ana\\대분류안됨.csv', encoding = 'utf-8')
