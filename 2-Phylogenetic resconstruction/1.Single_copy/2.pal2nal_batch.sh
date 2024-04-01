cd /usr_storage/stt/Populus_pangenome/single_copy_msa/Single_Copy_Orthologue_Sequences_pep_mafft/
out_dir="/usr_storage/stt/Populus_pangenome/single_copy_msa/Single_Copy_Orthologue_Sequences_pep_mafft_coden/"
cds_dir="/usr_storage/stt/Populus_pangenome/single_copy_msa/Single_Copy_Orthologue_Sequences_cds/"
for file in ./*.out
do
	out_file=$out_dir$file
	cds=${file:2:12}
	cds_file=$cds_dir$cds
	perl /usr_storage/software/pal2nal.v14/pal2nal.pl $file $cds_file -output fasta > $out_file
done

