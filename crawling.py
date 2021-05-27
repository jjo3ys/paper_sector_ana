import re
import csv
import math
import requests
import time

from bs4 import BeautifulSoup

def mk_csv(city, company_info):
    with open('C:\\Projects\\data_ana\\{0}기업.csv'.format(city), 'w', encoding = 'utf-8', newline = '') as f:
        wr = csv.writer(f)
        wr.writerows(company_info)

def page_num(city):
    #url = 'https://www.saramin.co.kr/zf_user/company-search?searchWord=&area={0}&industry=&welfare=&scale=%EB%8C%80%EA%B8%B0%EC%97%85%2C1000%EB%8C%80%EA%B8%B0%EC%97%85%2C%EC%A4%91%EA%B2%AC%EA%B8%B0%EC%97%85&listingType=&companyType=&employees=&revenue=100000&operatingRevenue=&netRevenue=&establishment=&salary=&startingSalary=&order=view&recruitCheck=&page=2'.format(city)
    #매출액1억, 중견기업이상
    url = 'https://www.saramin.co.kr/zf_user/company-search?searchWord=&area={0}&industry=&welfare=&scale=&listingType=&companyType=&employees=&revenue=100000&operatingRevenue=&netRevenue=&establishment=&salary=&startingSalary=&order=&recruitCheck=&page=2'.format(city)
    #매출액1억이상
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        total_count = soup.select_one('#content > div.wrap_company_search > div > div.list_company_search > div.total_sort > span > span').get_text()
        total_count = int(total_count.replace(',', ''))
    else:
        print(response.status_code)

    total_page_num = math.ceil(total_count/10)
    return total_page_num

def crawling(city):
    total_page_num = page_num(city)
    company_info = []
    element = [1,2,3,4,5,8,9,10,11,12]

    try:
        for i in range(1, total_page_num+1):
            print('page_num:{0}/{1}'.format(i, total_page_num))
            #url = 'https://www.saramin.co.kr/zf_user/company-search?searchWord=&area={0}&industry=&welfare=&scale=%EB%8C%80%EA%B8%B0%EC%97%85%2C1000%EB%8C%80%EA%B8%B0%EC%97%85%2C%EC%A4%91%EA%B2%AC%EA%B8%B0%EC%97%85&listingType=&companyType=&employees=&revenue=100000&operatingRevenue=&netRevenue=&establishment=&salary=&startingSalary=&order=view&recruitCheck=&page={1}'.format(city, i)
            #매출액1억, 중견기업이상
            url = 'https://www.saramin.co.kr/zf_user/company-search?searchWord=&area={0}&industry=&welfare=&scale=&listingType=&companyType=&employees=&revenue=100000&operatingRevenue=&netRevenue=&establishment=&salary=&startingSalary=&order=&recruitCheck=&page={1}'.format(city, i)
            #매출액1억이상
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            for j in element:
                year = scale = employees = ''

                company = soup.select_one('#content > div.wrap_company_search > div > div.list_company_search > div.wrap_list > div:nth-child(%d) > div > div.area_info > strong > a:nth-child(1)'%j).get_text()
                sector = soup.select_one('#content > div.wrap_company_search > div > div.list_company_search > div.wrap_list > div:nth-child(%d) > div > div.area_info > div.text_info > span:nth-child(1)'%j).get_text()
                details = soup.select('#content > div.wrap_company_search > div > div.list_company_search > div.wrap_list > div:nth-child(%d) > div > div.area_info > div.text_info > span'%j)
                
                for detail in details:
                    info =  detail.get_text() 
                    if '년차' in info:
                        year = info
                    elif '기업' in info:
                        scale = info
                    elif '명' in info and info != company:
                        employees = info     
            
                try:
                    grow = soup.select_one('#content > div.wrap_company_search > div > div.list_company_search > div.wrap_list > div:nth-child(%d) > div > div.company_finance > div > ul > li.finance.sales > a > dl > dd.ico_finance.up > span:nth-child(1)'%j).get_text()
                    sales = soup.select_one('#content > div.wrap_company_search > div > div.list_company_search > div.wrap_list > div:nth-child(%d) > div > div.company_finance > div > ul > li.finance.sales > a > dl > dd:nth-child(2)'%j).get_text()
                    sales = sales.replace(' ', '').replace(',', '')

                except:
                    grow = ''
                    sales = ''
                    
                #print('기업:',company,', 분야:', sector,', 년차:', year,', 기업 규모:', scale, ', 사원수:', employees, ', 전년대비 매출성장률', grow)
                company_info.append([company, sector, year, scale, employees, sales, grow])
        return company_info
        
    except:      
        with open('C:\\Projects\\data_ana\\{0}임시파일.csv'.format(city), 'w', encoding = 'utf-8', newline = '') as f:
            wr = csv.writer(f)
            wr.writerows(company_info)    
        company_info = 0
        return company_info

    

def main():
    cities = {'인천':'108000', '대전':'105000', '대구':'104000', '광주':'103000', '울산':'107000', '부산':'106000', '서울':'101000'}#인천, 대전, 대구, 광주, 울산, 부산, 서울
    cities = {'서울':'101000'}
    for city in cities.keys():
        print(city)
        company_info = crawling(cities.get(city))
        if company_info == 0:
            continue
        else:
            mk_csv(city, company_info)
main()