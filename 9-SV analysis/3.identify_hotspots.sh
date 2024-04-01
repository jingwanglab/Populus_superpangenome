for i in {Pade,Palby,Pdav,Pdel,Peup,Pkor,Plas,Ppse,Pqio,Prot,Psim,Psze,Ptre,Pwua,Pyun}; do bedtools merge -i /usr_storage/stt/syri/Ref_Ptri/$i/insertion.bed > /usr_storage/stt/syri/Ref_Ptri/$i/insertion_m.bed; done   
for i in {Pade,Palby,Pdav,Pdel,Peup,Pkor,Plas,Ppse,Pqio,Prot,Psim,Psze,Ptre,Pwua,Pyun}; do bedtools merge -i /usr_storage/stt/syri/Ref_Ptri/$i/deletion.bed > /usr_storage/stt/syri/Ref_Ptri/$i/deletion_m.bed; done 
for i in {Pade,Palby,Pdav,Pdel,Peup,Pkor,Plas,Ppse,Pqio,Prot,Psim,Psze,Ptre,Pwua,Pyun}; do bedtools merge -i /usr_storage/stt/syri/Ref_Ptri/$i/inversion.bed > /usr_storage/stt/syri/Ref_Ptri/$i/inversion_m.bed; done 
for i in {Pade,Palby,Pdav,Pdel,Peup,Pkor,Plas,Ppse,Pqio,Prot,Psim,Psze,Ptre,Pwua,Pyun}; do bedtools merge -i /usr_storage/stt/syri/Ref_Ptri/$i/translocation.bed > /usr_storage/stt/syri/Ref_Ptri/$i/translocation_m.bed; done 
for i in {Pade,Palby,Pdav,Pdel,Peup,Pkor,Plas,Ppse,Pqio,Prot,Psim,Psze,Ptre,Pwua,Pyun}; do bedtools merge -i /usr_storage/stt/syri/Ref_Ptri/$i/dup_g.bed > /usr_storage/stt/syri/Ref_Ptri/$i/dup_g_m.bed; done 
for i in {Pade,Palby,Pdav,Pdel,Peup,Pkor,Plas,Ppse,Pqio,Prot,Psim,Psze,Ptre,Pwua,Pyun}; do bedtools merge -i /usr_storage/stt/syri/Ref_Ptri/$i/dup_l.bed > /usr_storage/stt/syri/Ref_Ptri/$i/dup_l_m.bed; done 

cat /usr_storage/stt/syri/Ref_Ptri/*/insertion_m.bed > all_ins.bed
cat /usr_storage/stt/syri/Ref_Ptri/*/deletion_m.bed > all_del.bed
cat /usr_storage/stt/syri/Ref_Ptri/*/inversion_m.bed > all_inv.bed
cat /usr_storage/stt/syri/Ref_Ptri/*/translocation_m.bed > all_transd.bed
cat /usr_storage/stt/syri/Ref_Ptri/*/dup_g_m.bed > all_dupg.bed
cat /usr_storage/stt/syri/Ref_Ptri/*/dup_l_m.bed > all_dupl.bed

cat all_ins.bed all_del.bed all_inv.bed all_transd.bed all_dupg.bed all_dupl.bed > all_sv.bed
sort -k1,1 -k2,2n -k3,3n all_sv.bed > all_sv.sort.bed

bedtools makewindows -g Ptri_genome.bed -w 200000 -s 100000> Ptri_genome_200k_s100k.bed
bedtools coverage -a Ptri_genome_200k_s100k.bed -b all_sv.sort.bed > Ptri_genome_200k_s100k_sv.cov
sort -k 4 Ptri_genome_200k_s100k_sv.cov > Ptri_genome_200k_s100k_sv.sort.covs