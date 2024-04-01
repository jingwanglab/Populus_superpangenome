cd /usr_storage/stt/Populus_pangenome/single_copy_msa/Single_Copy_Orthologue_Sequences_pep_mafft_coden/
out_dir="/usr_storage/stt/Populus_pangenome/single_copy_msa/Single_Copy_Orthologue_Sequences_pep_mafft_coden_trimal/"
for file in ./*.out
do
	out_file=$out_dir$file
	/usr_storage/software/trimal-trimAl/source/trimal -in $file -out $out_file -automated1
done
