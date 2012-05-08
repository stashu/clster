# proof of concept for ls clustering

import os
from mlpy import kmeans
from math import log

dir = '/Users/sbaehr/Downloads'
dinfo = []
dirlist = os.listdir(dir)

for file in dirlist:
    
    mypath = dir + '/' + file
    info = os.stat(mypath)
    
    # don't deal with directories yet
    if info.st_size > 0:
        finfo = [file,float(info.st_size)/1024,info.st_mtime,info.st_mode]
        dinfo += [finfo]
    
# cluster by size
infos = [[log(x[1])] for x in dinfo]

cls,means,steps = kmeans(infos,k=10,plus=True)

ctmp = -1
data = zip([x[0] for x in dinfo],cls,infos)
for f,c,s in sorted(data,key=lambda tempkey: tempkey[2]):
    
    if c != ctmp:
        print '###############################'
        
    print c,'\t',round(s[0],1),'\t\t',f
        
    ctmp = c





