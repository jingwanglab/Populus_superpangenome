iqtree -t species.astral.tre --gcf all_gene.treefile -s supergene_pep_coden.phy --scf 100 --prefix iqtree_concord -T 20
java -jar astral.5.7.8 -q species.astral.tre -i all_gene.treefile -t 1 -o species.astral_t1.tre
