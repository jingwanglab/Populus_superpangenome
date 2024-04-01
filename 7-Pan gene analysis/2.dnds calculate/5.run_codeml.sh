#!/bin/bash

for i in {4..19}
do
	cd "/usr_storage/stt/Populus_pangenome/Populus_pangene/dnds/"$i"/single_copy_dnds"
	for dd in ./*
	do
		cd $dd
		/usr_storage/software/paml4.9i/bin/codeml codeml_0.ctl
		cd ..
	done
done
