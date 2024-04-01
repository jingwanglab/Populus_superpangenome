# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 17:23:31 2023

@author: stt

"""

import pandas as pd

########kaks
pan = pd.read_csv('F:/work/Populus_pangenome/Populus_pangene/pan_gene/pangene_compare.csv')
pan = pan[['gene_id','pan_type']]
kaks = pd.read_csv('F:/work/Populus_pangenome/Dup_gene/kaks/all_spe_kaks.csv')
kaks = kaks[kaks['ks']<5]

kaks['dup1'] = kaks.apply(lambda x: x['pair'].split(',')[0], axis=1)
kaks['dup2'] = kaks.apply(lambda x: x['pair'].split(',')[1], axis=1)

dup1 = kaks[['dup1','dup_type']] 
dup2 = kaks[['dup2','dup_type']] 

pan.columns=['dup1','dup1_pan']
kaks1 = pd.merge(kaks,pan)
pan.columns=['dup2','dup2_pan']
kaks2 = pd.merge(kaks1,pan)

def core(dup1pan,dup2pan):
    if dup1pan=='core' and dup2pan=='core':
        return 'core'
    elif dup1pan=='core' or dup2pan=='core':
        return 'other'
    else:
        return 'variable'
    
kaks2['pan']=kaks2.apply(lambda x: core(x['dup1_pan'],x['dup2_pan']), axis=1)
kaks2['class'] = kaks2.apply(lambda x: x['dup_type']+'_'+x['pan'], axis=1)
kaks2.to_csv('F:/work/Populus_pangenome/Dup_gene/kaks/dup_pan_kaks.csv',index=False)


dup1.columns = ['gene_id','dup_type']
dup2.columns = ['gene_id','dup_type']
dup = pd.concat([dup1,dup2])
dup_pan = pd.merge(dup, pan, on=['gene_id'])

a = dup_pan.groupby(['pan_type','dup_type'])['dup_type'].count()
a=a.to_frame()
a.columns=['count']
a.reset_index(inplace=True)
a.to_csv('F:/work/Populus_pangenome/Dup_gene/pan_dup_states.csv',index=False)
#dup_pan['dup_type'].value_counts()

dup_pan['pan'] = dup_pan.apply(lambda x: 'core' if x['pan_type']=='core' else 'variable', axis=1)
#dup_pan.groupby(['dup_type','pan'])['pan'].count()

dup_pan.to_csv('F:/work/Populus_pangenome/Dup_gene/pan_dup_compare.csv')

