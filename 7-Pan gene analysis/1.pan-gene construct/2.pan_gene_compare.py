# -*- coding: utf-8 -*-
"""
Created on Tue May  4 18:10:58 2021

@author: Stt
"""

import pandas as pd


core = pd.read_csv('F:/work/Populus_pangenome/Populus_pangene/pan_gene/all_gene.list', header=None)
softcore = pd.read_csv('F:/work/Populus_pangenome/Populus_pangene/pan_gene/softcore/all_gene.list', header=None)
dis = pd.read_csv('F:/work/Populus_pangenome/Populus_pangene/pan_gene/dis/all_gene.list', header=None)
spe = pd.read_csv('F:/work/Populus_pangenome/Populus_pangene/pan_gene/private/all_gene.list', header=None)

core.columns=['gene']
softcore.columns=['gene']
dis.columns = ['gene']
spe.columns = ['gene']

core['pan_type'] = 'core'
softcore['pan_type'] = 'softcore'
dis['pan_type'] = 'dispensable'
spe['pan_type'] = 'private'
genes = pd.concat([core, softcore, dis, spe])

gene_cdslen = pd.read_csv('F:/work/Populus_pangenome/Populus_pangene/pan_gene/gene_cdslen.csv')
gene_cdslen = gene_cdslen[['species','gene_id','cds_len']]
fpkm = pd.read_csv('F:/work/Populus_pangenome/Populus_pangene/gene_expression/all_gene_fpkm.csv')
fpkm = fpkm[['gene_id', 'FPKM']]
tau = pd.read_csv('F:/work/Populus_pangenome/Populus_pangene/tau/tau.csv')
tau = tau[['gene_id', 'tau']]
tedis = pd.read_csv('F:/work/Populus_pangenome/Populus_pangene/pan_gene/pan_gene_diste.csv')
tedis = tedis[['gene_id', 'gene2te_distance']]
atac = pd.read_csv('F:/work/Populus_pangenome/ATAC/all_peak2gene.csv')
atac = atac[['gene_id','peak2gene_distance']]



df = pd.merge(genes, gene_cdslen, on='gene_id',how='left')
df2 = pd.merge(df, fpkm, on='gene_id',how='left')
df3 = pd.merge(df2, tau, on='gene_id',how='left')
df4 = pd.merge(df3, tedis, on='gene_id',how='left')
df5 = pd.merge(df4, atac, on='gene_id',how='left')
df5.to_csv('F:/work/Populus_pangenome/Populus_pangene/pan_gene/pangene_compare.csv', index=False)
