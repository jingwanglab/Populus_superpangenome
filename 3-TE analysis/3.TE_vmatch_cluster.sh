#!/bin/bash
for dir in ./*
do
	cd $dir
	if [ -f "ltr_junction.fa" ];then
	mkdir 70
	mkdir 80
	mkdir 90
	mkvtree -db ltr_junction.fa -dna -pl -allout -v && vmatch -dbcluster 70 70 70/Cluster -s -identity 70 -exdrop 6 -seedlength 10 -d ltr_junction.fa && vmatch -dbcluster 80 80 80/Cluster -s -identity 80 -exdrop 5 -seedlength 15 -d ltr_junction.fa &&	vmatch -dbcluster 90 90 90/Cluster -s -identity 90 -exdrop 4 -seedlength 20 -d ltr_junction.fa
	cd ../
	else
	echo "$dir no file"
	cd ../
	fi
done
