import pymysql
import csv
import datetime

conn = pymysql.connect(host = "moberan.com", user = "rndhubv2", password = "rndhubv21@3$",  db = "inu_rndhub", charset = "utf8")
curs = conn.cursor()

curs.execute('Select start_date, researcher_idx from tbl_data where data_type_code = 2')
data = curs.fetchall()
data_list = []
for d in data:
    year = str(d[0]).split('-')[0]
    curs.execute('Select department, research_field from tbl_researcher_data where idx = %s', d[1])
    r_data = curs.fetchall()
    data_list.append([year, r_data[0][0], r_data[0][1]])
    print(year)

with open('C:\\Projects\\data_ana\\db_data.csv', 'w', encoding = 'utf-8', newline='') as f:
    wr = csv.writer(f)
    wr.writerows(data_list)
