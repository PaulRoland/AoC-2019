# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import itertools as it
start_time = time.time_ns()

def get_modevalues(i,nums,modes,n,base):
    if i+1 in nums:
        value1=nums[i+1]
        if modes[2]==2:
            value1=value1+base
            print(value1)
            modes[2]=0
        if modes[2]==0:
            if value1 in nums:
                value1=nums[value1]
            else:
                value1=0
    if n==1:
        return [value1]
    
    if i+2 in nums:
        value2=nums[i+2]
        if modes[1]==2:
            value2=value2+base
            modes[1]=0
        if modes[1]==0:
            if value2 in nums:
                value2=nums[value2]
            else:
                value2=0
        
    if n==2:
        return [value1,value2]
    
    if i+3 in nums:
        value3=nums[i+3]
        if modes[0]==0:
            value3=nums[nums[i+3]]  
    return [value1,value2,value3]

    
def compute(nums,instructions,inp):
    output=0
    base=0
    i=0
    
    while i<len(nums):
        mode_op=str(nums[i]).zfill(5)
        mode=[int(d) for d in list(mode_op[0:3])]
        opcode=int(mode_op[3:])

        #print(ind3,ind1,ind2)
        if opcode in [1,2,5,6,7,8]:
            [value1,value2]=get_modevalues(i,nums,mode,2,base)
            
        if opcode==1: #add
            pos=nums[i+3]+base*(mode[0]==2)
            nums[pos]=value1+value2
            i+=4
        
        elif opcode==2: #multiply
            pos=nums[i+3]+base*(mode[0]==2)
            nums[pos]=value1*value2
            i+=4
        elif opcode==3: #Input
            value1=nums[i+1]+base*(mode[2]==2)
            nums[value1]=inp
            i+=2
        elif opcode==4: #Output
            [value1]=get_modevalues(i,nums,mode,1,base)
            output=value1
            print("Output",value1)
            i+=2
        elif opcode==5: #Jump if true
            if value1!=0:
                i=value2
            else:
                i+=3
                
        elif opcode==6: #Jump if false
            if value1==0:
                i=value2
            else:
                i+=3
                
        elif opcode==7: #less than
            pos=nums[i+3]+base*(mode[0]==2)
            if value1<value2:
                nums[pos]=1
            else:
                nums[pos]=0
            i+=4
            
        elif opcode==8: #equals
            pos=nums[i+3]+base*(mode[0]==2)
            if value1==value2:
                nums[pos]=1
            else:
                nums[pos]=0
            i+=4 
        elif opcode==9:
            [value1]=get_modevalues(i,nums,mode,1,base)
            base+=value1
            i+=2
        else:
            break
    return output

f = open("input.txt", "r")
for i,line in enumerate(f):
    nums=[int(d) for d in line.split(',')]
f.close()

memory=dict()
for i,instr in enumerate(nums):
    memory.update({i:instr})
total_p1=compute(memory,nums,2)
        
print("Part 1",total_p1)
print("Part 2")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))