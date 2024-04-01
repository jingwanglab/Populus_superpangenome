cd /usr_storage/stt/Populus_pangenome/single_copy_msa/gene_tree/
cat *treefile >> all_gene.treefile
java -jar astral.5.6.1.jar -i all_gene.treefile -o /usr_storage/stt/Populus_pangenome/single_copy_msa/species.astral.tre
