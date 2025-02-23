# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def get_modevalues(i,nums,modes,n):
    value1=nums[i+1]
    if modes[2]==0:
        value1=nums[nums[i+1]]
    if n==1:
        return [value1]
    
    value2=nums[i+2]
    if modes[1]==0:
        value2=nums[nums[i+2]]
    if n==2:
        return [value1,value2]
       
    value3=nums[i+3]
    if modes[0]==0:
        value3=nums[nums[i+3]]  
    return [value1,value2,value3]

    
def compute(instructions,inp):
    nums=list(instructions)
    i=0
    while i<len(nums):
        mode_op=str(nums[i]).zfill(5)
        mode=[int(d) for d in list(mode_op[0:3])]
        opcode=int(mode_op[3:])
        
        #print(ind3,ind1,ind2)
        if opcode==1: #add
            [value1,value2]=get_modevalues(i,nums,mode,2)
            pos=nums[i+3]
            nums[pos]=value1+value2
            i+=4
            
        elif opcode==2: #multiply
            [value1,value2]=get_modevalues(i,nums,mode,2)
            pos=nums[i+3]
            nums[pos]=value1*value2
            i+=4
        elif opcode==3: #Input
            pos=nums[i+1]
            nums[pos]=inp
            i+=2
        elif opcode==4: #Output
            [value1]=get_modevalues(i,nums,mode,1)
            output=value1
            #print("Output",output)
            i+=2
        elif opcode==5: #Jump if true
            [value1,value2]=get_modevalues(i,nums,mode,2)
            if value1!=0:
                i=value2
            else:
                i+=3
                
        elif opcode==6: #Jump if false
            [value1,value2]=get_modevalues(i,nums,mode,2)
            if value1==0:
                i=value2
            else:
                i+=3
                
        elif opcode==7: #less than
            [value1,value2]=get_modevalues(i,nums,mode,2)
            pos=nums[i+3]
            if value1<value2:
                nums[pos]=1
            else:
                nums[pos]=0
            i+=4
            
        elif opcode==8: #equals
            [value1,value2]=get_modevalues(i,nums,mode,2)
            pos=nums[i+3]
            if value1==value2:
                nums[pos]=1
            else:
                nums[pos]=0
            i+=4            
        else:
            break
    return output


f = open("input.txt", "r")
for i,line in enumerate(f):
    nums=[int(d) for d in line.split(',')]
f.close()

print("Part 1",compute(nums,1))
print("Part 2",compute(nums,5))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))