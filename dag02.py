# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def compute(start_nums,target):
    
    scores=list()
    for noun,verb in [[0,0],[11,2],[12,2]]:
        nums=list(start_nums)
        nums[1]=noun
        nums[2]=verb
        i=0
        while i<len(nums):
            opcode=nums[i]
            ind1=nums[i+1]
            ind2=nums[i+2]
            ind3=nums[i+3]
            #print(ind3,ind1,ind2)
            if opcode==1:
                nums[ind3]=nums[ind1]+nums[ind2]
            if opcode==2:
                nums[ind3]=nums[ind1]*nums[ind2]
            if opcode==99:
                break
            i+=4
        scores.append(nums[0])
    nf=scores[2]-scores[1]
    [noun,verb]=[(target-scores[0])//nf,(target-scores[0])%nf]
    return nums[0],100*noun+verb

f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    nums=[int(d) for d in line.split(',')]
f.close()

[total_p1,total_p2]=compute(nums,19690720)

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))