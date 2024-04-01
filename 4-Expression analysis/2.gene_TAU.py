# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 22:06:25 2021

@author: Stt
"""

import pandas as pd
import os


species = ['Prot','Psim','Psze','Palby','Pdav','Peup','Pkor','Ppru','Ppse','Ptre','Ptri','Pwua']
gene_fpkm_dir='gene_expression/'


all_df = pd.DataFrame()
for spe in species:
    file_path=[]
    for maindir, subdir, file_name_list in os.walk(gene_fpkm_dir+spe):
        for filename in file_name_list:
            if 'genes.fpkm_tracking' in filename:
                file_path.append(os.path.join(maindir, filename))
          
    for i,path in enumerate(file_path):
        aa = path.split('/')[-1].split('_')[0]
        df = pd.read_csv(path,sep='\t')
        df = df[['gene_id','FPKM']]
        df.rename(columns={'FPKM':aa},inplace=True)
        if i==0:
            df_gene_fpkm = df
        if i!=0:
            df_gene_fpkm = pd.merge(df_gene_fpkm,df,on = 'gene_id',how='outer')
    
    
    df_gene_fpkm['max']=df_gene_fpkm.max(axis=1)
    df_gene_fpkm['sum']=df_gene_fpkm.sum(axis=1)
    df_gene_fpkm['sum_final']=df_gene_fpkm['sum']-df_gene_fpkm['max']
    n=i+1
    df_gene_fpkm['tau'] = df_gene_fpkm.apply(lambda x: n/(n-1)-(x['sum_final']/((n-1)*x['max'])) if x['max']!=0 else -9999, axis=1)
    gene_tau = df_gene_fpkm[['gene_id','tau']]
    gene_tau['species'] = spe
    all_df = pd.concat([all_df, gene_tau], axis=1)

all_df.to_csv('tau.csv',index=False)
