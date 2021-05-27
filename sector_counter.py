import csv
import pandas as pd
import numpy as np

def sorting_sector():
    df = pd.read_csv('C:\\Projects\\data_ana\\sector.csv', encoding = 'utf-8')
    df = df.values
    print(len(df))
    total_sect = []
    not_sect = []
    no = []
    for i in range(len(df)):
        if '업' in df[i][1]: 
            sector = df[i][1].split()[-1]
            if sector not in total_sect:
                total_sect.append(sector)
        elif '명' not in df[i][1] and '년차' not in df[i][1]:
            total_sect.append(df[i][1])



    print(len(total_sect))
    print(total_sect)
    total_sect = np.array(total_sect)
    total_sect = pd.DataFrame(total_sect, columns = ['추린 산업분야'])
    total_sect.to_csv('C:\\Projects\\data_ana\\sorted_sector.csv', encoding = 'cp949')

def get_sector():
    cities = ['광주', '대구', '대전', '부산', '울산', '인천', '서울']
    sectors = []
    total_count = 0
    for city in cities:
        try:
            with open('C:\\Projects\\data_ana\\6대광역시,매출1억이상\\{0}기업.csv'.format(city), 'r', encoding = 'utf-8') as f:
                lines = csv.reader(f)
                for line in lines:
                    total_count += 1
                    if line[1] not in sectors:
                        sectors.append(line[1])
                
        except:
            pass

        with open('C:\\Projects\\data_ana\\6대광역시+서울,중견기업이상, 매출1억이상\\{0}.csv'.format(city), 'r' , encoding = 'utf-8') as f:
            lines = csv.reader(f)
            for line in lines:
                total_count += 1
                if line[1] not in sectors:
                    sectors.append(line[1])
    print(len(sectors), total_count)
    '''sectors = np.array(sectors)
    sectors = pd.DataFrame(sectors, columns = ['sector'])
    sectors.to_csv('C:\\Projects\\data_ana\\sector.csv', encoding = 'utf-8')'''

get_sector()
#sorting_sector()