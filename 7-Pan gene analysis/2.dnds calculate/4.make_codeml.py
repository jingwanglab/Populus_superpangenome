# -*- coding: utf-8 -*-
"""
Created on Sat May 15 19:03:15 2021

@author: Stt
"""

import os

path = '/usr_storage/stt/Populus_pangenome/Populus_pangene/dnds/'
codeml_ctl_path='/usr_storage/stt/Populus_pangenome/Populus_pangene/dnds/codeml_0.ctl'

for i in range(4,20):

    tree_path = path+str(i)+'/single_copy_tree/'
    phy_path = path+str(i)+'/single_copy_phylip/'
    out_path = path+str(i)+'/single_copy_dnds/'
   
    tree_files = os.listdir(tree_path)
    
    for file in tree_files:
        os.system('mkdir '+out_path+file.split('.')[0])
        codeml = open(codeml_ctl_path).readlines()
        codeml[0] = '      seqfile = '+phy_path+file.split('.')[0]+'\n'
        codeml[1]= '     treefile = '+tree_path+file+'\n'
        codeml[2] = '      outfile = '+out_path+file.split('.')[0]+'/'+file.split('.')[0]+'.dnds'+'\n'
        code_new = open(out_path+file.split('.')[0]+'/codeml_0.ctl','w')
        code_new.writelines(codeml)
        code_new.close()
    #    os.system('/usr_storage/software/paml4.9i/bin/codeml '+ out_path+file.split('.')[0]+'/codeml_0.ctl')
