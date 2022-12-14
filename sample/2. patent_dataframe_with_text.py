import pandas as pd
import numpy as np
raw_data=pd.read_excel(r'./sample/result/1.sample_patent_impact_index.xlsx',keep_default_na=False)
#출원인국가 유형 확인하기
aff_country_all=list(raw_data["출원인국가"])
#중복제거
uniq_aff_country=list(set(aff_country_all))
print(uniq_aff_country)
#2인이상의 출원인일 경우 | 로 나타나는 특징이 있어, 보정이 필요함
modified_aff_list=[]
#uniq_aff_country list안에있는 값하나씩 가져와서 반복작업함
for country in uniq_aff_country:
    #정제된 목록에 없을경우에만 작업 진행
    if country not in modified_aff_list:
        #'|'가 없을경우 그냥 더해줌
        if '|' not in country:
            modified_aff_list.append(country)
        else:
            multi_auth_country=country.split('|')
            for splited_country in multi_auth_country:
                if splited_country not in modified_aff_list:
                    modified_aff_list.append(splited_country)
print(modified_aff_list)

# 공백은 없에줌
# modified_aff_list list안에있는 vl이라는 값이 ''이 아닐 경우에만 리스트에 남겨둠
modified_aff_list=[vl for vl in modified_aff_list if vl!='']
#'국가' 기준으로 특허를 불러와서 영향력의 평균치와 특허의 수를 계산해줌

#분석결과를 저장할 빈 DF를 만듦
result_df=pd.DataFrame()
for ctr in modified_aff_list:
    #raw_data의 "출원인국가" 열에 변수 ctr에 들어간 값이 들어간 데이터프레임만 선택함
    target_data=raw_data[raw_data["출원인국가"].str.contains(ctr)]
    target_data_count=len(target_data)
    target_data_avg_index=np.average(list(target_data["영향력지표"]))
    #소수점 자리 설정
    target_data_avg_index=round(target_data_avg_index,4)
    #1개 국가의 결과물을 DF로 만들기
    this_target_df=pd.DataFrame({"Country":[ctr],"특허수":[target_data_count],"평균영향력":[target_data_avg_index]})
    #1개 국가 결과물을 전체 분석결과에 더해주기
    result_df=result_df.append(this_target_df,ignore_index=True)
#점수내림차순으로 정렬 ascending=True하면 오름차순임
result_df=result_df.sort_values(by="평균영향력",ascending=False)
result_df.to_excel('./sample/result/2.impact analysis_by_ctr.xlsx',index=False)

