# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:23:40 2021

@author: Stt
"""

import pandas as pd
data = pd.read_csv('F:/work/Populus_pangenome/Dup_gene/kaks/dup_pan_kaks.csv')
wgd = data[data['dup_type']=='WGD']


wgd['dup1']=wgd.apply(lambda x: x['pair'].split(',')[0], axis=1)
wgd['dup2']=wgd.apply(lambda x: x['pair'].split(',')[1], axis=1)

dup_1 = wgd['dup1'].tolist()
dup_2 = wgd['dup2'].tolist()

wgd_g = dup_1+dup_2

s = {}
for i in wgd_g:
    if i in s.keys():
        s[i]+=1
    else:
        s[i]=1

wgd1=[]
for k in s.keys():
    if s[k]==1:
       wgd1.append(k) 


def wgd1to1(a, genes):
    xx = a.split(',')
    if xx[0] in genes and xx[1] in genes:
        return 'Yes'
    else:
        return 'No'

wgd['1to1'] = wgd.apply(lambda x: wgd1to1(x['pair'], wgd1), axis=1)
wgd_f = wgd[wgd['1to1']=='Yes']
wgd_f.to_csv('F:/work/Populus_pangenome/Dup_gene/all_spe_wgd1to1.csv', index=False)

