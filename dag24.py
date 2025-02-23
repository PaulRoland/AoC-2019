# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
bugs=set()
for row,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    for col,s in enumerate(line):
        if s=='#':
            bugs.add('0,'+str(row)+','+str(col))
f.close()

start_bugs=set(bugs)
scores=list()
while True:
    new_bugs=set()
    dirs=[[-1,0],[0,1],[1,0],[0,-1]]
    
    score=0
    for r in range(0,5):
        for c in range(0,5):
            nbrs=0
            for dr,dc in dirs:
                key='0,'+str(r+dr)+','+str(c+dc)
                if key in bugs:
                    nbrs+=1
            
            key='0,'+str(r)+','+str(c)
            if key in bugs:
                if nbrs==1:
                    new_bugs.add(key)
                    score+=2**(r*5+c)
            else:
                if nbrs==1 or nbrs==2:
                    new_bugs.add(key)
                    score+=2**(r*5+c)
    if score in scores:
        break
    scores.append(score)               
    bugs=set(new_bugs)
    

##Part 2
bugs=start_bugs

for i in range(0,200):
    nbrs=dict()
    for key in bugs:
        lvl,r,c=[int(d) for d in key.split(',')]
        #Standaard buren
        nbrs_list=[[lvl,r-1,c],[lvl,r,c+1],[lvl,r+1,c],[lvl,r,c-1]]

        #Nieuwe buren op andere levels
        if r==0:
            nbrs_list.remove([lvl,r-1,c])
            nbrs_list.append([lvl-1,1,2])
        elif r==4:
            nbrs_list.remove([lvl,r+1,c])
            nbrs_list.append([lvl-1,3,2])
            
        if c==0:
            nbrs_list.remove([lvl,r,c-1])
            nbrs_list.append([lvl-1,2,1])
        elif c==4:
            nbrs_list.remove([lvl,r,c+1])
            nbrs_list.append([lvl-1,2,3])    

        if r==1 and c==2:
            nbrs_list.remove([lvl,r+1,c])
            nbrs_list.append([lvl+1,0,0])
            nbrs_list.append([lvl+1,0,1])
            nbrs_list.append([lvl+1,0,2])
            nbrs_list.append([lvl+1,0,3])
            nbrs_list.append([lvl+1,0,4])
        if r==3 and c==2:
            nbrs_list.remove([lvl,r-1,c])
            nbrs_list.append([lvl+1,4,0])
            nbrs_list.append([lvl+1,4,1])
            nbrs_list.append([lvl+1,4,2])
            nbrs_list.append([lvl+1,4,3])
            nbrs_list.append([lvl+1,4,4])
        
        if r==2 and c==1:
            nbrs_list.remove([lvl,r,c+1])
            nbrs_list.append([lvl+1,0,0])
            nbrs_list.append([lvl+1,1,0])
            nbrs_list.append([lvl+1,2,0])
            nbrs_list.append([lvl+1,3,0])
            nbrs_list.append([lvl+1,4,0])            

        if r==2 and c==3:
            nbrs_list.remove([lvl,r,c-1])
            nbrs_list.append([lvl+1,0,4])
            nbrs_list.append([lvl+1,1,4])
            nbrs_list.append([lvl+1,2,4])
            nbrs_list.append([lvl+1,3,4])
            nbrs_list.append([lvl+1,4,4])
        
        for nbr in nbrs_list:
            nbr_key=str(nbr[0])+','+str(nbr[1])+','+str(nbr[2])
            if nbr_key in nbrs:
                nbrs[nbr_key]+=1
            else:
                nbrs[nbr_key]=1
    
    new_bugs=set()
    for nbr in nbrs:
        if nbr in bugs and nbrs[nbr]==1:
            new_bugs.add(nbr)
            
        elif nbr not in bugs and (nbrs[nbr]==1 or nbrs[nbr]==2):
            new_bugs.add(nbr)
    bugs=new_bugs

print("Part 1",score)
print("Part 2",len(bugs))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))