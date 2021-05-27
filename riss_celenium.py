from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

data = []
all_data = []

count = 1
driver = webdriver.Chrome('C:\Projects\data_ana\chromedriver.exe')
driver.get("http://www.riss.kr/search/Search.do?isDetailSearch=Y&searchGubun=true&viewYn=OP&queryText=znPublisher%2C%EC%9D%B8%ED%95%98%EB%8C%80%ED%95%99%EA%B5%90&strQuery=&exQuery=univ_cd%3A223009%E2%97%88&exQueryText=%EC%88%98%EC%97%AC%EA%B8%B0%EA%B4%80+%5B%EC%9D%B8%ED%95%98%EB%8C%80%ED%95%99%EA%B5%90%5D%40%40univ_cd%3A223009%E2%97%88&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=0&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&image_yn=&gubun=&kdc=&ttsUseYn=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=bib_t&colName=bib_t&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query=")


for page in range(2632):
    try:
        for x in range(10):
            try:
                print(count)
                research = driver.find_element_by_css_selector('#divContent > div.rightContent > div > div.srchResultW > div.srchResultListW > ul > li:nth-child('+str(x+1)+') > div.cont > p.title > a')
                driver.execute_script("arguments[0].click();", research)

                if driver.find_element_by_xpath('//*[@id="thesisInfoDiv"]/div[2]/div[1]/ul/li[6]/span').text == '주제어':
                    data.append([
                        count,
                        driver.find_element_by_xpath('//*[@id="thesisInfoDiv"]/div[1]/h3').text,
                        driver.find_element_by_xpath('//*[@id="thesisInfoDiv"]/div[2]/div[1]/ul/li[1]/div/p').text,
                        driver.find_element_by_xpath('//*[@id="thesisInfoDiv"]/div[2]/div[1]/ul/li[3]/div/p').text,
                        driver.find_element_by_xpath('//*[@id="thesisInfoDiv"]/div[2]/div[1]/ul/li[4]/div/p').text,
                        driver.find_element_by_xpath('//*[@id="thesisInfoDiv"]/div[2]/div[1]/ul/li[6]/div/p').text])

                else:
                    data.append([
                        count,
                        driver.find_element_by_xpath('//*[@id="thesisInfoDiv"]/div[1]/h3').text,
                        driver.find_element_by_xpath('//*[@id="thesisInfoDiv"]/div[2]/div[1]/ul/li[1]/div/p').text,
                        driver.find_element_by_xpath('//*[@id="thesisInfoDiv"]/div[2]/div[1]/ul/li[3]/div/p').text,
                        driver.find_element_by_xpath('//*[@id="thesisInfoDiv"]/div[2]/div[1]/ul/li[4]/div/p').text])

                
                driver.back()

                if count % 10 == 0 :
                    print("----",page,"---"+str(page%10 + 3))
                    

                    element = driver.find_element_by_xpath('//*[@id="divContent"]/div[2]/div/div[3]/a['+str(page%10 + 3)+']')
                    driver.execute_script("arguments[0].click();", element)
                
                count = count + 1
            except:
                continue
    except:
        continue
    
df = pd.DataFrame(data)
df.to_csv("C:\\Projects\\data_ana\\인하대학교_논문.csv", index=False, encoding='utf-8')

#   driver.find_element_by_xpath('//*[@id="divContent"]/div[2]/div/div[3]/a['+str(page%10 + 3)+']').click()
#research = driver.find_element_by_css_selector('#divContent > div.rightContent > div > div.srchResultW > div.srchResultListW > ul > li:nth-child('+str(x+1)+') > div.cont > p.title > a')

#waitpage = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="divContent"]/div[2]/div/div[3]/a['+str(page%10 + 3)+']')))
#            waitpage.click()