species='Pade'
cd /usr_storage/stt/Populus_pangenome/gene_methy/${species}/

bedtools flank -i ${species}_gene.bed -g ${species}_genome.len  -l 0 -r 2000 -s > ${species}_gene_down2k.bed
bedtools flank -i ${species}_gene.bed -g ${species}_genome.len  -l 2000 -r 0 -s > ${species}_gene_up2k.bed

for m in CHG CpG CHH
do
        bedtools intersect -a ${species}_gene_down2k.bed -b /usr_storage/stt/Populus_pangenome/methy_call/${species}/${m}.bed -wa -wb > ${species}_gene_down2k_${m}_intersect.bed
        bedtools intersect -a ${species}_gene_up2k.bed -b /usr_storage/stt/Populus_pangenome/methy_call/${species}/${m}.bed -wa -wb > ${species}_gene_up2k_${m}_intersect.bed
        bedtools intersect -a ${species}_gene.bed -b /usr_storage/stt/Populus_pangenome/methy_call/${species}/${m}.bed -wa -wb > ${species}_gene_${m}_intersect.bed
done
