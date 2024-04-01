
library(ggplot2)

data = read.csv('pan_core.csv')

data$type <- factor(data$type, levels = c('pan','core'))
core = subset(data, type=='core')
pan = subset(data, type=='pan')

data_median = read.csv('pan_core_median.csv')
data_median$accession_num<- as.factor(data_median$accession_num)

p_compare  <- ggplot(data_median, aes(x = accession_num, y = gene_num))
p_compare  <- p_compare  + 
  stat_boxplot(data = core,geom ="errorbar",width=0.5,aes(group = accession_num))+
  stat_boxplot(data = pan,geom ="errorbar",width=0.5,aes(group = accession_num))+
  geom_boxplot(data = core, aes(group = accession_num), outlier.shape = NA) +
  geom_boxplot(data = pan, aes(group = accession_num), outlier.shape = NA) +
  geom_point(aes( color = type), size = 1) +
  geom_line(aes(color = type))+
  theme_classic()+
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        legend.title=element_blank(),
        axis.title.x = element_text(size=9,color='black'),
        axis.text = element_text(size=9,color='black'))+
  scale_y_continuous(limits = c(18000,83200),breaks = seq(20000,80000,15000))+
  scale_x_continuous(limits = c(1,19),breaks = seq(1,19,1))+
  ylab("Gene number") + xlab('Genome number')

ggsave(a, filename="pan_core.pdf", width=10,height=6, units=c("cm"))

