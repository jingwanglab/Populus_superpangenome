# Populus_superpangenome
Scripts for Shi et al. (2024). The suer-pangenome of Populus unveils genomic facets for its adaptation and diversification in widespread forest trees. Molecular Plant. 

# 1.Genome annotation

TE annotation: 

First, we performed command ‘perl EDTA.pl --genome genome.fasta --sensitive 1 -anno 1’ implemented in EDTA software to annotate TE. Then, we employed TEsorter to reclassfy reclassify TEs that were annotated as “LTR/unknown” by EDTA, using the command 'TEsorter LTR_unknown.fasta -db rexdb-plant -p 6'.

Gene annotation:

Gene annotation was performed in the pipeline https://github.com/jingwanglab/Populus_genomic_prediction_climate_vulnerability/tree/main/1-Genome_analyses

# 2.Phylogenetic reconstruction

Based on single-copy gene families:

(1) 1.mafft.sh - Script to align single-copy gene families.

(2) 2.pal2nal_batch.sh - Script to convert the protein sequence alignments into the corresponding codon alignments for each single-copy gene family.

(3) 3.trimal.sh - Script to remove poorly aligned regions.

(4) 4.msa2supergene.py - Script to join all gene sequences of each species into each super-gene sequence.

(5) 5.supergene_iqtree.sh - Script to construct concatenated tree.

(6) 6.single_copy_gene_iqtree.sh - Script to estimate gene tree for each single-copy gene family.

(7) 7.astral_tre.sh - Script to construct coalescent tree.

(8) 8.estimate_tree_confilct.sh - Script to quantify phylogenetic discordance between species tree and gene trees.

Based on low-copy gene families:

(1) 1.low_copy_extract.py - Script to extract low-copy orthologue from Orthifinder output

(2) 2.mafft_pal2nal.sh - Script to align low-copy gene families and convert the protein sequence alignments into the corresponding codon alignments.

(3) 3.gene_rename.py - Script to rename the gene IDs to meet ASTRAL input requirements.

(4) 4.trimal_iqtree.sh - Script to remove poorly aligned regions and estimate gene tree for each low-copy gene family.

(5) 5.astral.sh - Script to construct species tree.

Based on whole-genome alignments:

(1) First, we performed Cactus software to generate multiple whole-genome sequence alignment using default parameters. Then, we employed hal2maf to convert HAL file to MAF file, using the command ‘hal2maf cactus.hal Ptri_as_ref.maf --refGenome Ptri --noAncestors --onlyOrthologs --noDupes’.

(2) 1.maf_block_filter.py - Script to filter blocks requiring each block with at least one species per clade and >100 bp in length, and split the chromosomes

(3) 2.maf2phy.py - Script to filter sites requiring each site to be present in at least one species per clade, and transfer MAF file to sequence file.

(4) We employed IQTREE to construct species tree using the command ‘iqtree -s site_phy.fasta -m MFP -bb 1000 -T 20’.

# 3.TE analysis

Obtain TEs present in shared region or species-specific region:

For each species, run the following steps:

(1) Extract non-homolog regions in MAF file.

$python 1.maf_extract_nonhomo.py -i ./maf_file/species_as_ref.maf -o ./non_homolog/species_nonhomolog

(2) Merge non-homolog regions. 

$sort -k1,1 -k2,2n species_nonhomolog | awk -F '\t' '{print $1"\t"$2"\t"$3"\t"($2+$3)"\t"$4}' | awk -F '\t' '{print $1"\t"$2"\t"$4"\t"$5}' | bedtools merge -i - > ./non_homolog/species_nonhomolog_sort.merge.bed

(3) Obtain homolog regions.

$bedtools complement -i ./non_homo/species_nonhomolog_sort.merge.bed -g ./genome_bed/species_genome.bed > ./homo/species_homolog.bed

(4) Obtain TEs present in species-specific region.

$bedtools intersect -a ./non_homo/species_nonhomolog_sort.merge.bed -b species_TE.bed -wao > species_nonhomolog_TE.intersect

(5) Obtain TEs present in shared region.

$bedtools intersect -a ./homo/species_homolog.bed -b species_TE.bed -wao > species_homolog_TE.intersect

TE cluster:

(1) 2.cluster_file_build.py - Script to generate TE files of pairwise poplar genomes for cluster.

(2) 3.TE_vmatch_cluster.sh - Script to cluster syntentic fl-LTRs for pairwise poplar genomes.

TE distance:

(1) Obtain the distance of TE to closet gene.

$bedtools closest -a species_TE.bed -b species_gene.bed -D a > species_TE2gene.distance

(2) Obtain the distance of gene to closet upstream TE.

$bedtools closest -a species_gene.bed -b species_TE.bed -id -D a > species_gene2upTE.distance

# 4.Expression analysis

(1) 1.gene_expression.sh - Script to obtain gene expression (FPKM) based on RNA-seq data.

(2) 2.gene_TAU.py - Script to calculate tissue-specific expression for each of gene.

# 5.Methylation analysis

(1) 1.methy_call.sh - Script for methylation calling.

(2) 2.gene_methy.sh - Script to obtain methylation level in genes (body and flanking 2 kb regions).

(3) 3.gene_methy_bin.sh - Script to obtain methylation level in genes (body and flanking 2 kb regions based on divided bins).

# 6.ATAC peak calling

ATAC peak calling was performed in the pipeline https://github.com/jingwanglab/Populus_genomic_prediction_climate_vulnerability/tree/main/5-ATAC_call_peak

# 7.Pan-gene analysis

pan-gene construct：

(1) 1.pan_gene_extract.py - Script to extract pan-gene family and pan genes in Orthifinder output.

(2) 2.pan_gene_compare.py - Script to compare genome characteristics of different types of pan genes.

dN/dS calculate：

(1) 1.singlle_copy_orthextract.py - Script to extract single-copy ortholog groups (scOGs) containing more than three species.

(2) 2.build_tree.sh - Script to construct gene tree for each ortholog group.

(3) 3.make_phylip.py - Script to generate PHYLIP file format of sequence alignments.

(4) 4.make_codeml.py - Script to generate control file (codeml.ctl) for each ortholog group. 

(5) 5.run_codeml.sh - Script to estimate the dN/dS ratio for each ortholog group.

# 8.Dup gene analysis

(1) 1.dup_pan_compare.py - Script to compare different types of duplicate genes intersect with the pan-gene categories (core vs. variable).

(2) 2.wgd1to1_extract.py - Script to extract one-to-one WGD gene pairs.

(3) 3.wgd1to1_divergence.py - Script to calculate methylation divergence (CG) and expression divergence.

(4) 4.ks_correct.R - Script to correct Ks values.

(5) 5.wgd1to1_equal_ks.R - Script to select duplicate gene pairs locate within the confidence interval of corrected Ks peaks.

(6) 6.wgd1to1_equal_ks_compare.py - Script to compare genome characteristics of conserved and diverged WGD gene pairs.

# 9.SV analysis

Identify hemizygous genes:

For each species, run the following steps:

(1) minimap2 -t 20 -ax map-ont genome.fasta longreads.fastq.gz >minimap2.sam

(2) samtools view --threads 20 -Sb minimap2.sam > minimap2.bam

(3) samtools sort -@ 15 -O BAM -o minimap2.sort.bam minimap2.bam

(4) sniffles -t 15 --input minimap2.sort.bam --vcf species.vcf.gz

(5) less species.vcf.gz | grep -v ‘#’ | grep SVTYPE=DEL | grep ‘0/1’ > species.del01.vcf

(6) python 1.vcf2bed.py

(7) bedtools intersect -a species.del01.bed -b species.gene.bed -wo -F 1 > species_hemi.gene

SV characteristic analysis:

(1) 2.SV_stats.py - Script to extract SVs and perform preliminary statistics.

(2) 3.identify_hotspots.sh - Script to identify SV hotspots.

(3) 4.hotspots_random_hemigene.sh - Script to obtain the hemizyous genes in SV hotspot regions and genomic random regions.

(4) 5.pan_dup_in randomGene.py - Script to compare the ratios of different categoreis of pan-gene and duplicated gene in hemizygous genes and genes selected randomly.

# 10.Figure plot

A collection of scripts for drawing main figures in article.
