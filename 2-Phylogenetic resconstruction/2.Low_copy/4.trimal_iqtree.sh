cd /usr_storage/stt/Populus_pangenome/low_copy/Low_Copy_Orthologue_Sequences_pep_mafft_coden_rename/
out_dir="/usr_storage/stt/Populus_pangenome/low_copy/Low_Copy_Orthologue_Sequences_pep_mafft_coden_rename_tre/"
for file in ./*.out
do
	out_file=$out_dir$file
	/usr_storage/software/trimal-trimAl/source/trimal -in $file -out $out_file -automated1
	iqtree -s $out_file -m MFP -bb 1000 -T 20
done
