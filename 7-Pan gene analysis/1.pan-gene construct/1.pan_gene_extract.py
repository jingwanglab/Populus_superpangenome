

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:06:55 2021

@author:Stt
"""

import pandas as pd


data= open('F:/work/Populus_pangenome/Populus_pangene/Orthogroups.tsv').readlines()
data_m = data[1:]

core_lines = []
softcore_lines = []
dis2_lines=[]
dis3_lines=[]
dis4_lines=[]
dis5_lines=[]
dis6_lines=[]
dis7_lines=[]
dis8_lines=[]
dis9_lines=[]
dis10_lines=[]
dis11_lines=[]
dis12_lines=[]
dis13_lines=[]
dis14_lines=[]
dis15_lines=[]
dis16_lines=[]
dis17_lines=[]
private_lines=[]


##### obtain pan-gene family
for line in data_m:
    xx = line.strip().split('\t')
    spe_i = 0
    for i in range(1,20):
#        ids = xx[i].split(',')
        if len(xx[i]) >0 and xx[i]!='':
            spe_i += 1
                
    if spe_i ==19:
        core_lines.append(line)
        continue
    elif spe_i ==1:
        private_lines.append(line)
        continue
    elif spe_i ==2:
        dis2_lines.append(line)
        continue
    elif spe_i ==3:
        dis3_lines.append(line)
        continue    
    elif spe_i ==4:
        dis4_lines.append(line)
        continue    
    elif spe_i ==5:
        dis5_lines.append(line)
        continue    
    elif spe_i ==6:
        dis6_lines.append(line)
        continue
    elif spe_i ==7:
        dis7_lines.append(line)
        continue
    elif spe_i ==8:
        dis8_lines.append(line)
        continue
    elif spe_i ==9:
        dis9_lines.append(line)
        continue
    elif spe_i ==10:
        dis10_lines.append(line)
        continue
    elif spe_i ==11:
        dis11_lines.append(line)
        continue
    elif spe_i ==12:
        dis12_lines.append(line)
        continue
    elif spe_i ==13:
        dis13_lines.append(line)
        continue
    elif spe_i ==14:
        dis14_lines.append(line)
        continue
    elif spe_i ==15:
        dis15_lines.append(line)
        continue
    elif spe_i ==16:
        dis16_lines.append(line)
        continue
    elif spe_i ==17:
        softcore_lines.append(line)
        continue
    elif spe_i ==18:
        softcore_lines.append(line)
        continue

dis_lines = dis2_lines + dis3_lines + dis4_lines + dis5_lines + dis6_lines + dis7_lines + dis8_lines + dis9_lines+\
           dis10_lines + dis11_lines + dis12_lines + dis13_lines + dis14_lines + dis15_lines + dis16_lines

types = ['core','softcore','dis','private']

for ty in types:
    f_o = open('F:/work/Populus_pangenome/Populus_pangene/pan_gene/'+ty+'/'+ty+'_og.tsv','w')
    for line in softcore_lines:
        f_o.write(line)
    f_o.close()
    
    
    ## extract gene ID of each species in pan-gene family
    ogs = pd.read_csv('F:/work/Populus_pangenome/Populus_pangene/pan_gene/'+ty+'/'+ty+'_og.tsv', sep='\t')    
    spe = ogs.columns.tolist()
    spe = spe[1:]
      
    a_genes=[]
    for sp in spe:
        sp_df = ogs[ogs[sp].notna()]
        sp_genes = sp_df[sp].tolist()
        all_genes = []
        for ll in sp_genes:
            xx = ll.split(',')
            for i in xx:
                all_genes.append(i)
                a_genes.append(i)
        f = open('F:/work/Populus_pangenome/Populus_pangene/pan_gene/'+ty+'/'+sp+'_gene.list','w')
        for gene in all_genes:
            f.write(gene+'\n')
        f.close()
         
    f = open('F:/work/Populus_pangenome/Populus_pangene/pan_gene/'+ty+'/all_gene.list','w')
    for gene in a_genes:
        f.write(gene+'\n')
    f.close()
    

  
