
library(ggplot2)
library(ggsignif)

#Figure 4H,I,K
data = read.csv('SVgene_compare.csv') 
data$type = factor(data$type, levels=c("SV-","SV+","Hemizygous"))
my_comparisons <- list(c("SV-","SV+"),c("SV+","Hemizygous"))

#Figure 4H
p1 = ggplot(data,aes(type,gene2te_distance,fill=type))+
  geom_boxplot(width=0.5) +#
  theme_bw()+
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        legend.title= element_blank(),
        legend.position = 'None',
        axis.text.x = element_text(color='black',size=9, hjust=1,angle=30),
        axis.text.y = element_text(color='black',size=9),
        axis.title.y = element_text(color='black',size=9)) +
  geom_signif(comparisons = my_comparisons,  y_position = c(1600,1250), map_signif_level = T) +
  scale_y_continuous(limits =c(0,2000), breaks = seq(0,2000,500))+
  xlab('')+ylab('Distance of gene to closest TE')

ggsave(p1,filename = "SVgene_compare_TE.pdf",width =6,height = 6,units=c("cm"),colormodel="srgb")

#Figure 4I
p2 = ggplot(data,aes(type,log2(FPKM+1),fill=type))+
  geom_boxplot(width=0.5) +#
  theme_bw()+
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        legend.title= element_blank(),
        legend.position = 'None',
        axis.text.x = element_text(color='black',size=9, hjust=1,angle=30),
        axis.text.y = element_text(color='black',size=9),
        axis.title.y = element_text(color='black',size=9)) +
  geom_signif(comparisons = my_comparisons,  y_position = c(9,6), map_signif_level = T) +
  scale_y_continuous(limits =c(0,12), breaks = seq(0,12,3))+
  xlab('')+ylab('Log2(FPKM+1)')

ggsave(p2,filename = "SVgene_compare_fpkm.pdf",width =6,height = 6,units=c("cm"),colormodel="srgb")

#Figure 4k
data$absdistance = abs(data$peak2gene_distance)/1000
p3 =ggplot(data, aes(absdistance+0.001, color=type))+ 
  geom_density(size=1)+
  theme_bw() +  
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        legend.title = element_blank()) +
  scale_x_log10( breaks=c(0.001,0.1,1,10,100,1000),labels=c(0,0.1,1,10,100,1000)) + 
  xlab('Distance between ACR and nearest gene (kb)')+ylab('Relative density')

ggsave(p3,filename = "SVgene_compare_ACR.pdf",width = 9.5,height = 6.5,units="cm",colormodel="srgb")


#Figure 4J
data = read.csv('SVgene_compare_CG.csv')
data$type <- factor(data$type, levels = c("SV-","SV+","Hemizygous"))

a = ggplot(data, aes(x=plot_bin, y = methy, color=type)) +
  geom_line(size=1)+
  theme_bw()+
  theme(axis.text = element_text(color='black',size=9),
        legend.title = element_blank(),
        legend.text = element_text(size =8),
        legend.key.size = unit(0.5, "cm"))  +
  scale_x_continuous(limits = c(0,90),breaks=c(1.5, 30, 60,90),labels = c('-2kb', 'TSS','TES','+2kb')) +
  xlab('')+ylab('mCpG level (%)')

ggsave(a, filename="SVgene_compare_CG.pdf", width = 6,height = 6,units="cm",colormodel="srgb")


