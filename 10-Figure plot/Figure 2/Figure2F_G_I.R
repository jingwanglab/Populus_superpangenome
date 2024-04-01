library(ggplot2)
library(ggsignif)

#Figure 2F
dt = read.table('Pkor_pangene.fst',sep='\t',header=T)
dt$pan = factor(dt$pan,levels = c('core','softcore','dispensable','private'))

my_comp = list(c('core','private'),c('softcore','private'),c('dispensable','private'))
p = ggplot(dt, aes(pan,fst,fill=pan))+
  geom_boxplot()+
  geom_signif(comparisons = my_comp,
              map_signif_level = TRUE,
               y_position = c(0.13,0.15,0.17))+
  theme_bw()+
  ylim(0,0.18)

ggsave(a, filename="Pkor_pangene_fst.pdf", width = 6,height = 6,units="cm",colormodel="srgb")


#Figure 2G
type = c('climate','struture','geography','confounded')
pev = c(0.29, 0.09,0.05,0.57)
d1 = data.frame(pev,type)
d1$pan='core'

pev = c(0.23, 0.09,0.04,0.64)
d2 = data.frame(pev,type)
d2$pan='softcore'

pev = c(0.26, 0.08,0.06,0.6)
d3 = data.frame(pev,type)
d3$pan='dispensable'

pev = c(0.49, 0.1,0.07,0.34)
d4 = data.frame(pev,type)
d4$pan='private'

dt = rbind(d1,d2,d3,d4)
dt$type = factor(dt$type, levels=c('confounded','geography','struture','climate'))
dt$pan =factor(dt$pan, levels=c('core','softcore','dispensable','private'))
p = ggplot(dt, aes(pan,pev,fill=type))+
  geom_col(position = 'stack',width=.5)+
  theme_bw()

ggsave(p, filename="Pkor_pangene_climate.pdf", width=6, height=6, units=c("cm"),colormodel="srgb")


#Figure 2I
data = read.csv('Pkor23334_env_altfreq.csv')

p <-  ggplot(data,aes(env,alt_freq))+
  geom_point(size=2)+
  scale_color_manual(values=c("#ff3333","#ff3333"))+
  geom_smooth(formula = y ~ x, method = "lm",se=F,level=0.95,color="black",size=0.7,fullrange = F)+
  geom_ribbon(stat = "smooth",
              method = "lm",
              se = TRUE,
              size=0.5,
              alpha = 0, # or, use fill = NA
              colour = "black",
              linetype = "dashed")+
  xlab("BIO13")+ylab("Allele frequency")+
  scale_y_continuous(limits = c(0,1),breaks=seq(0,1,0.25))+
  stat_cor(method = "pearson",aes(env,alt_freq,label = paste(..rr.label.., ..p.label.., sep = "~`,`~")),color='black',size = 6)+
  theme_bw()+
  theme(
    text=element_text(family="serif"),
    axis.text.x=element_text(angle=0,hjust=1,vjust=0.5,size=9,family="serif",colour = "black"),
    axis.text.y=element_text(size=9,family="serif",colour = "black"), 
    axis.title.y = element_text(size = 10,family="serif",colour="black"),
    legend.key.size=unit(0.3,'inch'),
    legend.position = "none",
    axis.title.x = element_text(size = 10,family="serif"),
    panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
    plot.margin=unit(c(0.5,0.5,0.5,0.5),"mm"))

ggsave(p, filename="Pkor23334_env_altfreq_cor.pdf", width=6, height=6, units=c("cm"),colormodel="srgb")
