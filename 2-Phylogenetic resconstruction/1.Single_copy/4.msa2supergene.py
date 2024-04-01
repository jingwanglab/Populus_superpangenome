# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:30:48 2020

@author: stt
"""

import os
from Bio import SeqIO

path = '/usr_storage/stt/Populus_pangenome/single_copy_msa/Single_Copy_Orthologue_Sequences_pep_mafft_coden_trimal/'



Pade_seqs = ''
Pdav_seqs = ''
Palba_seqs = ''
Palbay_seqs = ''
Peup_seqs = ''
Ptre_seqs = ''
Ptri_seqs = ''
Pdel_seqs = ''
Pili_seqs = ''
Pkor_seqs = ''
Plas_seqs = ''
Ppru_seqs = ''
Ppse_seqs = ''
Pqio_seqs = ''
Prot_seqs = ''
Psim_seqs = ''
Psze_seqs = ''
Pwua_seqs = ''
Pyun_seqs = ''
Sbra_seqs = ''
Spur_seqs = ''
Ssuc_seqs = ''


files = os.listdir(path) 
for file in files: 
    file_path = path + file  
    for record in SeqIO.parse(file_path,'fasta'):
        id = record.id
        seq= str(record.seq)
        

        if "Poade" in id:
            Pade_seqs=Pade_seqs+seq

        if "Podav" in id:
            Pdav_seqs=Pdav_seqs+seq

        if "Palba" in id:
            Palba_seqs=Palba_seqs+seq
            
        if "pal_pou" in id:
            Palbay_seqs=Palbay_seqs+seq

        if "POPULUS_EUPHRATICA" in id:
            Peup_seqs=Peup_seqs+seq

        if "Potra" in id:
            Ptre_seqs=Ptre_seqs+seq
            
        if "Potri" in id:
            Ptri_seqs=Ptri_seqs+seq

        if "Podel" in id:
            Pdel_seqs=Pdel_seqs+seq
            
        if "model" in id:
            Pili_seqs = Pili_seqs+seq

        if "Pokor" in id:
            Pkor_seqs=Pkor_seqs+seq

        if "Polas" in id:
            Plas_seqs=Plas_seqs+seq

        if "Ppr" in id:
            Ppru_seqs=Ppru_seqs+seq

        if "Popse" in id:
            Ppse_seqs=Ppse_seqs+seq

        if "Qdy" in id:
            Pqio_seqs = Pqio_seqs+seq

        if "Porot" in id:
            Prot_seqs=Prot_seqs+seq

        if "Posim" in id:
            Psim_seqs=Psim_seqs+seq

        if "Posze" in id:
            Psze_seqs=Psze_seqs+seq

        if "Powua" in id:
            Pwua_seqs=Pwua_seqs+seq

        if "Poyun" in id:
            Pyun_seqs=Pyun_seqs+seq

        if "Sabra" in id:
            Sbra_seqs=Sbra_seqs+seq

        if "Sapur" in id:
            Spur_seqs=Spur_seqs+seq

        if "EVM" in id:
            Ssuc_seqs=Ssuc_seqs+seq
            

speciesa_num = 22
length = len(Pdav_seqs)
with open('/usr_storage/stt/Populus_pangenome/single_copy_msa/supergene_pep_coden.phy', 'w') as fout:
    fout.write('%d %d\n' % (speciesa_num, length))
    fout.write('%-20s %s\n' % ('Pade',Pade_seqs))
    fout.write('%-20s %s\n' % ('Pdav',Pdav_seqs))
    fout.write('%-20s %s\n' % ('Palb',Palba_seqs))
    fout.write('%-20s %s\n' % ('Palby',Palbay_seqs))
    fout.write('%-20s %s\n' % ('Ptre',Ptre_seqs))
    fout.write('%-20s %s\n' % ('Ptri',Ptri_seqs))
    fout.write('%-20s %s\n' % ('Pdel',Pdel_seqs))
    fout.write('%-20s %s\n' % ('Peup',Peup_seqs))
    fout.write('%-20s %s\n' % ('Ppru',Ppru_seqs))
    fout.write('%-20s %s\n' % ('Pili',Pili_seqs))
    fout.write('%-20s %s\n' % ('Pqio',Pqio_seqs))
    fout.write('%-20s %s\n' % ('Prot',Prot_seqs))
    fout.write('%-20s %s\n' % ('Psim',Psim_seqs))
    fout.write('%-20s %s\n' % ('Pkor',Pkor_seqs))
    fout.write('%-20s %s\n' % ('Psze',Psze_seqs))
    fout.write('%-20s %s\n' % ('Pyun',Pyun_seqs)) 
    fout.write('%-20s %s\n' % ('Pwua',Pwua_seqs))
    fout.write('%-20s %s\n' % ('Plas',Plas_seqs))
    fout.write('%-20s %s\n' % ('Ppse',Ppse_seqs))    
    fout.write('%-20s %s\n' % ('Sbra',Sbra_seqs))
    fout.write('%-20s %s\n' % ('Ssuc',Ssuc_seqs))
    fout.write('%-20s %s' % ('Spur',Spur_seqs))

fout.close()
    
