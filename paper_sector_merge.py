import csv
import ast
import pandas as pd

def get_key(value, dict):
    key_list = []
    for key, values in dict.items():
        if value in values:
            key_list.append(key)

    return key_list

def gen_dict():
    sector_dict = {}
    department_dict = {}
    with open('C:\\Projects\\data_ana\\대분류dictionary.csv', 'r', encoding='utf-8') as f:
        lines = csv.reader(f)
        for line in lines:
            sector_dict[line[0]] = line[1]

    for a in list(sector_dict.keys()):
        department_dict[a] = []

    with open('C:\\Projects\\data_ana\\department_sector.csv', 'r', encoding = 'utf-8') as f:
        lines = csv.reader(f)
        for line in lines:            
            for i in range(1, len(line)):
                li = department_dict[line[i]]
                li.append(line[0])
                department_dict[line[i]] = li

    return sector_dict, department_dict

def sorted_by_year():
    department = []
    with open('C:\\Projects\\data_ana\\db_data.csv', 'r', encoding='utf-8') as f:
        lines = csv.reader(f)
        for line in lines:
            try:
                department.append([int(line[0]), line[1]])
            except:
                pass

    sector = []
    with open('C:\\Projects\\data_ana\\6대광역시,매출1억이상\\인천기업.csv', 'r', encoding = 'utf-8') as f:
        lines = csv.reader(f)
        for line in lines:
            try:
                year = int(line[2].replace('년차', ''))
                sector.append([(2021 - year), line[1]])
            except:
                pass

    department.sort()
    sector.sort()

    return sector, department

def get_year_dict(dict, li):
    year_num = {}
    for s in list(dict.keys()):
        year_num[s] = []

    for s in li:
        try:
            key_list = get_key(s[1], dict)
            for key in key_list:
                key = year_num.get(key)
                key.append(s[0])
                year_num[s] = key 
        except:
            pass

    return year_num

sd, dd = gen_dict()
sl, dl = sorted_by_year()

paper_year = get_year_dict(dd,dl)
company_year = get_year_dict(sd,sl)

for a in list(sd.keys()):
    print(a, len(paper_year.get(a)), len(company_year.get(a)))

with open('C:\\Projects\\data_ana\\dic.csv', 'w', encoding= 'utf-8', newline='') as f:
    wr = csv.writer(f)
    for a in list(sd.keys()):
        wr.writerow([a, paper_year.get(a), company_year.get(a)])