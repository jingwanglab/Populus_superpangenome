
library(dplyr)
library(data.table)
library(ggplot2)
library(forcats)
#install.packages("ggrepel")
library(ggrepel)

data = read.csv('all_SV.gene.GO.csv')
data = subset(data, Annotated<1000)
index = duplicated(data[,3])
df = data[!index,]
df$rich_factor = df$Significant/df$Annotated

p = ggplot(df,aes(rich_factor,-log10(as.numeric(adjust.p))))+
  geom_point(aes(size=Significant,color=-log10(as.numeric(adjust.p))))+
  # scale_color_distiller(palette = "Spectral")+
  # scale_color_gradient(low="red")+
  scale_color_gradient2(low = "#5abbd4", mid = "white", high = "red",midpoint = median(df$Significant))+
  theme_bw()+
  geom_text_repel(aes(rich_factor, -log10(as.numeric(adjust.p)), label =Term ),size=4)+
  theme(axis.text.x = element_text(size = 8 , color='black',face="bold"),
        axis.text.y = element_text(size = 8 , color='black',face="bold"),
        #  legend.position = 'none',
        panel.grid.major = element_line(size=0.1,colour = "#F4F2F3"),
        panel.grid.minor = element_line(size=0.1,colour = "#F4F2F3"),
        axis.title.x  = element_text( size= 9,color='black',face="bold" ))+
  labs(y="-Log10(P.value)",x="Rich factor",size="Gene number")  

ggsave("all_SV.gene.GO.pdf", width=10, height=8, units=c("cm"),colormodel="srgb")



