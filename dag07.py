# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import itertools as it
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

    
def compute(instructions,inp,inp_n,i):
    nums=list(instructions)
    output=0
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
            nums[pos]=inp[min(inp_n,1)]
            inp_n+=1
            i+=2
        elif opcode==4: #Output
            [value1]=get_modevalues(i,nums,mode,1)
            output=value1
            #print("Output",output)
            i+=2
            return output,nums,inp_n,i
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
    return output,nums,inp_n,i

f = open("input.txt", "r")
for i,line in enumerate(f):
    nums=[int(d) for d in line.split(',')]
f.close()
start_nums=list(nums)

total_p1=0
for [A,B,C,D,E] in it.permutations([0,1,2,3,4],5):
    out_A,_,_,_=compute(start_nums,[A,0],0,0)
    out_B,_,_,_=compute(start_nums,[B,out_A],0,0)
    out_C,_,_,_=compute(start_nums,[C,out_B],0,0)
    out_D,_,_,_=compute(start_nums,[D,out_C],0,0)
    out_E,_,_,_=compute(start_nums,[E,out_D],0,0)
    if out_E>total_p1:        
        total_p1=out_E

total_p2=0
for [A,B,C,D,E] in it.permutations([9,7,8,5,6],5):
    [nums_A,nums_B,nums_C,nums_D,nums_E]=[list(nums),list(nums),list(nums),list(nums),list(nums)]
    [inp_A,inp_B,inp_C,inp_D,inp_E]=[0,0,0,0,0]
    [Ai,Bi,Ci,Di,Ei]=[0,0,0,0,0]
    out_E_prev=0
    out_E=0
    while True:
        out_A,nums_A,inp_A,Ai=compute(nums_A,[A,out_E],inp_A,Ai)
        out_B,nums_B,inp_B,Bi=compute(nums_B,[B,out_A],inp_B,Bi)
        out_C,nums_C,inp_C,Ci=compute(nums_C,[C,out_B],inp_C,Ci)
        out_D,nums_D,inp_D,Di=compute(nums_D,[D,out_C],inp_D,Di)
        out_E,nums_E,inp_E,Ei=compute(nums_E,[E,out_D],inp_E,Ei)

        if out_E==0: #E has halted
            break
        out_E_prev=out_E
    if out_E_prev>total_p2:        
        total_p2=out_E_prev
        
print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))