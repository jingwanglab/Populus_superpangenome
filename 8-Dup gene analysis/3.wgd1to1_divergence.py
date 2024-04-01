# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:03:28 2021

@author: Stt
"""

import pandas as pd

pair = pd.read_csv('F:/work/Populus_pangenome/Dup_gene/all_spe_wgd1to1.csv',sep='\t')
pair['pan'] = pair.apply(lambda x: 'same' if x['dup1_pan']==['dup2_pan'] else 'different', axis=1)

fpkm = pd.read_csv('F:/work/Populus_pangenome/Populus_pangene/gene_expression/all_gene_fpkm.csv', sep='\t')
fpkm= fpkm[['gene_id', 'FPKM']]
fpkm.columns = ['dup1', 'dup1_FPKM']
pair_1 = pd.merge(pair, fpkm, on=['dup1'],how='left')
fpkm.columns=['dup2', 'dup2_FPKM']
pair_2 = pd.merge(pair_1, fpkm, how='left', on=['dup2'])
pair_2 = pair_2[['species','dup1', 'dup2', 'ka', 'ks', 'ka/ks', 'dup_type','pan','dup1_FPKM','dup2_FPKM']]
pair_2['FPKM_sum'] = pair_2['dup1_FPKM'] + pair_2['dup2_FPKM']
pair_2 = pair_2[pair_2['FPKM_sum']!=0]

def diver(e1, e2):
    di = (float(e1)-float(e2))/(float(e1)+float(e2))
    return di

pair_2['divergence_fpkm'] = pair_2.apply(lambda x: diver(x["dup1_FPKM"],x['dup2_FPKM']), axis=1)
#pair_2.to_csv('F:\work\Populus_pangenome/expression_methy_divergence/Pdav/fpkm.csv', index=False)

methy = pd.read_csv('F:/work/Populus_pangenome/Gene_methy/all_spe_methy.csv')

methy.columns = ['dup1', 'dup1_CpG_body', 'dup1_CpG_up', 'dup1_CpG_down', 'dup1_CHH_body', 'dup1_CHH_up','dup1_CHH_down', 'dup1_CHG_body', 'dup1_CHG_up', 'dup1_CHG_down']
data = pd.merge(pair_2, methy, how='left',on='dup1')

methy.columns = ['dup2', 'dup2_CpG_body', 'dup2_CpG_up', 'dup2_CpG_down', 'dup2_CHH_body', 'dup2_CHH_up','dup2_CHH_down', 'dup2_CHG_body', 'dup2_CHG_up', 'dup2_CHG_down']
dataa = pd.merge(data, methy, how='left',on='dup2')


dataa['divergence_CpG_up'] = dataa.apply(lambda x: diver(x["dup1_CpG_up"],x['dup2_CpG_up']), axis=1)
dataa['divergence_CHG_up'] = dataa.apply(lambda x: diver(x["dup1_CHG_up"],x['dup2_CHG_up']), axis=1)
dataa['divergence_CHH_up'] = dataa.apply(lambda x: diver(x["dup1_CHH_up"],x['dup2_CHH_up']), axis=1)

dataa['divergence_CpG_down'] = dataa.apply(lambda x: diver(x["dup1_CpG_down"],x['dup2_CpG_down']), axis=1)
dataa['divergence_CHG_down'] = dataa.apply(lambda x: diver(x["dup1_CHG_down"],x['dup2_CHG_down']), axis=1)
dataa['divergence_CHH_down'] = dataa.apply(lambda x: diver(x["dup1_CHH_down"],x['dup2_CHH_down']), axis=1)

dataa['divergence_CpG_body'] = dataa.apply(lambda x: diver(x["dup1_CpG_body"],x['dup2_CpG_body']), axis=1)
dataa['divergence_CHG_body'] = dataa.apply(lambda x: diver(x["dup1_CHG_body"],x['dup2_CHG_body']), axis=1)
dataa['divergence_CHH_body'] = dataa.apply(lambda x: diver(x["dup1_CHH_body"],x['dup2_CHH_body']), axis=1)


spes = dataa['species'].unique().tolist()
def ks_1(ks_c):
    aa = ks_c.split(',')
    return aa[0]

def ks_class(kskut_temp, ks_list):
    if kskut_temp == ks_list[0]:
        return 'L'
    elif kskut_temp == ks_list[1]:
        return 'M'    
    else:
        return 'H'

all_df = pd.DataFrame()
for spee in spes:
    globals()['df_'+spee]=data[data['spe']==spee]
    globals()['df_'+spee]['spe_kscut']=pd.qcut(globals()['df_'+spee]['ks'],3)
     
    globals()['df_'+spee]['spe_kscut'] = globals()['df_'+spee]['spe_kscut'].astype(str)
    globals()['df_'+spee]['spe_kscut'] = globals()['df_'+spee]['spe_kscut'].str.replace(r'(', '')  
    globals()['df_'+spee]['kscut_temp'] = globals()['df_'+spee].apply(lambda x: ks_1(x['spe_kscut']),axis=1)
    ks_cut_list = globals()['df_'+spee]['kscut_temp'].unique().tolist()
    ks_cut_list.sort()
    globals()['df_'+spee]['ks_class'] = globals()['df_'+spee].apply(lambda x: ks_class(x['kscut_temp'],ks_cut_list),axis=1)
    globals()['df_'+spee].drop(['spe_kscut','kscut_temp'], axis=1,inplace=True)
    all_df = pd.concat([all_df,globals()['df_'+spee]])

all_df.to_csv('F:/work/Populus_pangenome/Dup_gene/wgd/wgd1to1_divergence.csv', index=False)
