# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
from collections import defaultdict

start_time = time.time_ns()

def draw_screen(screen,sr,sc):
    screen[str(sr)+','+str(sc)]='D'
    string=''
    output=list()
    total_blocks=0
    for cr in range(0,41):
        for cc in range(0,41):
            key=str(cr)+','+str(cc)
            if key in screen:
                if screen[key]==2:
                    string+='X'
                elif screen[key]==1:
                    string+=' '
                elif screen[key]==0:
                    string+='#'
                else:
                    string+='x'
            else:
                string+='.'
        output.append(string)
        string=''
    return output


def get_modevalues(i,nums,modes,base):
    value1=nums[i+1]+base*(modes[2]==2)
    value2=nums[i+2]+base*(modes[1]==2)
    pos1=value1
    pos3=nums[i+3]+base*(modes[0]==2)
    if modes[2]!=1: value1=nums[value1]
    if modes[1]!=1: value2=nums[value2]
    return [pos1,pos3,value1,value2]
   
def compute(nums,inp=0):
    base=0
    screen=dict()

    i=0
    i_op=[0,4,4,2,2,3,3,4,4,2]   
    directions=[[-1,0],[0,1],[1,0],[0,-1]]
    cur_direction=1
    command_dir={0:1,2:2,1:4,3:3}
    
    sr,sc,cr,cc=21,21,21,21
    
    while i<len(nums):
        mode_op=str(nums[i]).zfill(5)
        modes=[int(d) for d in list(mode_op[0:3])]
        opcode=int(mode_op[3:])
        [pos1,pos3,value1,value2]=get_modevalues(i,nums,modes,base)
        if opcode==1: nums[pos3]=value1+value2
        elif opcode==2: nums[pos3]=value1*value2
        elif opcode==3:
            nums[pos1]=command_dir[cur_direction] #move east

        elif opcode==7: nums[pos3]=(value1<value2)
        elif opcode==8: nums[pos3]=(value1==value2)  
        elif opcode==9: base+=value1
        elif opcode==5 and value1!=0: i=value2-3 #-3 is fixed in last line of func.
        elif opcode==6 and value1==0: i=value2-3 #-3 is fixed in last line of func.
        elif opcode==4:
            key=str(cr+directions[cur_direction][0])+','+str(cc+directions[cur_direction][1])
            screen[key]=value1
            
            if value1==0: #hits wall
                cur_direction=(cur_direction+1)%4
            if value1==1:
                cr+=directions[cur_direction][0]
                cc+=directions[cur_direction][1]
                cur_direction=(cur_direction-1)%4
            if value1==2:
                cr+=directions[cur_direction][0]
                cc+=directions[cur_direction][1]
                er=cr
                ec=cc
                cur_direction=(cur_direction-1)%4
                #return screen                
            
            if cr==sr and cc==sc and len(screen)>10:
                return screen,sr,sc,er,ec
    
        elif opcode not in [1,2,3,4,5,6,7,8,9]: break
        i+=i_op[opcode]
    return screen,sr,sc,er,ec

f = open("input.txt", "r")
line=f.readline()
nums=[int(d) for d in line.split(',')]
f.close()

memory=defaultdict(lambda: 0)
for i,instr in enumerate(nums):
    memory.update({i:instr})

screen,sr,sc,er,ec=compute(memory)
maze=draw_screen(screen,sr,sc)

import numpy as np
min_dist=np.ones((len(maze),len(maze[0])))*10**99
directions=[[-1,0],[0,1],[1,0],[0,-1]]
dist=0
heap=[[sr,sc,dist]]
min_dist[sr,sc]=0
i=0
while i<len(heap):
    [cr,cc,dist]=heap[i]
    for [dr,dc] in directions:
        if maze[cr+dr][cc+dc]!='#' and dist+1<min_dist[cr+dr,cc+dc]:
            min_dist[cr+dr,cc+dc]=dist+1
            heap.append([cr+dr,cc+dc,dist+1])
    i+=1
total_p1=min_dist[er,ec]

min_dist=np.ones((len(maze),len(maze[0])))*10**99
directions=[[-1,0],[0,1],[1,0],[0,-1]]
dist=0
heap=[[er,ec,dist]]
min_dist[er,ec]=0
i=0
while i<len(heap):
    [cr,cc,dist]=heap[i]
    for [dr,dc] in directions:
        if maze[cr+dr][cc+dc]!='#' and dist+1<min_dist[cr+dr,cc+dc]:
            min_dist[cr+dr,cc+dc]=dist+1
            heap.append([cr+dr,cc+dc,dist+1])
    i+=1
total_p2=min_dist[1,1]

max_dist=0
for row in min_dist:
    for s in row:
        if s<10**98:
            max_dist=max(s,max_dist)
            


print("Part 1",total_p1)
print("Part 2",max_dist)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))# -*- coding: utf-8 -*-
