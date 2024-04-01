
#####Ks correct
data=read.csv('F:/work/Populus_pangenome/Dup_gene/all_spe_wgd1to1.csv')
data=subset(data, ks != "NA")
data =subset(data, ks<=3)

densFindPeak <- function(x){
  td <- density(x)
  maxDens <- which.max(td$y)
  list(x=td$x[maxDens])
}


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

pade_peak = as.numeric(unlist(densFindPeak(as.vector(pade$ks))))
pdav_peak = as.numeric(unlist(densFindPeak(as.vector(pdav$ks))))
Palby_peak = as.numeric(unlist(densFindPeak(as.vector(Palby$ks))))
Peup_peak = as.numeric(unlist(densFindPeak(as.vector(Peup$ks))))
Pkor_peak = as.numeric(unlist(densFindPeak(as.vector(Pkor$ks))))
Plas_peak = as.numeric(unlist(densFindPeak(as.vector(Plas$ks))))
Ppse_peak = as.numeric(unlist(densFindPeak(as.vector(Ppse$ks))))
Prot_peak = as.numeric(unlist(densFindPeak(as.vector(Prot$ks))))
Psim_peak = as.numeric(unlist(densFindPeak(as.vector(Psim$ks))))
Psze_peak = as.numeric(unlist(densFindPeak(as.vector(Psze$ks))))
Pyun_peak = as.numeric(unlist(densFindPeak(as.vector(Pyun$ks))))
Pwua_peak = as.numeric(unlist(densFindPeak(as.vector(Pwua$ks))))
Pqio_peak = as.numeric(unlist(densFindPeak(as.vector(Pqio$ks))))
Pdel_peak = as.numeric(unlist(densFindPeak(as.vector(Pdel$ks))))
Ptre_peak = as.numeric(unlist(densFindPeak(as.vector(Ptre$ks))))
Ptri_peak = as.numeric(unlist(densFindPeak(as.vector(Ptri$ks))))


#Select the species with the smallest Ks peak value, that is, Ppse, to correct the Ks of other species.
pade$correct_ks= pade$ks * Ppse_peak/pade_peak
pdav$correct_ks= pdav$ks * Ppse_peak/pdav_peak
Palby$correct_ks= Palby$ks * Ppse_peak/Palby_peak
Peup$correct_ks= Peup$ks * Ppse_peak/Peup_peak
Pkor$correct_ks= Pkor$ks * Ppse_peak/Pkor_peak
Plas$correct_ks= Plas$ks * Ppse_peak/Plas_peak
Prot$correct_ks= Prot$ks * Ppse_peak/Prot_peak
Psim$correct_ks= Psim$ks * Ppse_peak/Psim_peak
Psze$correct_ks= Psze$ks * Ppse_peak/Psze_peak
Pwua$correct_ks= Pwua$ks * Ppse_peak/Pwua_peak
Pyun$correct_ks= Pyun$ks * Ppse_peak/Pyun_peak
Ppse$correct_ks= Ppse$ks 

Pqio$correct_ks= Pqio$ks * Ppse_peak/Pqio_peak
Ptre$correct_ks= Ptre$ks * Ppse_peak/Ptre_peak
Ptri$correct_ks= Ptri$ks * Ppse_peak/Ptri_peak
Pdel$correct_ks= Pdel$ks * Ppse_peak/Pdel_peak

r = rbind(pade,pdav,Palby,Peup,Pkor,Plas,Prot,Psim,Psze,Pyun,Pwua,Ppse,Pdel,Pqio,Ptre,Ptri)
write.csv(r,'F:/work/Populus_pangenome/Dup_gene/wgd/wgd1to1_correctKs.csv',row.names=FALSE)

