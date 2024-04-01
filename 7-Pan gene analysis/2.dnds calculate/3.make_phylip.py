# -*- coding: utf-8 -*-
"""
Created on Fri May 14 18:15:23 2021

@author: Stt
"""

import os
from Bio import SeqIO


path = '/usr_storage/stt/Populus_pangenome/Populus_pangene/dnds/'

for i in range(4,20):
    files = os.listdir(path+str(i)+'/single_copy')  
    out_path='/usr_storage/stt/Populus_pangenome/Populus_pangene/dnds/'+str(i)+'/single_copy_phylip/'
    for file in files: 
        if file.split('.')[-1]=='trimal':                
            file_path = path+str(i)+'/single_copy/'+file 
            ids=[]
            seqs=[]
            for record in SeqIO.parse(file_path,'fasta'):
                ids.append(record.id)
                seqs.append(str(record.seq))
            dicts = dict(zip(ids, seqs))
            with open(out_path+file.split('.')[0], 'w') as fout:
                fout.write('%d %d\n' % (len(dicts), len(seqs[0])))
                for k in dicts.keys():
                    fout.write(k+'    '+dicts[k]+'\n')
            fout.close()
