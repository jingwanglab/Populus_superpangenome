# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:41:11 2021

@author: Stt
"""

#obtain low-copy genes

import pandas as pd
from Bio import SeqIO
import shutil
import os


df = pd.read_csv('Orthogroups/Orthogroups.GeneCount.tsv',sep='\t')  # othorfinder output

col=list(df.columns)
col=col[1:-1]
for c in col:
    df=df.drop(df[df[c]<1].index)

for c in col:
    df=df.drop(df[df[c]>5].index)

low_copy = df[df['Total']!=22] #remove single-copy
low_copy_ogs = low_copy['Orthogroup'].tolist()

fas = os.listdir('Orthogroups/Orthogroup_Sequences/')
for fa in fas:
    fi = fa.split('.')[0]
    if fi in low_copy_ogs:    
        old_p = 'Orthogroups/Orthogroup_Sequences/'+fa
        new_p = 'Low_Copy_Orthologue_Sequences/'+fa
        shutil.move(old_p,new_p)



####obtain CDS
import os
from Bio import SeqIO

path = 'Low_Copy_Orthologue_Sequences/' 
files = os.listdir(path)  


def id2seq(cds_file):
    cds_dict = {}
    for record in SeqIO.parse(cds_file,'fasta'):
        cds_dict[record.id] = str(record.seq)
    return cds_dict

ade_cds = id2seq('F:/work/gene_annotation/all_cds/pade_cds.fa')
alb_cds = id2seq('F:/work/gene_annotation/all_cds/Palb.cds')
alby_cds = id2seq('F:/work/gene_annotation/all_cds/Palby.cds')
dav_cds = id2seq('F:/work/gene_annotation/all_cds/pdav_cds.fa')
del_cds = id2seq('F:/work/gene_annotation/all_cds/pdel_cds.fa')
eup_cds = id2seq('F:/work/gene_annotation/all_cds/peup_cds.fa')
ili_cds = id2seq('F:/work/gene_annotation/all_cds/pili.cds')
kor_cds = id2seq('F:/work/gene_annotation/all_cds/pkor_cds.fa')
las_cds = id2seq('F:/work/gene_annotation/all_cds/plas_cds.fa')
pru_cds = id2seq('E:/data/pruinosa/yangwenlu_huiyang/04.Ppr_35131.cds.fa')
pse_cds = id2seq('F:/work/gene_annotation/all_cds/ppse_cds.fa')
qio_cds = id2seq('F:/work/gene_annotation/all_cds/pqio_cds.fa')
rot_cds = id2seq('F:/work/gene_annotation/all_cds/prot_cds.fa')
sim_cds = id2seq('F:/work/gene_annotation/all_cds/psim.cds')
sze_cds = id2seq('F:/work/gene_annotation/all_cds/psze_cds.fa')
tri_cds = id2seq('F:/work/gene_annotation/all_cds/ptri_cds.fa')
tre_cds = id2seq('F:/work/gene_annotation/all_cds/ptre.cds')
wua_cds = id2seq('F:/work/gene_annotation/all_cds/pwua_cds.fa')
yun_cds = id2seq('F:/work/gene_annotation/all_cds/pyun_cds.fa')
ssuc_cds = id2seq('F:/work/gene_annotation/Ssuc/Ssuc.cds')
spur_cds = id2seq('F:/work/gene_annotation/Spur/Spur.cds')
sbra_cds = id2seq('F:/work/gene_annotation/Sbra/Sbra_cds.fa')

def spe_cds(idd):
    if 'Poade' in idd:
        s = ade_cds[idd]
    if 'alba' in idd:
        s = alb_cds[idd]
    if 'pal_pou' in idd:
        s = alby_cds[idd]
    if 'Podav' in idd:
        s = dav_cds[idd]
    if 'Podel' in idd:
        s = del_cds[idd]  
    if 'EUPHRATICA' in idd:
        s = eup_cds[idd]          
    if 'model' in idd:
        aa = idd.split('scaffold')[1]
        s = ili_cds[aa]
    if 'Pokor' in idd:
        s = kor_cds[idd]
    if 'Polas' in idd:
        s = las_cds[idd]        
    if 'Ppr' in idd:
        s = pru_cds[idd]
    if 'Popse' in idd:
        s = pse_cds[idd]
    if 'Qdy' in idd:
        s = qio_cds[idd]
    if 'Porot' in idd:
        s = rot_cds[idd]
    if 'Posim' in idd:
        s = sim_cds[idd]
    if 'Posze' in idd:
        s = sze_cds[idd]
    if 'Potra' in idd:
        s = tre_cds[idd]
    if 'Potri' in idd:
        s = tri_cds[idd]
    if 'Powua' in idd:
        s = wua_cds[idd]
    if 'Poyun' in idd:
        s = yun_cds[idd]
    if 'Sabra' in idd:
        s = sbra_cds[idd]
    if 'Sapur' in idd:
        s = spur_cds[idd]
    if 'EVM' in idd:
        s = ssuc_cds[idd]
    return s

for f in files:
    ids=[]
    seqs=[]
    for record in SeqIO.parse('Low_Copy_Orthologue_Sequences/'+f,'fasta'):
        ids.append(record.id)
    for idd in ids:
        seqs.append(spe_cds(idd))
    out_f = open('Low_Copy_Orthologue_Sequences_cds/'+f,'w')
    for i,iddd in enumerate(ids):
        out_f.write('>'+iddd+'\n')
        out_f.write(seqs[i]+'\n')    
    out_f.close()
    