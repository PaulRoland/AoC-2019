# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()


def maze_lengths_keys(maze,start_key):
    sr,sc=object_locations[start_key]
    heap=[[sr,sc,0,[]]]
    i=0
    min_dist=[[999 for c in maze[0]] for r in maze]
    min_dist[sr][sc]=0
    directions=[[-1,0],[0,1],[1,0],[0,-1]]
    path_lengths=dict()
    while i<len(heap):
        r,c,l,keys_needed=heap[i]
        if l>min_dist[r][c]: continue
        for dr,dc in directions:
            if maze[r+dr][c+dc]=='#': continue
            if min_dist[r+dr][c+dc]<l+1: continue
            
            if maze[r+dr][c+dc].isupper():
                keys_needed.append(maze[r+dr][c+dc].lower())
                path_lengths[maze[r+dr][c+dc]]=[l+1,keys_needed]
            if maze[r+dr][c+dc].islower():
                path_lengths[maze[r+dr][c+dc]]=[l+1,keys_needed]
            heap.append([r+dr,c+dc,l+1,list(keys_needed)])
            min_dist[r+dr][c+dc]=l+1
        i+=1
    return path_lengths



          
def shortest_path(start_key,total_length,keys):
    global best,all_keys
    extra_keys=list(keys)
    extra_keys.sort()
    dict_key=start_key+'_'+''.join(extra_keys)

    if dict_key in mem:
        return total_length + mem[dict_key]
    
    if total_length>=best:
        return total_length + 10**9

    if len(keys)==len(all_keys):
        best=total_length
        return total_length
        
    new_length=10**99     
    for opt in options[start_key]:
        if opt.isupper(): #Geen interesse in deuren, alleen in sleutels
            continue
        if opt in keys: #Deze hebben we al
            continue
        
        keys_needed=options[start_key][opt][1]
        
        if set(keys_needed)<=set(keys):
            path_length=options[start_key][opt][0]
            new_keys=list(keys)
            new_keys.append(opt)
            new_length = min(new_length,shortest_path(opt,total_length+path_length,new_keys))
    
    mem[dict_key]=new_length-total_length
    return new_length




def shortest_path4(start_key,total_length,keys):
    global best,all_keys
    extra_keys=list(keys)
    extra_keys.sort()
    dict_key=start_key+'_'+''.join(extra_keys)

    if dict_key in mem:
        return total_length + mem[dict_key]
    
    if total_length>=best:
        return total_length + 10**9

    if len(keys)==len(all_keys):
        best=total_length
        return total_length
        
    new_length=10**99   
    for i,s in enumerate(list(start_key)):

        for opt in options[s]:
            if opt.isupper(): #Geen interesse in deuren, alleen in sleutels
                continue
            if opt in keys: #Deze hebben we al
                continue
            
            keys_needed=options[s][opt][1]

            if set(keys_needed)<=set(keys):
                path_length=options[s][opt][0]
                new_keys=list(keys)
                new_keys.append(opt)
                new_start_key=list(start_key)
                new_start_key[i]=opt
                new_start_key=''.join(new_start_key)
                #print(new_start_key)
                
                new_length = min(new_length,shortest_path4(new_start_key,total_length+path_length,new_keys))
    
    mem[dict_key]=new_length-total_length
    return new_length
  



  

f = open("input.txt", "r")
data=list()
object_locations=dict()
all_keys=list()
doors=list()
for row,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    for col,s in enumerate(line):
        if s=='#' or s=='.':
            continue
        object_locations[s]=[row,col]
        if s.islower():
            all_keys.append(s)
        else:
            doors.append(s)
        
    data.append(line)
    line=line.replace('.',' ').replace('#','\u2588')
f.close()

options=dict()
for key in object_locations:
    options[key]=maze_lengths_keys(data,key)
#print(options)

best=10**99
mem=dict()
shortest_path('@',0,[])

###Part 2
r,c=object_locations['@']
data[r-1]=data[r-1][:c-1]+'1#2'+data[r-1][c+2:]
data[r]=  data[r][:c-1]+'###'+data[r][c+2:]
data[r+1]=data[r+1][:c-1]+'3#4'+data[r+1][c+2:]

del object_locations['@']
object_locations['1']=[r-1,c-1]
object_locations['2']=[r-1,c+1]
object_locations['3']=[r+1,c-1]
object_locations['4']=[r+1,c+1]

options=dict()
for key in object_locations:
    options[key]=maze_lengths_keys(data,key)
shortest_path4('1234',0,[])    
    





print("Part 1",mem['@_'])
print("Part 2",mem['1234_'])
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))