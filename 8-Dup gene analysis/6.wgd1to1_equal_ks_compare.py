# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 16:14:42 2021

@author: Stt
""" 
import pandas as pd
data = pd.read_csv('F:/work/Populus_pangenome/Dup_gene/wgd/wgd1to1_equal_Ks.csv')

data['min_fpkm']= data.apply(lambda x: x['dup1_FPKM'] if x['dup1_FPKM']<x['dup2_FPKM'] else x['dup2_FPKM'], axis=1)
data['max_fpkm']= data.apply(lambda x: x['dup2_FPKM'] if x['dup1_FPKM']<x['dup2_FPKM'] else x['dup1_FPKM'], axis=1)


def fpkm_fold(a,b):
    if a==b:
        f =0
    elif a==0 or b==0:
        f = abs(a-b)
    elif a>b:
        f = (a-b)/b
    elif a< b:
        f = (b-a)/a
    if f <=0.5:
        return 'conserved'
    if f>=2:
        return 'divergent'
    else:
        return 'M'
        
data['fpkm_div'] = data.apply(lambda x: fpkm_fold(x['min_fpkm'],x['max_fpkm']),axis=1)
data['fpkm_div'].value_counts()
data.to_csv('F:/work/Populus_pangenome/Dup_gene/wgd/wgd1to1_equal_Ks_class.csv',index=False)

def fpkm_max_gene(a,b,c,d):
    if c > d:
        return a
    else:
        return b

def fpkm_min_gene(a,b,c,d):
    if c < d:
        return a
    else:
        return b

fdlow=data[data['fpkm_div']=='conserved']
fdhigh=data[data['fpkm_div']=='divergent']
fdlow['fpkml_gene'] = fdlow.apply(lambda x: fpkm_min_gene(x['dup1'],x['dup2'],x['dup1_FPKM'],x['dup2_FPKM']),axis=1)
fdlow['fpkmh_gene'] = fdlow.apply(lambda x: fpkm_max_gene(x['dup1'],x['dup2'],x['dup1_FPKM'],x['dup2_FPKM']),axis=1)
fdhigh['fpkml_gene'] = fdhigh.apply(lambda x: fpkm_min_gene(x['dup1'],x['dup2'],x['dup1_FPKM'],x['dup2_FPKM']),axis=1)
fdhigh['fpkmh_gene'] = fdhigh.apply(lambda x: fpkm_max_gene(x['dup1'],x['dup2'],x['dup1_FPKM'],x['dup2_FPKM']),axis=1)

f_h_l = fdhigh[['fpkml_gene']]
f_h_h = fdhigh[['fpkmh_gene']]
f_l_l = fdlow[['fpkml_gene']]
f_l_h = fdlow[['fpkmh_gene']]

f_h_l['type']='div_L'
f_h_h['type']='div_H'
f_l_l['type']='con_L'
f_l_h['type']='con_H'

f_h_l.columns=['gene_id','type']
f_h_h.columns=['gene_id','type']
f_l_l.columns=['gene_id','type']
f_l_h.columns=['gene_id','type']

df_all = pd.concat([f_h_l, f_h_h, f_l_l, f_l_h])
pan = pd.read_csv('F:/work/Populus_pangenome/Populus_pangene/pan_gene/pangene_compare.csv')
df_all_comp = pd.merge(df_all,pan,how='left',on=['gene_id'])
df_all.to_csv('F:/work/Populus_pangenome/Dup_gene/wgd/wgd1to1_equal_4type_gene_compare.csv',index=False)

