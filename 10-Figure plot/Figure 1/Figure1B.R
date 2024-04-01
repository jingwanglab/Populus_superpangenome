library(ggplot2)
library(reshape2)

data = read.csv('genome_content.csv')

data_long = melt(data,
                 id.vars = c('species'),
                 measure.vars = c('gene_ratio','te_ratio','others'),
                 variable.name='type',
                 value.name='value')

data_long$type = factor(data_long$type, levels=c('others','te_ratio','gene_ratio'))
data_long$species = factor(data_long$species, levels=c("P. pseudoglauca","P. wuana", "P. szechuanica", "P. yunnanensis", "P. koreana", "P. trichocarpa",
                                                       "P. deltoides","P. simonii", "P. lasiocarpa","P. davidiana", "P. rotundifolia","P. tremula",
                                                       " P. alba","P. alba var. pyramidalis","P. qiongdaoensis","P. adenopoda","P. euphratica",
                                                       "P. pruinosa","P. ilicifolia","S. purpurea","S. suchowensis","S. brachista"))

p = ggplot(data_long, aes(x = '', y = value, fill = type))+
  geom_bar(stat ="identity",width = 0.6) +
  coord_polar(theta = "y") +
  labs(x = "", y = "", title = "") +
  theme(axis.ticks = element_blank(),
        legend.position = 'top') +
#  scale_fill_brewer(palette="Set2")+
  facet_wrap(~species, ncol=1) +
  scale_fill_manual(values=c("#41B3E2", "#F1786B", "#FBD984"))+
  theme_nothing()

ggsave(p, filename="genome_content.pdf", width=0.6, height=12, units=c("cm"),colormodel="srgb")
