library(ggplot2)
library(ggsignif)

#Figure 3F
data = read.csv('wgd1to1_equal_4type_gene_compare.csv')
data$type = factor(data$type, levels = c('con_L','con_H','div_L','div_H'))

p1 = ggplot(data,aes(type,log2(fpkm+1),fill=type))+
  geom_boxplot(width=0.5,size=0.3,outlier.color = NA )+
  theme_classic()+
  geom_signif(comparisons = list(c("con_L", "con_H"),c("div_L", "div_H"),c("con_L", "div_L"),c("con_H", "div_H")),
              map_signif_level=TRUE)+  
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        legend.title= element_blank(),
        legend.position = 'none',
        axis.text.x = element_text(color='black',size=9,hjust = 1),
        axis.text.y = element_text(color='black',size=9)) +
  ylim(0,10)+
  xlab('')+ylab('Log2(FPKM+1)')

ggsave(p1,filename = "wgd1to1_equal_4type_gene_compare_fpkm.pdf",width=6, height=6, units=c("cm"),colormodel="srgb")

#Figure 3G
data = read.csv('wgd1to1_equal_4type_gene_compare_CG.csv')
data$type = factor(data$type, levels = c('con_L','con_H','div_L','div_H'))

a = ggplot(data, aes(x=plot_bin, y = methy, color=type)) +
  geom_line(size=1)+
  scale_fill_brewer(palette="Set2")+
  theme_bw()+
  theme(axis.text = element_text(color='black',size=9),
        legend.title = element_blank(),
        legend.text = element_text(size =8),
        legend.key.size = unit(0.5, "cm"))  +
  scale_x_continuous(limits = c(0,90),breaks=c(1.5, 30, 60,90),labels = c('-2kb', 'TSS','TES','+2kb')) +
  xlab('')+ylab('mCpG level (%)')

ggsave(a, filename="wgd1to1_equal_4type_gene_compare_CG.pdf", width = 6,height = 6,units="cm",colormodel="srgb")
