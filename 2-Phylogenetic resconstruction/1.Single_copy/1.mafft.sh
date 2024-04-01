cd /usr_storage/stt/Populus_pangenome/orthofinder/pep/OrthoFinder/Results_Jan22/Single_Copy_Orthologue_Sequences/
out_dir="/usr_storage/stt/Populus_pangenome/single_copy_msa/Single_Copy_Orthologue_Sequences_pep_mafft/"
for file in ./*.fa
do
	out_file=$out_dir$file".out"
	mafft --auto --thread 10 $file > $out_file
done
