import csv

def mkcsv():
    with open('C:\\Projects\\data_ana\\db_data.csv', 'r', encoding = 'utf-8') as f:
        lines = csv.reader(f)
        department = []
        for line in lines:
            if [line[1], ''] not in department:
                department.append([line[1], ''])

    with open('C:\\Projects\\data_ana\\department.csv', 'w', encoding = 'utf-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerows(department)

def rdcsv():
    with open('C:\\Projects\\data_ana\\department_sector.csv', 'r', encoding = 'utf-8') as f:
        lines = csv.reader(f)
        data = []
        for line in lines:
            if len(line) > 2:
                data.append([line[0], line[1:]])
            else:
                data.append([line[0], [line[1]]])

    with open('C:\\Projects\\data_ana\\department.csv', 'w', encoding = 'utf-8', newline='') as f:
        wr = csv.writer(f)
        wr.writerows(data) 
rdcsv()