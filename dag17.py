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
   
def compute(nums,inp):
    base=0

    i=0
    i_op=[0,4,4,2,2,3,3,4,4,2]   
    
    
    inp_counter=0
    
    output=''
   
    while i<len(nums):
        mode_op=str(nums[i]).zfill(5)
        modes=[int(d) for d in list(mode_op[0:3])]
        opcode=int(mode_op[3:])
        [pos1,pos3,value1,value2]=get_modevalues(i,nums,modes,base)
        if opcode==1: nums[pos3]=value1+value2
        elif opcode==2: nums[pos3]=value1*value2
        elif opcode==3:
            nums[pos1]=inp[inp_counter]
            inp_counter+=1
        elif opcode==7: nums[pos3]=(value1<value2)
        elif opcode==8: nums[pos3]=(value1==value2)  
        elif opcode==9: base+=value1
        elif opcode==5 and value1!=0: i=value2-3 #-3 is fixed in last line of func.
        elif opcode==6 and value1==0: i=value2-3 #-3 is fixed in last line of func.
        elif opcode==4:
            if value1<255:
                output+=chr(value1)
            else:
                output=value1
    
        elif opcode not in [1,2,3,4,5,6,7,8,9]: break
        i+=i_op[opcode]
    return output

f = open("input.txt", "r")
line=f.readline()
nums=[int(d) for d in line.split(',')]
f.close()

memory=defaultdict(lambda: 0)
for i,instr in enumerate(nums):
    memory.update({i:instr})

scaff=compute(memory,0).split('\n')[:-2]

total_p1=0
for row,line in enumerate(scaff):
    for col,s in enumerate(line):
        if row==0 or row==len(scaff)-1: continue
        if col==0 or col==len(line)-1: continue
        
        if s=='#':
            if scaff[row-1][col]=='#' and scaff[row+1][col]=='#' and scaff[row][col+1]=='#' and scaff[row][col-1]=='#':
                total_p1+=row*col

                
######Part 2
memory=defaultdict(lambda: 0)
for i,instr in enumerate(nums):
    memory.update({i:instr})
memory[0]=2

#Handmatig gezochte oplossing
input_text=['A,A,B,C,C,A,B,C,A,B','L,12,L,12,R,12','L,8,L,8,R,12,L,8,L,8','L,10,R,8,R,12','N']
#A,A,B,C,C,A,B,C,A,B
#A: L12,L12,R12
#B: L8,L8,R12,L8,L8
#C: L10,R8,R12
#Y/N
input_ascii=list()
for row in input_text:
    for s in row:
        input_ascii.append(ord(s))
    input_ascii.append(ord('\n')) 
       
total_p2=compute(memory,input_ascii)


print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))# -*- coding: utf-8 -*-
