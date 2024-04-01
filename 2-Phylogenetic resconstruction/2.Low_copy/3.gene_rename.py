# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:41:11 2021

@author: Stt
"""

from Bio import SeqIO
import os
in_path = 'Low_Copy_Orthologue_Sequences_pep_mafft_coden/'
files = os.listdir(in_path)  

out_path = 'Low_Copy_Orthologue_Sequences_pep_mafft_coden_rename/'

for f in files:
    ids=[]
    seqs=[]
    for record in SeqIO.parse(in_path+f,'fasta'):
        ids.append(record.id)
        seqs.append(str(record.seq))
                
    ids_n=[]    
    pade=1
    palb=1
    palby=1
    pdav=1
    pdel=1
    peup=1
    pili=1
    pkor=1
    plas=1
    ppru=1
    ppse=1
    pqio=1
    prot=1
    psim=1
    psze=1
    ptre=1
    ptri=1
    pwua=1
    pyun=1
    sbra=1
    spur=1
    ssuc=1
    
    for idd in ids:
        if 'Poade' in idd:
            s = 'Pade_'+ str(pade)
            pade+=1
        if 'alba' in idd:
            s = 'Palba_'+ str(palb)
            palb+=1
        if 'pal_pou' in idd:
            s = 'Palby_'+ str(palby)
            palby+=1
        if 'Podav' in idd:
            s = 'Pdav_'+ str(pdav)
            pdav+=1
        if 'Podel' in idd:
            s = 'Pdel_'+ str(pdel)
            pdel+=1
        if 'EUPHRATICA' in idd:
            s = 'Peup_'+ str(peup)
            peup+=1          
        if 'model' in idd:
            s = 'Pili_'+ str(pili)
            pili+=1
        if 'Pokor' in idd:
            s = 'Pkor_'+ str(pkor)
            pkor+=1
        if 'Polas' in idd:
            s = 'Plas_'+ str(plas)
            plas+=1
        if 'Ppr' in idd:
            s = 'Ppru_'+ str(ppru)
            ppru+=1
        if 'Popse' in idd:
            s = 'Ppse_'+ str(ppse)
            ppse+=1
        if 'Qdy' in idd:
            s = 'Pqio_'+ str(pqio)
            pqio+=1
        if 'Porot' in idd:
            s = 'Prot_'+ str(prot)
            prot+=1
        if 'Posim' in idd:
            s = 'Psim_'+ str(psim)
            psim+=1
        if 'Posze' in idd:
            s = 'Psze_'+ str(psze)
            psze+=1
        if 'Potra' in idd:
            s = 'Ptre_'+ str(ptre)
            ptre+=1
        if 'Potri' in idd:
            s = 'Ptri_'+ str(ptri)
            ptri+=1
        if 'Powua' in idd:
            s = 'Pwua_'+ str(pwua)
            pwua+=1
        if 'Poyun' in idd:
            s = 'Pyun_'+ str(pyun)
            pyun+=1
        if 'Sabra' in idd:
            s = 'Sbra_'+str(sbra)
            sbra+=1
        if 'Sapur' in idd:
            s = 'Spur_'+str(spur)
            spur+=1
        if 'EVM' in idd:
            s = 'Ssuc_'+str(ssuc)
            ssuc+=1
        
        ids_n.append(s)
    
    out_f = open(out_path+f,'w')
    for i,idd in enumerate(ids_n):
        out_f.write('>'+idd+'\n')
        out_f.write(seqs[i]+'\n')
    out_f.close()
        