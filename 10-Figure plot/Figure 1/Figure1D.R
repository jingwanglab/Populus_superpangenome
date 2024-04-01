library(ggplot2)
library(ggpubr)


data = read.csv('genome_region_TE.overlap',sep='\t')
mean(data$homo_TE_proportion)
mean(data$nonhomo_TE_proportion)

type = c('te','other')
homo =c(0.32,0.68)
no_homo =c(0.77,0.23)
df1 = data.frame(type,homo)
df2 = data.frame(type,no_homo)

p1 = ggplot(data = df1, mapping = aes(x = 'Content', y = df1, fill = type)) + 
  geom_bar(stat = 'identity', position = 'stack')+
  coord_polar(theta = 'y')+
  theme(axis.text = element_blank())

p2 = ggplot(data = df2, mapping = aes(x = 'Content', y = df2, fill = type)) + 
  geom_bar(stat = 'identity', position = 'stack')+
  coord_polar(theta = 'y')+
  theme(axis.text = element_blank())

ggsave(p1, filename="genome_region_TE.shared.pdf", width=8, height=8, units=c("cm"),colormodel="srgb")
ggsave(p2, filename="genome_region_TE.specific.pdf", width=8, height=8, units=c("cm"),colormodel="srgb")


### homo/non-homo LTR age
data = read.csv('all_LTRage.csv')
data$type = factor(data$type, levels=c('shared','specific'))

p = ggplot(data, aes(type, Insertion_time,fill=type))+
  geom_boxplot(outlier.colour = NA,width=0.6)+
  theme_bw()+
  theme(
    panel.grid = element_blank(),
    axis.text= element_text(color='black',size=9),
    legend.position = 'none')+
  geom_signif(comparisons = list(c('shared','specific')),  y_position = c(13), map_signif_level = T,tip_length = c(0))+
  xlab('')+ylab('')+
  ylim(0,15)+
  facet_grid(spe~.) +
  coord_flip()


ggsave(p, filename="all_LTRage.pdf", width=7, height=7, units=c("cm"),colormodel="srgb")

  