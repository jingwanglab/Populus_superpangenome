#install.packages("ggalluvial")
library(ggplot2)
library(ggalluvial)

dt = read.csv('pan_dup.stats.csv')
dt$pan_type = factor(dt$pan_type,levels = c('core','softcore','dispensable','private'))
dt$dup_type = factor(dt$dup_type,levels = c('WGD','TD', 'PD','TRD','DSD', 'Singleton' ))

p = ggplot(dt,
       aes(axis1 = pan_type, axis2 = dup_type, y= count)) +
  scale_x_discrete(limits = c("pan", "dup" ), expand = c(.0, .0)) +
  geom_alluvium(aes(fill = pan_type)) +
  geom_stratum(width=1/4) + geom_text(stat = "stratum", label.strata = TRUE) +
  theme_minimal()

ggsave(p,filename="F:/work/Populus_pangenome/Dup_gen/wgd_pan.states1.pdf", width=15, height=10, units=c("cm"),colormodel="srgb")
