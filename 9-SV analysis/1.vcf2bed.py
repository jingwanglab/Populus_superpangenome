# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 22:18:00 2024

@author: Stt
"""

import pandas as pd
import re

vcf_path=''
out_path=''
vcf  = pd.read_csv(vcf_path,sep='\t',header=None)
vcf['end'] = vcf.apply(lambda x: re.findall(r'END=(.*?);', x[7])[0], axis=1)
vcf = vcf[[0,1,'end']]
vcf['start'] = vcf.apply(lambda x: int(x[1]) if int(x[1]) < int(x['end']) else int(x['end']), axis=1)
vcf['end'] = vcf.apply(lambda x: int(x['end']) if int(x[1]) < int(x['end']) else int(x[1]), axis=1)
vcf = vcf[[0,'start','end']]
vcf.sort_values([0,'start'],inplace=True)
vcf.to_csv(out_path)