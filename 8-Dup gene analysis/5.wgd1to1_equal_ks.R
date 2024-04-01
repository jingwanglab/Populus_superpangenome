
##########################抽样1000次计算peak平均值,返回peak平均值置信区间内的数据
data=read.csv('F:/work/Populus_pangenome/Dup_gene/wgd/wgd1to1_correctKs.csv')
pade = subset(data,spe=='Pade')
pdav = subset(data,spe=='Pdav')
Palby = subset(data,spe=='Palby')
Peup = subset(data,spe=='Peup')
Pkor = subset(data,spe=='Pkor')
Plas = subset(data,spe=='Plas')
Ppse = subset(data,spe=='Ppse')
Prot = subset(data,spe=='Prot')
Psim = subset(data,spe=='Psim')
Psze = subset(data,spe=='Psze')
Pwua = subset(data,spe=='Pwua')
Pyun = subset(data,spe=='Pyun')
Pqio = subset(data,spe=='Pqio')
Pdel = subset(data,spe=='Pdel')
Ptre = subset(data,spe=='Ptre')
Ptri = subset(data,spe=='Ptri')

sample_mean_sd <- function(x){
  m <- vector("numeric")
  for (j in 1:1000) {
  sample = sample(as.vector(x$correct_ks),length(x$correct_ks)*0.6)
  peak = densFindPeak(sample)
  a = as.numeric((unlist(peak)))
  m <- append(m, a)
  }
  peak_mean = mean(m)
  peak_sd=sd(m)
  peak_min=peak_mean-2*peak_sd
  peak_max=peak_mean+2*peak_sd
  x2 = subset(x, correct_ks >=peak_min & correct_ks<=peak_max)
  return (x2)
}
pade_sample = sample_mean_sd(pade)
pdav_sample = sample_mean_sd(pdav)
palby_sample = sample_mean_sd(Palby)
peup_sample = sample_mean_sd(Peup)
plas_sample = sample_mean_sd(Plas)
prot_sample = sample_mean_sd(Prot)
pkor_sample = sample_mean_sd(Pkor)
psim_sample = sample_mean_sd(Psim)
psze_sample = sample_mean_sd(Psze)
pwua_sample = sample_mean_sd(Pwua)
pyun_sample = sample_mean_sd(Pyun)
ppse_sample = sample_mean_sd(Ppse)
pqio_sample = sample_mean_sd(Pqio)
ptre_sample = sample_mean_sd(Ptre)
ptri_sample = sample_mean_sd(Ptri)
pdel_sample = sample_mean_sd(Pdel)


r_sample = rbind(pade_sample,pdav_sample,palby_sample,peup_sample,pkor_sample,plas_sample,prot_sample,psim_sample,psze_sample,
                 pyun_sample,pwua_sample,ppse_sample,pqio_sample,ptre_sample,ptri_sample,ppru_sample,pdel_sample)

write.csv(r_sample,'F:/work/Populus_pangenome/Dup_gene/wgd/wgd1to1_equal_Ks.csv',row.names = FALSE)
