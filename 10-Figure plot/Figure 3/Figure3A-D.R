library(ggplot2)
library(RColorBrewer)

#Figure 3A
library(ggradar)
data = read.csv('wgd1to1_ks_pan.ratio',sep='\t')

data$ks_class = factor(data$ks_class, levels=c('L','M','H'))
data$pan_type = factor(data$pan_type, levels=c('core','softcore','dispensable','private'))
df_wide<-dcast(data,ks_class~data$pan_type,value.var = 'ratio')
a = ggradar(df_wide, grid.line.width =0.5,axis.label.size=5,group.line.width =1,group.point.size =2)
ggsave(a, filename="wgd1to1_ks_pan.ratio.pdf", width=10, height=10, units=c("cm"),colormodel="srgb")


#Figure 3B,C
library(ggplot2)
library(reshape2)
data = read.csv('wgd1to1_divergence.csv')

data$ks_class = factor(data$ks_class, levels=c('L','M','H'))
data$pan = factor(data$pan, levels=c('same','different'))
#Figure 3B
a = ggplot(data, aes(ks_class, abs(divergence_fpkm), fill=pan))+
  geom_boxplot(width=0.5,outlier.color = NA)+
  theme_bw()+
  theme(
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    axis.text.x = element_text(color='black',size=9),
    axis.text.y = element_text(color='black',size=9))+
  facet_wrap(~spe)+
  xlab('')+ylab('FPKM divergence')
ggsave(a, filename="wgd1to1_divergence_fpkm.pdf", width=8, height=6, units=c("cm"),colormodel="srgb")


#Figure 3C
library(ggsignif)

a = ggplot(data, aes(x=ks_class,y=abs(divergence_CpG_body),fill=pan))+
  geom_boxplot(width=0.5,outlier.colour = NA) +
#  scale_fill_brewer(palette="Set3")+
  theme_bw()+
  theme(
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank(),
    axis.text.x = element_text(color='black',size=9),
    axis.text.y = element_text(color='black',size=9))+
  xlab('')+
  #geom_signif(comparisons = list(c('same','different')),map_signif_level = F,test = wilcox.test)+
  ylab('mCpG divergence (gene body)')
ggsave(a, filename="wgd1to1_divergence_CGbody.pdf", width=8, height=6, units=c("cm"),colormodel="srgb")


#Figure 3D
library(tidyverse)
library(dplyr)
library(reshape2)

data = read.csv('wgd1to1_divergence.csv')

df = data[,c('pan','divergence_CpG_body','divergence_fpkm')]

df$abs_divergence_CpG_body = abs(df$divergence_CpG_body)
df$abs_divergence_fpkm = abs(df$divergence_fpkm)

df=subset(df, abs_divergence_fpkm != "NA")
df=subset(df, abs_divergence_CpG_body != "NA")

df=df %>% mutate(fpkm_quantile=ntile(abs_divergence_fpkm,15))

ratio_mean=as.vector(by(df$abs_divergence_CHH_down, df$fpkm_quantile, function(x) mean(x,na.rm=T)))
ratio_sd=as.vector(by(df$abs_divergence_CHH_down, df$fpkm_quantile, function(x) 1.96*(sd(x,na.rm=T)/sqrt(length(x)))))
ratio_p25=as.vector(by(df$abs_divergence_CHH_down, df$fpkm_quantile, function(x) quantile(x, 0.25)))
ratio_p50=as.vector(by(df$abs_divergence_CHH_down, df$fpkm_quantile, function(x) quantile(x, 0.5)))
ratio_p75=as.vector(by(df$abs_divergence_CHH_down, df$fpkm_quantile, function(x) quantile(x, 0.75)))

stats=data.frame(cbind(fpkm_quantile=1:15,mean=ratio_mean,sd=ratio_sd, p25=ratio_p25,p50=ratio_p50,p75=ratio_p75))
cor.test(stats$fpkm_quantile, stats$mean,method="pearson")

p = ggplot(stats,aes(as.factor(fpkm_quantile),y=mean,ymin=mean-sd,ymax=mean+sd))+
  geom_pointrange(size=0.1)+
  geom_smooth(aes(y=mean,x=fpkm_quantile),method = 'lm', se = FALSE,col='red',size=0.75)+
  theme_classic()+
  theme(
    #panel.grid.major = element_blank(),
    #panel.grid.minor = element_blank(),
    legend.position  = "None",
    axis.text.x = element_blank(),
    axis.text.y = element_text(color='black',size=9),
    axis.ticks.x =element_blank()) +
  ylab('CG Methylat divergence')+
  xlab('Expression divergence')

ggsave(p, filename="wgd1to1_divergence_fpkm_CGbody_cor.pdf", width=5.4, height=3.3, units=c("cm"),colormodel="srgb")
