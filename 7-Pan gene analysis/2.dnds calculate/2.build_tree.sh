path='/usr_storage/stt/Populus_pangenome/Populus_pangene/dnds/'
for i in {4..19}
do
	cd $path$i
	mkdir single_copy_tree single_copy_phylip single_copy_dnds
	cd ./single_copy
	for file in ./*.fa
	do
		mafft --auto --thread 10 $file > $file".mafft"
		perl /usr_storage/software/pal2nal.v14/pal2nal.pl $file".mafft" $path$i"/single_copy_cds/"$file -output fasta > $file".mafft.coden"
		/usr_storage/software/trimal-trimAl/source/trimal -in $file".mafft.coden" -out $file".mafft.coden.trimal" -automated1
		iqtree -s $file".mafft.coden.trimal" -m MFP -bb 1000 -T 10
		sed "1i $i      1" $file".mafft.coden.trimal.treefile" >  $path$i"/single_copy_tree/"$file".treefile"
	done
done
