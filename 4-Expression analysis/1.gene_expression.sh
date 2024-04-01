java -jar /usr_storage/software/Trimmomatic-0.36/trimmomatic-0.36.jar PE -threads 8 r1.fq.gz r2.fq.gz r1.clean.fq.gz r1.un.fq.gz r2.clean.fq.gz r2.un.fq.gz ILLUMINACLIP:/usr_storage/software/Trimmomatic-0.36/adapters/TruSeq3-SE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36 HEADCROP:13 
bowtie2-build --thread 5 ./genome_fasta/species_genome.fasta ./genome_index/species_genome 
/usr_storage/software/tophat-2.1.1.Linux_x86_64/tophat -o root.tophat.out -p 5 ./genome_index/species_genome r1.clean.fq.gz r2.clean.fq.gz
/usr_storage/software/cufflinks-2.2.1.Linux_x86_64/cufflinks -p 5 -G ./gene_annotation/species_gene.gff -b ./genome_fasta/species_genome.fasta -o cufflinks.out accepted_hits.bam

