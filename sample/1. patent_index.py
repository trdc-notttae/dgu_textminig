import pandas as pd
import numpy as np

###False로 할경우 공백으로 처리되어 텍스트 마이닝하기 쉬운형태로 불러 올 수 있음
# 한글이 포함된 csv파일을 불러올 때는 인코딩 문제로 제일끝에 encoding='cp949'를 추가해줘야함
test_data=pd.read_csv('./sample/sample_patent.csv',keep_default_na=False,encoding='cp949')
#영향력 지표 계산
# (value-min(피인용수))/(max(피인용수)-min(피인용수))
# 지표계산은 '모집단'을 어떻게 설정하는지에 따라 다르게 나타남
max_cited=np.max(list(test_data["자국피인용횟수"]))
min_cited=np.min(list(test_data["자국피인용횟수"]))

#i를 0부터 len(test_data)값만큼 반복하는 반복문
impact_index_list=[]
for i in range(len(test_data)):
    #i번째 행의 "자국피인용횟수"의 값을 불러옴
    this_cited=test_data.iloc[i]["자국피인용횟수"]
    this_impact_index=(this_cited-min_cited)/(max_cited-min_cited)
    #소숫점 자리수 맞춰주기
    this_impact_index=round(this_impact_index,4)
    #계산끝난 데이터 리스트에 넣기
    impact_index_list.append(this_impact_index)

test_data["영향력지표"]=impact_index_list
#영향력지표 계산결과 저장하기
test_data.to_excel('./sample/result/1.sample_patent_impact_index.xlsx',index=False)

