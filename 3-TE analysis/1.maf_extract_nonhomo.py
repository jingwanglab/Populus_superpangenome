# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:34:58 2022

@author: Stt
"""
import sys,getopt

def main(argv):
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            infile = arg
        elif opt in ("-o", "--ofile"):
            outfile = arg

    data = open(infile).readlines()
    data.append('\n')

    block=[]
    f=open(outfile,'w')
    for i,line in enumerate(data):
        if i%50000==0:
            print('process line:'+str(i))
        if len(line.strip('\n')) <3:
            if len(block)==1:
                ss = block[0].split('\t')
                ch = ss[1].split('.')[1]
                f.write(ch+'\t'+str(ss[2])+'\t'+str(ss[3])+'\t'+ss[4]+'\n')    
            block=[]        
            continue
        aa = line.strip('\n').split('\t')
        if aa[0]=='s':
            block.append(line)
    
    f.close()

if __name__ == "__main__":
   main(sys.argv[1:])
   