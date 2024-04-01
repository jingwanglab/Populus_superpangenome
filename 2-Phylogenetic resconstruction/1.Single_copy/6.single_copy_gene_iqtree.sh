cd /usr_storage/stt/Populus_pangenome/single_copy_msa/gene_tree/
for file in /usr_storage/stt/Populus_pangenome/single_copy_msa/Single_Copy_Orthologue_Sequences_pep_mafft_coden_trimal/*.out
do
	iqtree -s $file -m MFP -bb 1000 -T 10 
done
