cat /usr_storage/stt/Populus_pangenome/low_copy/Low_Copy_Orthologue_Sequences_pep_mafft_coden_rename_tre/*treefile >> low_copy_gene.trees
java -jar -D"java.library.path=/usr_storage/software/ASTRAL-MP/lib" /usr_storage/software/ASTRAL-MP/astral.5.15.5.jar -i low_copy_gene.trees -a genemap.txt -o low_copy_astral.tre
