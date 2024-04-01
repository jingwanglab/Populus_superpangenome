# -*- coding: utf-8 -*-
"""
Created on Thu May 13 12:58:12 2021

@author: Stt
"""


import pandas as pd
import os
import shutil

orth_path ='/usr_storage/stt/Populus_pangenome/Populus_pangene/Orthogroup_Sequences/' 
out_path='/usr_storage/stt/Populus_pangenome/Populus_pangene/dnds/'
data = pd.read_csv('/usr_storage/stt/Populus_pangenome/Populus_pangene/Orthogroups.GeneCount.tsv', sep='\t')

df4 = data[data['Total']==4]
df5 = data[data['Total']==5]
df6 = data[data['Total']==6]
df7 = data[data['Total']==7]
df8 = data[data['Total']==8]
df9 = data[data['Total']==9]
df10 = data[data['Total']==10]
df11 = data[data['Total']==11]
df12 = data[data['Total']==12]
df13 = data[data['Total']==13]
df14 = data[data['Total']==14]
df15 = data[data['Total']==15]
df16 = data[data['Total']==16]
df17 = data[data['Total']==17]
df18 = data[data['Total']==18]


def drop(df):    
    df.drop(df[df.pade >1].index, inplace=True)
    df.drop(df[df.palb >1].index, inplace=True)
    df.drop(df[df.palby >1].index, inplace=True)
    df.drop(df[df.pdav >1].index, inplace=True)
    df.drop(df[df.pdel >1].index, inplace=True)
    df.drop(df[df.peup >1].index, inplace=True)
    df.drop(df[df.pili >1].index, inplace=True)
    df.drop(df[df.pkor >1].index, inplace=True)
    df.drop(df[df.plas >1].index, inplace=True)
    df.drop(df[df.ppru >1].index, inplace=True)
    df.drop(df[df.ppse >1].index, inplace=True)
    df.drop(df[df.pqio >1].index, inplace=True)
    df.drop(df[df.prot >1].index, inplace=True)
    df.drop(df[df.psim >1].index, inplace=True)
    df.drop(df[df.psze >1].index, inplace=True)
    df.drop(df[df.ptre >1].index, inplace=True)
    df.drop(df[df.ptri >1].index, inplace=True)
    df.drop(df[df.pwua >1].index, inplace=True)
    df.drop(df[df.pyun >1].index, inplace=True)
    return df

df4 = drop(df4)
df5 = drop(df5)
df6 = drop(df6)
df7 = drop(df7)
df8 = drop(df8)
df9 = drop(df9)     
df10 = drop(df10)
df11 = drop(df11)
df12 = drop(df12)
df13 = drop(df13)
df14 = drop(df14)
df15 = drop(df15)
df16 = drop(df16)
df17 = drop(df17)
df18 = drop(df18)


for i in range(4,19):
    s = 'df'+str(i)
    orths = globals()[s]['Orthogroup'].tolist()
    os.makedirs(out_path + str(i) +'/single_copy') 
    for o in orths:
        shutil.copyfile(orth_path+o+'.fa',out_path+str(i)+'/single_copy/'+o+'.fa')


