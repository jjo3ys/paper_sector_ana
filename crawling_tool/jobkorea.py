import csv
import requests

from bs4 import BeautifulSoup

url = 'https://www.jobkorea.co.kr/Search/?local=K000&tabType=corp&Page_No=1'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    for i in range(1, 11):
        company = soup.select_one('#content > div > div > div.cnt-list-wrap > div > div.corp-info > div.lists > div > div.list-default > ul > li:nth-child(%s) > div > div.post-list-corp.clear > div'%i)

        sub_url = 'http://www.jobkorea.co.kr'+company.find('a')['href']
        sub_re = requests.get(sub_url)
        sub_html = sub_re.text
        sub_soup = BeautifulSoup(sub_html, 'html.parser')
        info = sub_soup.select_one('#company-body')
        details = info.find('div', class_ = 'value-container')

        for detail in details:
            print(detail)
            #print(detail.get_text())
#company-body
##company-body > div.company-body-infomation > div.company-infomation-row.basic-infomation > div > table > tbody