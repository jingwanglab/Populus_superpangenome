library(ggplot2)

data = read.csv('pan_fam_stats.csv')
data$type = factor(data$type, levels = c("core", "softcore", "dispensable", "private"))

p = ggplot(data, aes(factor(species_num), family_num,fill=type)) +
  geom_bar(stat='identity',width=0.75)+
  scale_fill_manual(values = c('#CE514D', '#F5A861','#7BC27A','#7AB3DA'))+ 
  theme_classic() +
  theme(
    legend.title=element_blank(),
    legend.position = 'None',
  axis.title.x = element_text(size=11,color='black'),
  axis.text = element_text(size=9, color='black')
  )+
  scale_y_continuous(expand = c(0,0)) +
  geom_hline(aes(yintercept=334 ), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=701), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=1122), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=1555), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=2029), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=2536), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=3099), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=3761), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=4448), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=5199), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=6034), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=7326), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=8642), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=10007), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=12111), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=14387), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=16726), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=19103), colour="darkgrey", linetype="dashed",size=0.3) +
  geom_hline(aes(yintercept=22391), colour="darkgrey", linetype="dashed",size=0.3) +
  xlab('Frequency')+
  ylab('Family number')

ggsave(p,filename="pan_fam.pdf", width=10.5, height=6, units=c("cm"),colormodel="srgb")



a = data.frame(type =c('core','softcore','dispensable','private'), value= c(51.11,22.78,22.50,3.61))
a$type = factor(a$type, levels = c('private','dispensable','softcore','core'))

p2 = ggplot(a, aes(x = '', y = value, fill = type))+
  geom_bar(stat ="identity",width = 0.6, alpha=0.8) +
  coord_polar(theta = "y") +
  labs(x = "", y = "", title = "") +
  theme(axis.ticks = element_blank(),
        legend.position = 'top') +
  scale_fill_manual(values = c('#7AB3DA','#7BC27A','#F5A861','#CE514D'))+ 
  theme_nothing()
ggsave(p2, filename="pan_pie.pdf", width=4, height=4, units=c("cm"),colormodel="srgb")
