cd /usr_storage/stt/Populus_pangenome/low_copy/Low_Copy_Orthologue_Sequences/
out_dir="/usr_storage/stt/Populus_pangenome/low_copy/Low_Copy_Orthologue_Sequences_pep_mafft/"
for file in ./*.fa
do
	out_file=$out_dir$file".out"
	mafft --auto --thread 10 $file > $out_file
done

cd /usr_storage/stt/Populus_pangenome/low_copy/Low_Copy_Orthologue_Sequences_pep_mafft/
out_dir2="/usr_storage/stt/Populus_pangenome/low_copy/Low_Copy_Orthologue_Sequences_pep_mafft_coden/"
cds_dir="/usr_storage/stt/Populus_pangenome/low_copy/Low_Copy_Orthologue_Sequences_cds/"
for file in ./*.out
do
	out_file2=$out_dir2$file
	cds=${file:2:12}
	cds_file=$cds_dir$cds
	perl /usr_storage/software/pal2nal.v14/pal2nal.pl $file $cds_file -output fasta > $out_file2
done

