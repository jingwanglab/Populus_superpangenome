# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 10:37:59 2021

@author: Stt
"""


#1.Divide SYRI result files into those containing SNPs (snp.out) and those not containing SNPs (nosnp.out).

import pandas as pd
import re
import os 

path = 'F:/work/Populus_pangenome/syri/Ref_Ptri/'
spes = os.listdir(path)

for sp in spes:
    data = pd.read_csv(path+sp+'/syri.out',sep='\t',header=None,low_memory=False)
    data.columns=['ref_chr','ref_start','ref_end','ref_b','query_b','query_chr','query_start','query_end','sv_num','sv_parent','sv_type','dd']
        
    snp = data[data['sv_type']=='SNP']
    nosnp = data[data['sv_type']!='SNP']
        
    def syn_gr(aa):
        s = re.findall(r"\D+", aa)[0]
        return s
    
    snp['parent_type'] = snp.apply(lambda x: syn_gr(x['sv_parent']), axis=1)
    nosnp['parent_type'] = nosnp.apply(lambda x: syn_gr(x['sv_parent']), axis=1)
    #nosnp['parent_type'].value_counts()
    snp.to_csv(path+sp+'/snp.out',sep='\t',index=False)
    nosnp.to_csv(path+sp+'/nosnp.out',sep='\t',index=False)


#2.SV statistics (Syntenic and rearrangement)
import pandas as pd

path = 'F:/work/Populus_pangenome/syri/Ref_Ptri/'
spes = os.listdir(path)

def syn(a):
    if 'SYN' in a:
        return 'SYN'
    else:
        return 'GR'

for sp in spes:
    snp = pd.read_csv(path+sp+'/snp.out',sep='\t')
    
    snp['SYN'] = snp.apply(lambda x: syn(x['sv_parent']), axis=1)
    snp['SYN'].value_counts()
    
    nosnp = pd.read_csv(path+sp+'/nosnp.out',sep='\t')
    #nosnp['sv_type'].value_counts()
    
    trans = nosnp[(nosnp['sv_type']=='TRANS')|(nosnp['sv_type']=='INVTR')]
    trans[['query_start','query_end']]=trans[['query_start','query_end']].astype('int')
    trans['len']=abs(trans['query_end']-trans['query_start'])+1
    trans['len'].sum()
    def inter_intra(chr1, chr2):
        if chr1==chr2:
            return 'intra'
        else:
            return 'inter'
    trans['chr_type']=trans.apply(lambda x: inter_intra(x['ref_chr'],x['query_chr']), axis=1)
    trans['chr_type'].value_counts()
    trans.groupby(['chr_type'])['len'].sum()
    
    cpls = nosnp[nosnp['sv_type']=='CPL']
    dels = nosnp[nosnp['sv_type']=='DEL']
    cpgs = nosnp[nosnp['sv_type']=='CPG']
    inss = nosnp[nosnp['sv_type']=='INS']
    hdr = nosnp[nosnp['sv_type']=='HDR']
    
    hdr[['query_start','query_end']]= hdr[['query_start','query_end']].astype('int')
    hdr['sv_len'] = abs(hdr['query_end']- hdr['query_start'])+1
    hdr['SYN']=hdr.apply(lambda x: syn(x['sv_parent']), axis=1)
    hdr['SYN'].value_counts()
    hdr.groupby(['SYN'])['sv_len'].sum()
    
    inss[['ref_start','ref_end','query_start','query_end']]=inss[['ref_start','ref_end','query_start','query_end']].astype('int')
    inss['sv_len'] = abs(inss['query_end']- inss['query_start'])-abs(inss['ref_end']- inss['ref_start'])
    inss['SYN']= inss.apply(lambda x: syn(x['sv_parent']), axis=1)
    inss['SYN'].value_counts()
    inss.groupby(['SYN'])['sv_len'].sum()
    
    dels[['ref_start','ref_end','query_start','query_end']]=dels[['ref_start','ref_end','query_start','query_end']].astype('int')
    dels['sv_len'] = abs(dels['ref_end']- dels['ref_start'])-abs(dels['query_end']- dels['query_start'])
    dels['SYN']=dels.apply(lambda x: syn(x['sv_parent']), axis=1)
    dels['SYN'].value_counts()
    dels.groupby(['SYN'])['sv_len'].sum()
    
    cpgs[['ref_start','ref_end','query_start','query_end']]= cpgs[['ref_start','ref_end','query_start','query_end']].astype('int')
    cpgs['sv_len'] = abs(cpgs['query_end']- cpgs['query_start'])+1  
    cpgs['SYN']= cpgs.apply(lambda x: syn(x['sv_parent']), axis=1)
    cpgs['SYN'].value_counts()
    cpgs.groupby(['SYN'])['sv_len'].sum()
    
    cpls[['ref_start','ref_end','query_start','query_end']]= cpls[['ref_start','ref_end','query_start','query_end']].astype('int')
    cpls['sv_len'] = abs(cpls['ref_end']- cpls['ref_start'])+1  
    cpls['SYN']= cpls.apply(lambda x: syn(x['sv_parent']), axis=1)
    cpls['SYN'].value_counts()
    cpls.groupby(['SYN'])['sv_len'].sum()



#3. Extract 5 types of representative SVs for further analysis (ins, dels, inv, trans, dup; >50bp).

import pandas as pd
import os

path = 'F:/work/Populus_pangenome/syri/Ref_Ptri/'
spes = os.listdir(path)

for sp in spes:
    data = pd.read_csv(path+sp+'/nosnp.out',sep='\t',low_memory=False)
    
    dels = data[data['sv_type']=='DEL']
    inss = data[data['sv_type']=='INS']
    dels[['ref_start','ref_end','query_start','query_end']]=dels[['ref_start','ref_end','query_start','query_end']].astype('int')
    inss[['ref_start','ref_end','query_start','query_end']]=inss[['ref_start','ref_end','query_start','query_end']].astype('int')
    dels['sv_len'] = abs(dels['ref_end']-dels['ref_start'])+1-(abs(dels['query_end']-dels['query_start'])+1)
    inss['sv_len'] = abs(inss['query_end']-inss['query_start'])+1-(abs(inss['ref_end']-inss['ref_start'])+1)
    
    dels50 =dels[dels['sv_len']>50] 
    inss50 =inss[inss['sv_len']>50] 
    
    inv = data[data['sv_type']=='INV']
    inv[['ref_start','ref_end','query_start','query_end']]=inv[['ref_start','ref_end','query_start','query_end']].astype('int')
    inv['sv_len'] = abs(inv.ref_end-inv.ref_start)+1
    inv50 = inv[inv.sv_len >50]
    
    trans = data[(data['sv_type']=='TRANS')|(data['sv_type']=='INVTR')]
    trans[['ref_start','ref_end','query_start','query_end']]=trans[['ref_start','ref_end','query_start','query_end']].astype('int')
    trans['sv_len'] = abs(trans.ref_end-trans.ref_start)+1
    trans50 = trans[trans.sv_len >50]
    
    
    dup = data[(data['sv_type']=='DUP')|(data['sv_type']=='INVDP')]
    dup_gain =dup[dup['dd']=='copygain'] 
    dup_gain[['query_start','query_end']]=dup_gain[['query_start','query_end']].astype('int')
    dup_gain['sv_len'] = abs(dup_gain.query_end- dup_gain.query_start)+1
    dup_gain50 = dup_gain[dup_gain.sv_len > 50]
    dup_loss =dup[dup['dd']=='copyloss'] 
    dup_loss[['ref_start','ref_end']]=dup_loss[['ref_start','ref_end']].astype('int')
    dup_loss['sv_len'] = abs(dup_loss.ref_end- dup_loss.ref_start)+1
    dup_loss50 = dup_loss[dup_loss.sv_len > 50]
    
    inss50['sv_class']='Insertion'
    dels50['sv_class']='Deletion'
    inv50['sv_class']='Inversion'
    trans50['sv_class']='Translocation'
    dup_gain50['sv_class']='Dup_gain'
    dup_loss50['sv_class']='Dup_loss'
       
    df = pd.concat([inss50, dels50, inv50, trans50, dup_gain50,dup_loss50])
    
    df2 = df[['ref_chr', 'ref_start', 'ref_end','sv_class']]    
    df2['start'] = df2.apply(lambda x: int(x['ref_start']) if int(x['ref_start']) < int(x['ref_end']) else int(x['ref_end']), axis=1)
    df2['end'] = df2.apply(lambda x: int(x['ref_end']) if int(x['ref_start']) < int(x['ref_end']) else int(x['ref_start']), axis=1)
    df2 = df2[['ref_chr','start','end','sv_class']]
    df2.sort_values(['ref_chr', 'start'],inplace=True)
    df2.to_csv(path+sp+'/5type_len50.bed',index=False,header=None,sep='\t')    
    ins_o = df2[df2['sv_class']=='Insertion']
    del_o = df2[df2['sv_class']=='Deletion']
    inv_o = df2[df2['sv_class']=='Inversion']    
    trans_o = df2[df2['sv_class']=='Translocation']        
    dupg_o = df2[df2['sv_class']=='Dup_gain']        
    dupl_o = df2[df2['sv_class']=='Dup_loss']     
    ins_o.to_csv(path+sp+'/deletion.bed', header=None, index=False, sep='\t')
    del_o.to_csv(path+sp+'/insertion.bed', header=None, index=False, sep='\t')
    inv_o.to_csv(path+sp+'/inversion.bed', header=None, index=False, sep='\t')    
    trans_o.to_csv(path+sp+'/translocation.bed', header=None, index=False, sep='\t')
    dupg_o.to_csv(path+sp+'/dup_g.bed', header=None, index=False, sep='\t')
    dupl_o.to_csv(path+sp+'/dup_l.bed', header=None, index=False, sep='\t')   
    
    df3 = df[['query_chr', 'query_start','query_end','sv_class']]    
    df3['start'] = df3.apply(lambda x: int(x['query_start']) if int(x['query_start']) < int(x['query_end']) else int(x['query_end']), axis=1)
    df3['end'] = df3.apply(lambda x: int(x['query_end']) if int(x['query_start']) < int(x['query_end']) else int(x['query_start']), axis=1)
    df3 = df3[['query_chr','start','end','sv_class']]
    df3.sort_values(['query_chr', 'start'],inplace=True)   
    df3.to_csv(path+sp+'/query_5type_sv.bed',index=False,header=None,sep='\t') 
    

#4. SV length
import os
import pandas as pd

path = 'F:/work/Populus_pangenome/syri/Ref_Ptri/'
apath=[]
for maindir, subdir, file_name_list in os.walk(path):
    for filename in file_name_list:
        if '5type_len50.bed' in filename:
            apath.append(os.path.join(maindir, filename))
     
file_path=[]
for f in apath:
    f =f.replace("\\", "/")
    file_path.append(f)

df_all = pd.DataFrame()
for path in file_path:
    aa = path.split('/')
    df = pd.read_csv(path)
    df = df[['sv_class','sv_len']]
    df['species']=aa[-2]
    df_all = pd.concat([df_all, df])

df_all.to_csv(path+'/all_5type_len50.csv',index=False)