# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 16:30:40 2022

@author: Stt
"""

#maf2phy and filter sites requiring each site to be present in at least one species per clade
import re
from Bio import AlignIO,SeqIO

chrs=['Chr01','Chr02','Chr03','Chr04','Chr05','Chr06','Chr07','Chr08','Chr09','Chr10',
      'Chr11','Chr12','Chr13','Chr14','Chr15','Chr16','Chr17','Chr18','Chr19']

for ch in chrs:

	data  = open('/usr_storage/stt/Populus_pangenome/msa_tree/len100/Ptri_as_ref_fil_'+ch+'.maf2').readlines()
	data.append('\n')

	path='/usr_storage/stt/Populus_pangenome/msa_tree/len100/site_filter/'+ch+'/'

	clade2_s=['','','','','','','']
	clade2=['Pade','Pdav','Prot','Palby','Palb','Pqio','Ptre']
	clade1_s=['','','','','','','','','']
	clade1 = ['Ptri','Pdel','Pkor','Plas','Psim','Psze','Ppse','Pyun','Pwua']
	clade3=['Pili','Peup','Ppru']
	clade3_s=['','','']
	salix=['Ssuc','Spur','Sbra']
	salix_s=['','','']

	dict_clade2s=dict(zip(clade2, clade2_s))
	dict_clade1s=dict(zip(clade1, clade1_s))
	dict_clade3s=dict(zip(clade3, clade3_s))
	dict_salix=dict(zip(salix, salix_s))

	block=[]
	for i,line in enumerate(data):
		if len(line) <3:            
			if len(block)>1:
				length=len(block[0].strip('\n').split('\t')[-1])
				dict_clade2={}
				dict_clade1={}
				dict_clade3={}
				dict_salix={}
				for sp in clade2: 
					dict_clade2[sp]='-'*length                
				for sp in clade1: 
					dict_clade1[sp]='-'*length    
				for sp in clade3: 
					dict_clade3[sp]='-'*length                
				for sp in salix: 
					dict_salix[sp]='-'*length    
				for bl in block:
					sp = bl.split('\t')[1].split('.')[0]
					if sp in clade2:
						dict_clade2[sp]=bl.strip('\n').split('\t')[-1]
					if sp in clade1:
						dict_clade1[sp]=bl.strip('\n').split('\t')[-1]
					if sp in clade3:
						dict_clade3[sp]=bl.strip('\n').split('\t')[-1]
					if sp in salix:
						dict_salix[sp]=bl.strip('\n').split('\t')[-1]
				for key in dict_clade2s.keys():
					dict_clade2s[key]=dict_clade2s[key]+dict_clade2[key]
				for key in dict_clade1s.keys():
					dict_clade1s[key]=dict_clade1s[key]+dict_clade1[key]
				for key in dict_clade3s.keys():
					dict_clade3s[key]=dict_clade3s[key]+dict_clade3[key]
				for key in dict_salix.keys():
					dict_salix[key]=dict_salix[key]+dict_salix[key]
			block=[]
			continue
		if i%20000==0:
			print ('line:'+str(i))
		aa = line.strip('\n').split('\t')
		if aa[0]=='s':
			block.append(line)

	f= open(path+'clade2.fasta','w')
	for key in dict_clade2s.keys():
		f.write('>'+key+'\n'+dict_clade2s[key]+'\n')
	f.close()    

	f= open(path+'clade1.fasta','w')
	for key in dict_clade1s.keys():
		f.write('>'+key+'\n'+dict_clade1s[key]+'\n')
	f.close()    

	f= open(path+'clade3.fasta','w')
	for key in dict_clade3s.keys():
		f.write('>'+key+'\n'+dict_clade3s[key]+'\n')
	f.close()    

	f= open(path+'salix.fasta','w')
	for key in dict_salix.keys():
		f.write('>'+key+'\n'+dict_salix[key]+'\n')
	f.close()    
		  
	  

	alignment_clade2 = AlignIO.read(path+'clade2.fasta', "fasta")
	alignment_clade1 = AlignIO.read(path+'clade1.fasta', "fasta")
	alignment_clade3 = AlignIO.read(path+'clade3.fasta', "fasta")
	alignment_salix = AlignIO.read(path+'salix.fasta', "fasta")


	for column in range(0, alignment_salix.get_alignment_length()):
			if len(alignment_clade2[:,int(column)])-alignment_clade2[:,int(column)].count("-") >= 1:
				if len(alignment_clade1[:,int(column)])-alignment_clade1[:,int(column)].count("-") >= 1:
					if len(alignment_clade3[:,int(column)])-alignment_clade3[:,int(column)].count("-") >= 1:
						if len(alignment_salix[:,int(column)])-alignment_salix[:,int(column)].count("-") >= 1:                        
							if 'alignment_trimmed_clade2' in vars():
								x=int(column)
								y=column+1
								alignment_trimmed_clade2 += alignment_clade2[:,x:y]
								alignment_trimmed_clade1 += alignment_clade1[:,x:y]
								alignment_trimmed_clade3 += alignment_clade3[:,x:y]
								alignment_trimmed_salix += alignment_salix[:,x:y]
							else:
								x=int(column)
								y=column+1
								alignment_trimmed_clade2 = alignment_clade2[:,x:y]
								alignment_trimmed_clade1 = alignment_clade1[:,x:y]
								alignment_trimmed_clade3 = alignment_clade3[:,x:y]                            
								alignment_trimmed_salix = alignment_salix[:,x:y]

	f = open(path+ch+'.fasta','w')
	for record in alignment_trimmed_clade2:
		f.write('>'+record.id+'\n'+str(record.seq)+'\n')
	for record in alignment_trimmed_clade1:
		f.write('>'+record.id+'\n'+str(record.seq)+'\n')    
	for record in alignment_trimmed_clade3:
		f.write('>'+record.id+'\n'+str(record.seq)+'\n')
	for record in alignment_trimmed_salix:
		f.write('>'+record.id+'\n'+str(record.seq)+'\n')    
	f.close()
  