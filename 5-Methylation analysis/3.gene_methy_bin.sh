species='Pade'
cd /usr_storage/stt/Populus_pangenome/gene_methy/${species}/

bedtools flank -i ${species}_gene.bed -g ${species}_genome.len  -l 0 -r 2000 -s > ${species}_gene_down2k.bed
bedtools flank -i ${species}_gene.bed -g ${species}_genome.len  -l 2000 -r 0 -s > ${species}_gene_up2k.bed
awk '($6=="-")' ${species}_gene_down2k.bed | bedtools makewindows -b - -n 20 -i srcwinnum -reverse > ${species}_gene_down2k_m.bed
awk '($6=="+")' ${species}_gene_down2k.bed | bedtools makewindows -b - -n 20 -i srcwinnum > ${species}_gene_down2k_p.bed
awk '($6=="-")' ${species}_gene_up2k.bed | bedtools makewindows -b - -n 20 -i srcwinnum -reverse > ${species}_gene_up2k_m.bed
awk '($6=="+")' ${species}_gene_up2k.bed | bedtools makewindows -b - -n 20 -i srcwinnum > ${species}_gene_up2k_p.bed
awk '($6=="-")' ${species}_gene.bed | bedtools makewindows -b - -n 30 -i srcwinnum -reverse > ${species}_gene_m.bed
awk '($6=="+")' ${species}_gene.bed | bedtools makewindows -b - -n 30 -i srcwinnum > ${species}_gene_p.bed
cat ${species}_gene_down2k_m.bed ${species}_gene_down2k_p.bed > ${species}_gene_down2k_20bin.bed
cat ${species}_gene_up2k_m.bed ${species}_gene_up2k_p.bed > ${species}_gene_up2k_20bin.bed
cat ${species}_gene_m.bed ${species}_gene_p.bed > ${species}_gene_30bin.bed

for m in CHG CpG CHH
do
        bedtools intersect -a ${species}_gene_down2k_20bin.bed -b /usr_storage/stt/Populus_pangenome/methy_call/${species}/${m}.bed -wa -wb > ${species}_gene_down2k_20bin_${m}_intersect.bed
        bedtools intersect -a ${species}_gene_up2k_20bin.bed -b /usr_storage/stt/Populus_pangenome/methy_call/${species}/${m}.bed -wa -wb > ${species}_gene_up2k_20bin_${m}_intersect.bed
        bedtools intersect -a ${species}_gene_30bin.bed -b /usr_storage/stt/Populus_pangenome/methy_call/${species}/${m}.bed -wa -wb > ${species}_gene_30bin_${m}_intersect.bed
done
