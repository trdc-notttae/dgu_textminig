import pandas as pd
voc_raw=pd.read_excel(r'./sample/sample_voc.xlsx',keep_default_na=False)
mf_dic=pd.read_excel(r'./sample/sample_company_mf_dic.xlsx',keep_default_na=False)
#사전에 제조그룹이 몇개있는지 확인하기
mf_all=list(set(list(mf_dic["제조그룹"])))
mf_all=[vl for vl in mf_all if vl !='']
#voc 데이터하나씩 불러와서 제조사 정규화시키기
modified_mf=[]
for i in range(len(voc_raw)):
    print(i,"//",len(voc_raw))
    this_maker=voc_raw.iloc[i]["제조사"]
    #VOC의 maker가 어떤 제조그룹에 속해있는지 확인하기
    #제조그룹 하나씩 불러와서 비교
    for mf in mf_all:
        #제조그룹의 정보가져오기
        this_mf_info=mf_dic[mf_dic["제조그룹"]==mf]
        #선택된 제조그룹의 모든 maker list확인
        maker_in_mf_list=list(this_mf_info["Maker"])
        #maker가 해당 제조그룹에 속할경우 modified_mf에 제조그룹의 이름 넣고 반복문 제거
        # 1개 maker는 하나의 제조사에만 속하므로, 더이상 반복이 필요없으니까
        ##, 아니면 다음 mf 불러오기
        if this_maker in maker_in_mf_list:
            modified_mf.append(mf)
            break
        if mf==mf_all[-1]:
            modified_mf.append('')


voc_raw["제조그룹정규화"]=modified_mf
voc_raw.to_excel(r'./sample/result/3.VOC_modified_mf.xlsx',index=False)
