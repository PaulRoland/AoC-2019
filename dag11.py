# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
from collections import defaultdict

start_time = time.time_ns()

def get_modevalues(i,nums,modes,base):
    value1=nums[i+1]+base*(modes[2]==2)
    value2=nums[i+2]+base*(modes[1]==2)
    pos1=value1
    pos3=nums[i+3]+base*(modes[0]==2)
    if modes[2]!=1: value1=nums[value1]
    if modes[1]!=1: value2=nums[value2]
    return [pos1,pos3,value1,value2]
   
def compute(nums,inp):

    
    output=0
    base=0
    paint=True
    hull=dict()
    cr,cc,cd=[0,0,0]
    hull['0,0']=inp
    dirs=[[-1,0],[0,1],[1,0],[0,-1]]
    i=0
    i_op=[0,4,4,2,2,3,3,4,4,2]    
    while i<len(nums):
        mode_op=str(nums[i]).zfill(5)
        modes=[int(d) for d in list(mode_op[0:3])]
        opcode=int(mode_op[3:])
        [pos1,pos3,value1,value2]=get_modevalues(i,nums,modes,base)
        if opcode==1: nums[pos3]=value1+value2
        elif opcode==2: nums[pos3]=value1*value2
        elif opcode==3: 
            key=str(cr)+','+str(cc)
            if key in hull:
                nums[pos1]=hull[key]
            else:
                nums[pos1]=0
        elif opcode==7: nums[pos3]=(value1<value2)
        elif opcode==8: nums[pos3]=(value1==value2)  
        elif opcode==9: base+=value1
        elif opcode==5 and value1!=0: i=value2-3 #-3 is fixed in last line of func.
        elif opcode==6 and value1==0: i=value2-3 #-3 is fixed in last line of func.
        elif opcode==4:
            output=value1
            if paint==True:
                hull[str(cr)+','+str(cc)]=output
                paint=False
            else:
                cd=(cd+output*2-1)%4 #current direction 0:-1, 1:1
                cr+=dirs[cd][0]
                cc+=dirs[cd][1]
                paint=True
                
            output=value1 #output
        elif opcode not in [1,2,3,4,5,6,7,8,9]: break
        i+=i_op[opcode]
    return hull

f = open("input.txt", "r")
line=f.readline()
nums=[int(d) for d in line.split(',')]
f.close()

memory=defaultdict(lambda: 0)
for i,instr in enumerate(nums):
    memory.update({i:instr})

painted_hull=compute(memory,0)
total_p1=len(painted_hull)

painted_hull=compute(memory,1)
string=''
for cr in range(0,6):
    string+='\n' 
    for cc in range(0,42):
        key=str(cr)+','+str(cc)
        if key in painted_hull:
            if painted_hull[key]==1:
                string+='\u2588'
            else:
                string+=' '
        else:
            string+=' '

print("Part 1",total_p1)
print("Part 2",string)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))