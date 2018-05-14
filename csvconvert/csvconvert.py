import os
import re

map = {'1':'Negative','2':'Positive'}
filename=r'C:\Users\TLCrow\Desktop\1\list.txt'
file = open(filename,'r')
list=[]
for line in file.readlines():
    tmp = line.split(',')
    kfb = tmp[0].strip('\n')
    kfb = os.path.basename(kfb)
#    db=re.sub('kfb','db',kfb)
    db=kfb.replace('kfb','db')
    label = tmp[1].strip('\n')
    list.append(kfb+':0|'+map[label]+'|'+db)
    print(kfb+':0|'+map[label]+'|'+db)
outpath='data.list'
with open(outpath,'w') as f:
    for lis in list:
        f.writelines(lis+'\n')