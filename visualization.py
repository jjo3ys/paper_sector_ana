from matplotlib import font_manager, rc

import matplotlib.pyplot as plt
import csv
import ast
import pandas as pd
import numpy as np

font = font_manager.FontProperties(fname = "C:/Windows/Fonts/NGULIM.TTF").get_name()
rc('font', family = font)

def normalization():
    df = pd.read_csv('C:\\project\\analyze\\분석완료.csv', encoding = 'utf-8')

    for i in range(10):
        if i<=4:
            a = df[['p{0}년'.format(2000+i*5)]]
            a = round(a/a.sum()*100,1)
            df[['p{0}년'.format(2000+i*5)]] = a

        else:
            a = df[['c{0}년'.format(2000+(i-5)*5)]]
            a = round(a/a.sum()*100,1)
            df[['c{0}년'.format(2000+(i-5)*5)]] = a

    return df.to_numpy()
df = normalization()

paper = df[:, 1:7]
company = df[:, 7:]

sector_dict = {'A':'농업, 임업 및 어업','B':'광업','C':'제조업','D':'전기,가스,증기 및 공기 조절 공급업',
               'E':'수도, 하수 및 폐기물 처리, 원료 재생업','F':'건설업','G':'도매 및 소매업','H':'운수 및 창고업',
               'I':'숙박 및 음식점업','J':'정보통신업','L':'금융 및 보험업','M':'전문, 과학 및 기술 서비스업',
               'N':'사업시설 관리, 사업 지원 및 임대 서비스업','O':'공공 행정, 국방 및 사회보장 행정','P':'교육 서비스업','Q':'보건업 및 사회복지 서비스업',
               'R':'예술, 스포츠 및 여가관련 서비스업','S':'협회 및 단체, 수리 및 기타 개인 서비스업','T':'가구 내 고용활동 및 달리 분류되지 않은 자가 소비 생산활동','U':'국제 및 외국기관'}

for p,c in zip(paper, company):
    x = np.arange(5)
    years = ['2000', '2005', '2010', '2015', '2020']
    plt.bar(x, p[1:], width = 0.3, align='edge', color = 'blue')
    plt.bar(x, c, width = 0.3, color = 'red')
    plt.xticks(x, years)
    plt.title('업종 : {0}'.format(sector_dict.get(p[0])))
    plt.ylabel('해당 년도 마다 업종별로 차지하는 %')
    plt.xlabel('blue : 관련 논문, red :관련 기업')
    plt.grid(True)
    plt.show()