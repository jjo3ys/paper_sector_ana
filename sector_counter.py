import csv
import pandas as pd
import numpy as np

def sorting_sector():
    df = pd.read_csv('C:\\project\\data_ana\\sector.csv', encoding = 'utf-8')
    df = df.values
    total_sect = []

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
    total_sect.to_csv('C:\\project\\data_ana\\sorted_sector.csv', encoding = 'utf-8')

def get_sector():
    cities = ['광주', '대구', '대전', '부산', '울산', '인천', '서울']
    sectors = []

    for city in cities:
        try:
            with open('C:\\project\\data_ana\\6대광역시,매출1억이상\\{0}기업.csv'.format(city), 'r', encoding = 'utf-8') as f:
                lines = csv.reader(f)
                for line in lines:
                    if line[1] not in sectors and '년차' not in line[1]:
                        sectors.append(line[1])
        except:
            pass

        with open('C:\\project\\data_ana\\6대광역시+서울,중견기업이상, 매출1억이상\\{0}.csv'.format(city), 'r' , encoding = 'utf-8') as f:
            lines = csv.reader(f)
            for line in lines:
                if line[1] not in sectors and '년차' not in line[1]:
                    sectors.append(line[1])

    sectors = np.array(sectors)
    sectors = pd.DataFrame(sectors, columns = ['sector'])
    sectors.to_csv('C:\\project\\data_ana\\sector.csv', encoding = 'utf-8')

def sorting():
    sector_dict = dict()
    with open('C:\\project\\data_ana\\대분류.csv', 'r', encoding='utf-8') as f:
        lines = csv.reader(f)
        count = 0
        a = []
        b = []
        c = []
        d = []
        e = []
        f = []
        g = []
        h = []
        i = []
        j = []
        k = []
        l = []
        m = []
        n = []
        o = []
        p = []
        q = []
        r = []
        s = []
        t = []
        u = []
        for line in lines:
            if count == 0:
                count = 1
                continue
            if int(line[2]) <= 3 and int(line[2]):
                a.append(line[1])
            elif int(line[2]) <= 8:
                b.append(line[1])
            elif int(line[2]) <= 34:
                c.append(line[1])
            elif int(line[2]) <= 35:
                d.append(line[1])
            elif int(line[2]) <= 39:
                e.append(line[1])
            elif int(line[2]) <= 42:
                f.append(line[1])
            elif int(line[2]) <= 47:
                g.append(line[1])
            elif int(line[2]) <= 52:
                h.append(line[1])
            elif int(line[2]) <= 56:
                i.append(line[1])
            elif int(line[2]) <= 63:
                j.append(line[1])
            elif int(line[2]) <= 66:
                k.append(line[1])
            elif int(line[2]) <= 68:
                l.append(line[1])
            elif int(line[2]) <= 73:
                m.append(line[1])
            elif int(line[2]) <= 76:
                n.append(line[1])
            elif int(line[2]) <= 84:
                o.append(line[1])
            elif int(line[2]) <= 85:
                p.append(line[1])
            elif int(line[2]) <= 87:
                q.append(line[1])
            elif int(line[2]) <= 91:
                r.append(line[1])
            elif int(line[2]) <= 96:
                s.append(line[1])
            elif int(line[2]) <= 98:
                t.append(line[1])
            elif int(line[2]) <= 99:
                u.append(line[1])
                
    sector_list = [a, b, c, d, e ,f ,g, h, i, j, k, l, m, n, o, p, q, r, s, t, u]
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']
    for i in range(len(sector_list)):
        sector_dict[str(alphabet[i]).upper()] = sector_list[i]
    
    with open('C:\\project\\data_ana\\대분류안됨.csv', 'r', encoding='utf-8') as f:
        lines = csv.reader(f)
        count = 0
        for line in lines:
            if count == 0:
                count = 0
                continue

            sec_alpha = line[2]
            sec_list = sector_dict.get(sec_alpha)
            sec_list.append(line[1])
            sector_dict[sec_alpha] = sec_list
    
    
    with open('C:\\project\\data_ana\\분류기준.csv', 'w', encoding = 'utf-8', newline = '') as f:
        wr = csv.writer(f)
        for sec in alphabet:
            sec = sec.upper()
            wr.writerow([sec, sector_dict.get(sec)])
#get_sector()
#sorting_sector()
sorting()