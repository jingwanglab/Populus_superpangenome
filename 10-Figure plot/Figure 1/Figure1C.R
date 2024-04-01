
library(reshape2)
library(ggplot2)

data = read.csv('TE_stack.csv')

data_long = melt(newdata,
                id.vars = c('TE'),
                measure.vars = c("S.purpurea","S.suchowensis","S.brachista","P.euphratica", "P.ilicifolia","P.pruinosa", "P.qiongdaoensis", "P.adenopoda",
                                 "P.alba","P.alba.var.pyramidalis","P.tremula","P.rotundifolia","P.davidiana","P.lasiocarpa","P.pseudoglauca","P.yunnanensis",
                                 "P.wuana","P.simonii","P.deltoides","P.trichocarpa","P.koreana","P.szechuanica"),#用于聚合的变量,
                variable.name='Species',
                value.name='value')


data_long$TE = factor(data_long$TE, levels=c("unknown", "DNA-TEs", "non-LTR", "LTR/unknown", "LTR/Gypsy","LTR/Copia"))

p = ggplot(data_long, aes(x = Species, y = value, fill = TE))+
  geom_bar(stat ="identity",width = 0.6,position ="stack") +
  theme_classic()+
  theme(axis.text = element_text(size=9, vjust=0.5,colour = 'black',face='italic'),   #family="sans", face='italic',
        panel.border = element_blank(),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
#        legend.position = "top",
#        axis.line.x = "black",
#        axis.line.y = "black",        
#        axis.title.y=element_text(size=16),
        axis.title.x=element_text(size=13,colour = 'black'),
#        axis.ticks.y = element_blank())
        axis.ticks.x = element_blank())+
  scale_fill_manual(name='', 
                    labels=c("unknown", "DNA-TEs", "non-LTR", "LTR/unknown", "LTR/Gypsy","LTR/Copia"), 
                    values=c('#CD3700','#7CCD7C','#fffb00','#7bbae5','#007acc','#0433ff'))+ 
  scale_y_continuous(limits = c(0,50),expand = c(0,0),breaks=seq(0, 50, 10)) +
  ylab('Percent of assembly')+
  xlab('') +
  coord_flip()


ggsave(p, filename="TE_stack.pdf", width=15, height=11, units=c("cm"),colormodel="srgb")

