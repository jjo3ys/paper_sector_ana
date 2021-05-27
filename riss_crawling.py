import csv
import math
import requests

from bs4 import BeautifulSoup

url = 'http://www.riss.kr/search/Search.do?isDetailSearch=Y&searchGubun=true&viewYn=OP&queryText=znPublisher%2C%EC%9D%B8%ED%95%98%EB%8C%80%ED%95%99%EA%B5%90&strQuery=&exQuery=univ_cd%3A223009%E2%97%88&exQueryText=%EC%88%98%EC%97%AC%EA%B8%B0%EA%B4%80+%5B%EC%9D%B8%ED%95%98%EB%8C%80%ED%95%99%EA%B5%90%5D%40%40univ_cd%3A223009%E2%97%88&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=0&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&image_yn=&gubun=&kdc=&ttsUseYn=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=bib_t&colName=bib_t&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query='
responese = requests.get(url)

html = responese.text
soup = BeautifulSoup(html, 'lxml')
total_count = soup.select_one('#divContent > div.rightContent > div > div.searchBox.pd > dl > dd > span > span').get_text()
total_count = int(total_count.replace(',', ''))

total_page_num = math.ceil(total_count/10)

for i in range(total_page_num):
    detail_list = []
    url = 'http://www.riss.kr/search/Search.do?isDetailSearch=Y&searchGubun=true&viewYn=OP&queryText=znPublisher%2C%EC%9D%B8%ED%95%98%EB%8C%80%ED%95%99%EA%B5%90&strQuery=&exQuery=univ_cd%3A223009%E2%97%88&exQueryText=%EC%88%98%EC%97%AC%EA%B8%B0%EA%B4%80+%5B%EC%9D%B8%ED%95%98%EB%8C%80%ED%95%99%EA%B5%90%5D%40%40univ_cd%3A223009%E2%97%88&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount={0}&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&image_yn=&gubun=&kdc=&ttsUseYn=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=bib_t&colName=bib_t&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query='.format(i*10)
    responese = requests.get(url)
    html = responese.text
    soup = BeautifulSoup(html, 'lxml')

    for j in range(1, 11):       
        detail_url = soup.select_one('#divContent > div.rightContent > div > div.srchResultW > div.srchResultListW > ul > li:nth-child(%d) > div.cont > p.title'%j)
        detail_list.append('http://www.riss.kr' + detail_url.find('a')['href'])
    
    for d in detail_list:
        responese = requests.get(d)
        html = responese.text
        soup = BeautifulSoup(html, 'lxml')
        print(html)
        title = soup.select_one('#thesisInfoDiv > div.thesisInfoTop')
        writer = soup.select_one('#thesisInfoDiv > div.infoDetail.on > div.infoDetailL > ul > li:nth-child(1) > div > p').get_text()
        keyward = soup.select('#thesisInfoDiv > div.infoDetail.on > div.infoDetailL > ul > li:nth-child(6) > div > p')

#thesisInfoDiv > div.thesisInfoTop > h3


