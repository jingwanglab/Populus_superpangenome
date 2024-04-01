library(ggplot2)

#Figure 5B
data = read.csv('inv_syn_diversity.csv')
data$type <- factor(data$type, levels = c('clade1', 'clade2', 'inter-clade'))

a = ggplot(data, aes(x=win, y = div, color=type)) +
  geom_line(size=1)+
  theme_bw()+
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        axis.text = element_text(color='black',size=9),
        legend.title = element_blank(),
        legend.text = element_text(size =8),
        legend.key.size = unit(0.5, "cm"))  +
  scale_y_continuous(limits = c(0,1),breaks=seq(0,1,0.25)) +
  xlab('')+ylab('Synteny diversity')

ggsave(a, filename="inv_syn_div.pdf", width = 9, height = 6,units="cm",colormodel="srgb")


#Figure 5C
data = read.csv('cuc2_seq_div.csv')
data$type <- factor(data$type, levels = c('clade1', 'clade2', 'inter-clade'))

a = ggplot(data, aes(x=plot_bin, y = div, color=type)) +
  geom_line(size=1)+
  theme_bw()+
  theme(panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        axis.text = element_text(color='black',size=9),
        legend.title = element_blank(),
        legend.text = element_text(size =8),
        legend.key.size = unit(0.5, "cm"))  +
  scale_x_continuous(limits = c(0,40),breaks=c(1, 20, 40),labels = c('-2kbp', 'TSS','TES')) +
  xlab('')+ylab('Sequence divergence')

ggsave(a, filename="cuc2_seq_div.pdf", width = 9, height = 6,units="cm",colormodel="srgb")


