# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
data=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    data.append(list(line))
    print(line)
f.close()

warps=dict()

for r,line in enumerate(data[:-1]):
    if r==0: continue

    for c,s in enumerate(line[:-1]):
        if s.isupper() and data[r-1][c].isupper() and data[r+1][c]=='.':
            key=data[r-1][c]+s
            [nr,nc]=[r+1,c]
        elif s.isupper() and data[r+1][c].isupper() and data[r-1][c]=='.':
            key=s+data[r+1][c]
            [nr,nc]=[r-1,c]
        elif s.isupper() and data[r][c-1].isupper() and data[r][c+1]=='.':
            key=data[r][c-1]+s
            [nr,nc]=[r,c+1]
        elif s.isupper() and data[r][c+1].isupper() and data[r][c-1]=='.':
            key=s+data[r][c+1]
            [nr,nc]=[r,c-1]
        else:
            continue
        
        data[r][c]=key
        if key in warps:
            warps[key].append([nr,nc])
        else:
            warps[key]=[[nr,nc]]

sr,sc=warps['AA'][0]
er,ec=warps['ZZ'][0]
print(sr,sc,er,ec)

directions=[[-1,0],[0,1],[1,0],[0,-1]]
min_dist=[[99999 for c in data[0]] for r in data]

heap=[[sr,sc,0]]
i=0
while i<len(heap):
    r,c,l=heap[i]
    i+=1
    #Eindpunt
    if r==er and c==ec:
        continue
    
    #Niet meer de kortste optie in de hele heap
    if l>min_dist[r][c]:
        continue
    
    for dr,dc in directions:
        if data[r+dr][c+dc]=='#': 
            continue
        elif data[r+dr][c+dc]=='.' and l+1<min_dist[r+dr][c+dc]:
            heap.append([r+dr,c+dc,l+1])
            min_dist[r+dr][c+dc]=l+1
        elif data[r+dr][c+dc]=='AA': 
            continue
        elif data[r+dr][c+dc]=='ZZ': 
            continue
        elif data[r+dr][c+dc].isupper():
            print(warps[data[r+dr][c+dc]])
            for [ddr,ddc] in warps[data[r+dr][c+dc]]:
                if l+1<min_dist[ddr][ddc]:
                    heap.append([ddr,ddc,l+1])
                    min_dist[ddr][ddc]=l+1
                   
total_p1 = min_dist[er][ec]


min_dist=[[[99999 for c in data[0]] for r in data] for l in range(0,1000)]
heap=[[0,sr,sc,0]]
i=0

inner_c=[4,len(data[0])-4]
inner_r=[4,len(data)-4]

while i<len(heap):
    rcr,r,c,l=heap[i]
    i+=1
    #print(i,rcr,r,c)
    #Eindpunt
    if r==er and c==ec and rcr==0:
        continue
    if rcr>=100:
        continue
    
    #Niet meer de kortste optie in de hele heap
    if l>min_dist[rcr][r][c]:
        continue
    
    for dr,dc in directions:
        if data[r+dr][c+dc]=='#': 
            continue
        elif data[r+dr][c+dc]=='.' and l+1<min_dist[rcr][r+dr][c+dc]:
            heap.append([rcr,r+dr,c+dc,l+1])
            min_dist[rcr][r+dr][c+dc]=l+1
        elif data[r+dr][c+dc]=='AA': #Wall or start
            continue
        elif data[r+dr][c+dc]=='ZZ': #Wall or end
            continue
        elif data[r+dr][c+dc].isupper():
            for [ddr,ddc] in warps[data[r+dr][c+dc]]:
                if r==ddr and c==ddc: #Doe niets met de stap naar dezelfde locatie
                    #print("backstep")
                    continue
                
                #Door de warp recurs je naar buiten of naar binnen
                new_level=rcr-1
                if c>inner_c[0] and c<inner_c[1] and r>inner_r[0] and r<inner_r[1]:
                    new_level+=2
                #Op het eerste level zijn de warps muren
                if new_level<0:

                    continue
                if new_level>=35:
                    continue
                    
                if l+1<min_dist[new_level][ddr][ddc]:
                    heap.append([new_level,ddr,ddc,l+1])
                    min_dist[new_level][ddr][ddc]=l+1
                   
total_p2 = min_dist[0][er][ec]




print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))