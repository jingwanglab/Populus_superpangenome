# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 15:30:30 2022

@author: Stt
"""
#Keep blocks with at least one species present in each clade and >100 bp in length and split the chromosomes
data = open('/usr_storage/stt/Populus_pangenome/msa_tree/Ptri_as_ref.maf').readlines()
data.append('\n')
clade2=['Pade','Pdav','Prot','Palby','Palb','Pqio','Ptre']
clade1 = ['Ptri','Pdel','Pkor','Plas','Psim','Psze','Ppse','Pyun','Pwua']
clade3=['Pili','Peup','Ppru']
salix=['Ssuc','Spur','Sbra']

block=[]

chrs=['Chr01','Chr02','Chr03','Chr04','Chr05','Chr06','Chr07','Chr08','Chr09','Chr10',
      'Chr11','Chr12','Chr13','Chr14','Chr15','Chr16','Chr17','Chr18','Chr19']

lists=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
dicts=dict(zip(chrs,lists))

for i,line in enumerate(data):
    if i%100000==0:
        print('process line:'+str(i))
    if len(line.strip('\n')) <3:
        if len(block)>3:
            if int(block[0].split('\t')[3])>100:
                ch = block[0].split('\t')[1].split('.')[1]
                if ch in chrs:
                    spes=[]
                    for ll in block:
                        spe = ll.split('\t')[1].split('.')[0]
                        spes.append(spe)
                    if len(set(spes))>3:
                        clade2_n=0
                        clade1_n=0
                        clade3_n=0
                        salix_n=0
                        for sp in clade2:
                            if sp in spes:
                                clade2_n=clade2_n+1
                        for sp in clade1:
                            if sp in spes:
                                clade1_n=clade1_n+1
                        for sp in clade3:
                            if sp in spes:
                                clade3_n=clade3_n+1
                        for sp in salix:
                            if sp in spes:
                                salix_n=salix_n+1
                        if clade2_n>0:
                            if clade1_n>0:
                                if clade3_n>0:
                                    if salix_n>0:    
                                        dicts[ch].append('a'+'\n')
                                        for ll in block:                            
                                            dicts[ch].append(ll)        
        block=[]        
        continue
    aa = line.strip('\n').split('\t')
    if aa[0]=='s':
        block.append(line)

for key in dicts.keys():    
    f=open('/usr_storage/stt/Populus_pangenome/msa_tree/len100/Ptri_as_ref_fil_'+key+'.maf','w')
    for ll in dicts[key]:
        f.write(ll)
    f.close()
    


##### Filter paralogous regions   
from collections import defaultdict
import os

path='/usr_storage/stt/Populus_pangenome/msa_tree/len100/'
files = os.listdir(path)
for fi in files:
    data = open(path+fi).readlines()
    data.append('\n')
    block=[]
    f=open(path+fi.split('.')[0]+'.maf2','w')
    for i,line in enumerate(data):
        if i%100000==0:
            print('process line:'+str(i))
        if len(line)<4:            
            if len(block)>3:
                dict_s = {'Spur':0,'Sbra':0,'Ssuc':0}
                spes=[]
                for bl in block:
                    sp = bl.split('\t')[1].split('.')[0]   
                    spes.append(sp)
                    
                dicts=defaultdict(list)
                for bl in block:
                    sp = bl.split('\t')[1].split('.')[0]   
                    if sp=='Ssuc':
                        dict_s['Ssuc']=int(bl.split('\t')[3])
                    if sp=='Spur':
                        dict_s['Spur']=int(bl.split('\t')[3])
                    if sp=='Sbra':
                        dict_s['Sbra']=int(bl.split('\t')[3])
                    dicts[sp].append(bl)
                if dict_s['Ssuc']>5 or dict_s['Sbra']>5 or dict_s['Spur']>5:        
                    f.write('a'+'\n')
                    for sp in dicts.keys():
                        if len(dicts[sp])==1:                        
                                f.write(dicts[sp][0])
                        else:
                            if  int(dicts[sp][0].split('\t')[3]) >= int(dicts[sp][1].split('\t')[3]):
                                f.write(dicts[sp][0])
                            else:
                                f.write(dicts[sp][1])
            block=[]        
            continue
        aa = line.strip('\n').split('\t')
        if aa[0]=='s':
            block.append(line)
    
    f.close()
  