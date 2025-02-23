# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def FFT1(data):
    ptrn=[0,1,0,-1]
    shift=1
    digits=list()
    for i in range(0,len(data)):
        new_digit=0
        for j,s in enumerate(data):
            ptrn_value=ptrn[((j+shift)//(i+1))%len(ptrn)]
            new_digit+=s*ptrn_value
        digits.append(abs(new_digit)%10)
    return digits

def FFT2(data,offset):
    digits=[0 for _ in range(0,len(data))]
    
    ptrn=[0,1,0,-1]
    shift=1
    strat_breakpoint=(len(data)-2)//3
    
    for i in range(offset,strat_breakpoint):
        new_digit=0

        for j in range(0,i+1):
            plus=data[j+i::(i+1)*4]
            mins=data[j+i+(i+1)*2::(i+1)*4]
            new_digit+=sum(plus)-sum(mins)
            
               
        digits[i]=abs(new_digit)%10
      
    digits[-1]=data[-1]

    for i in list(range(max(len(data)//2,offset),len(data)-1))[::-1]:
        digits[i]=(data[i]+digits[i+1])%10      
    
    for i in range(max(strat_breakpoint,offset),len(data)//2):
        digits[i]=digits[i]=sum(data[i:2*i+1])%10

    return digits



f = open("input.txt", "r")
data=list(int(d) for d in f.readline())
f.close()

data_org=list(data)
for n in range(0,100):
    data=FFT2(data,0)
total_p1=''.join(str(d) for d in data[:8])

data=list(data_org)*10000
offset=int(''.join(str(d) for d in data[:7]))

for n in range(0,100):
    data=FFT2(data,offset)  
total_p2=''.join(str(d) for d in data[offset:offset+8])

 
print("Part 1",total_p1)
print("Part 1",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))