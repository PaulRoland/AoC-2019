# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()

f = open("input.txt", "r")
layers=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    data=re.findall('.'*25*6,line)
    
f.close()

score=0
min_zero=10**99
for layer in data:
    count_0=layer.count('0')
    if count_0<min_zero:
        min_zero=count_0
        score=layer.count('1')*layer.count('2')

image=''
for i in range(0,len(data[0])):
    if i%25==0:
        image+='\n'
    depth=0
    while data[depth][i]=='2':
        depth+=1
    image+=data[depth][i]
    

image=image.replace('1','\u2588').replace('0',' ')

print("Part 1",score)
print("Part 2",image)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))