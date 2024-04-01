# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:23:08 2024

@author: Stt
"""
import pandas as pd

### The ratio of hemizyous genes in pangenes
hemi_gene = pd.read_csv('F:/work/Populus_pangenome/SV/hemi_gene/hemi_gene.csv')
pan = pd.read_csv('F:/work/Populus_pangenome/Populus_pangene/pan_gene/pangene_compare.csv')
pan = pan[['species','gene_id','pan_type']]

pan=pan[pan['species']!='Palba']
pan=pan[pan['species']!='Palby']
pan=pan[pan['species']!='Ptre']
pan=pan[pan['species']!='Pqio']
pan=pan[pan['species']!='Peup']
pan=pan[pan['species']!='Ppru']
pan=pan[pan['species']!='Pili']
pan=pan[pan['species']!='Pdel']
pan=pan[pan['species']!='Ptri']

df = pd.merge(hemi_gene, pan, how='left')
a = df.groupby(['species','pan_type'])['pan_type'].count()
a = a.to_frame()
a.columns=['count']
a = a.reset_index()
b = df.groupby(['species'])['pan_type'].count()
b = b.to_frame()
b.columns=['all']
b = b.reset_index()

pan_hemi = pd.merge(a,b,how='left')
pan_hemi['ratio'] = pan_hemi['count']/pan_hemi['all']

### The ratio of hemizyous genes in dup genes
dup = pd.read_csv('F:/work/Populus_pangenome/Dup_gene/all_dupgene.csv')
dup=dup[dup['species']!='Palby']
dup=dup[dup['species']!='Palba']
dup=dup[dup['species']!='Ptre']
dup=dup[dup['species']!='Pqio']
dup=dup[dup['species']!='Peup']
dup=dup[dup['species']!='Pili']
dup=dup[dup['species']!='Ppru']
dup=dup[dup['species']!='Pdel']
dup=dup[dup['species']!='Ptri']
dup = dup[['species','gene_id','dup_type']]
df2 = pd.merge( hemi_gene, dup, how='left')
a = df2.groupby(['species','dup_type'])['dup_type'].count()
a = a.to_frame()
a.columns=['count']
a = a.reset_index()
b = df2.groupby(['species'])['dup_type'].count()
b = b.to_frame()
b.columns=['all']
b = b.reset_index()

dup_hemi = pd.merge(a,b,how='left')
dup_hemi['ratio'] = dup_hemi['count']/dup_hemi['all']




##### The ratio of different types of pan/dup gene in random genes
core_random=[]
softcore_random=[]
dis_random=[]
private_random=[]

WGD_random=[]
TD_random=[]
PD_random=[]
TRD_random=[]
DSD_random=[]
sin_random=[]


for i in range(1,1001):
    random_gene = pan.sample(n=len(hemi_gene),random_state=i)
    random_gene = pd.merge(random_gene, dup)

    core_random.append(len(random_gene[random_gene['pan_type']=='core'])/len(random_gene))
    softcore_random.append(len(random_gene[random_gene['pan_type']=='softcore'])/len(random_gene))
    dis_random.append(len(random_gene[random_gene['pan_type']=='dispensable'])/len(random_gene))
    private_random.append(len(random_gene[random_gene['pan_type']=='private'])/len(random_gene))

    WGD_random.append(len(random_gene[random_gene['dup_type']=='WGD'])/len(random_gene))
    TD_random.append(len(random_gene[random_gene['dup_type']=='TD'])/len(random_gene))
    PD_random.append(len(random_gene[random_gene['dup_type']=='PD'])/len(random_gene))
    TRD_random.append(len(random_gene[random_gene['dup_type']=='TRD'])/len(random_gene))
    DSD_random.append(len(random_gene[random_gene['dup_type']=='DSD'])/len(random_gene))
    sin_random.append(len(random_gene[random_gene['dup_type']=='Singleton'])/len(random_gene))

random_r = pd.concat([core_random, softcore_random, dis_random, private_random, WGD_random,TD_random, PD_random, TRD_random, DSD_random, sin_random], axis=1)
random_r.to_csv('F:/work/Populus_pangenome/SV/dup_pan_in_randomGenes.csv',index=False)



