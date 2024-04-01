
library(ggplot2)
library(ggsignif)

#Figure 2C,E
data = read.csv('pangene_compare.csv') 
data$pan_type = factor(data$pan_type, levels=c('core',"softcore","dispensable","private"))

#Figure 2C
my_comparisons <- list(c("core","softcore"), c("core", "dispensable"),c("core", "private"))
p = ggplot(data,aes(pan_type,log2(FPKM+1),fill=pan_type))+
 # ggplot(data,aes(pan_type,tau,fill=pan_type))+
  geom_boxplot(width=0.5, outlier.color = NA) +#
  theme_bw()+
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        legend.title= element_blank(),
        legend.position = 'None',
        axis.text.x = element_text(color='black',size=9, hjust=1,angle=45),
        axis.text.y = element_text(color='black',size=9),
        axis.title.y = element_text(color='black',size=9)) +
    geom_signif(comparisons = my_comparisons,  y_position = c(9,10.5,12), map_signif_level = T) +
  scale_y_continuous(limits =c(0,13), breaks = seq(0,10,2.5))+
  scale_fill_manual(values = c('#CE514D', '#F5A861','#7BC27A','#7AB3DA')) +
  xlab('')+ylab('Log2(FPKM+1)')

ggsave(p,filename = "pangene_compare_fpkm.pdf",width =6,height = 6,units=c("cm"),colormodel="srgb")

#Figure 2E
data$absdistance = abs(data$peak2gene_distance)/1000
p2 =ggplot(data, aes(absdistance+0.001, color=pan_type))+ 
  geom_density(size=1)+
  theme_bw() +  
  theme(legend.position = 'None',
        legend.title = element_blank())+
  scale_x_log10( breaks=c(0.001,0.1,1,10,100,1000),labels=c(0,0.1,1,10,100,1000)) + 
  xlab('Distance between ACR and nearest gene (kb)')+ylab('Relative density')

ggsave(p2,filename = "pangene_compare_ACR.pdf",width = 9.5,height = 6.5,units="cm",colormodel="srgb")


#Figure 2D
data = read.csv('pangene_compare_CG.csv')
data$pan_type <- factor(data$pan_type, levels = c('core', 'softcore', 'dispensable', 'private'))

a = ggplot(data, aes(x=plot_bin, y = methy, color=pan_type)) +
  geom_line(size=1)+
  scale_fill_brewer(palette="Set2")+
  theme_bw()+
  theme(axis.text = element_text(color='black',size=9),
        legend.title = element_blank(),
        legend.text = element_text(size =8),
        legend.key.size = unit(0.5, "cm"))  +
  #  scale_y_continuous(limits = c(0,50),expand = c(0,0),breaks=seq(0,50,10)) +
  scale_x_continuous(limits = c(0,90),breaks=c(1.5, 30, 60,90),labels = c('-2kb', 'TSS','TES','+2kb')) +
  xlab('')+ylab('mCpG level (%)')

ggsave(a, filename="pangene_compare_CG.pdf", width = 6,height = 6,units="cm",colormodel="srgb")


