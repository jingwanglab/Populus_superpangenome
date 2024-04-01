bedtools intersect -a RefPade.hotspots.bed -b Pade_hemi_gene.bed -wao > hotspot_hemigene.overlap
count=1;while(($count<1001));do bedtools shuffle -i RefPade.hotspots.bed -g Pade.genome.leng -chrom > ./hotspot_random/random_${count}.bed;((count=$count+1));done;
cd ./hotspot_random/
for file in ./*.bed
do
	bedtools intersect -a $file -b ../Pade_hemi_gene.bed -wao > ../hotspot_random_hemigene/${file%.*}".overlap"
done
