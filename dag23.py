# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
from collections import defaultdict
from copy import copy

start_time = time.time_ns()


def get_modevalues(i,nums,modes,base):
    value1=nums[i+1]+base*(modes[2]==2)
    value2=nums[i+2]+base*(modes[1]==2)
    pos1=value1
    pos3=nums[i+3]+base*(modes[0]==2)
    if modes[2]!=1: value1=nums[value1]
    if modes[1]!=1: value2=nums[value2]
    return [pos1,pos3,value1,value2]
   
def compute(cpu,nums,base,i,input_count,output_count,output):
    i_op=[0,4,4,2,2,3,3,4,4,2]
    
    global packages
    global last_input
    global NAT

    while i<len(nums):
        mode_op=str(nums[i]).zfill(5)
        modes=[int(d) for d in list(mode_op[0:3])]
        opcode=int(mode_op[3:])
        [pos1,pos3,value1,value2]=get_modevalues(i,nums,modes,base)
        if opcode==1: nums[pos3]=value1+value2
        elif opcode==2: nums[pos3]=value1*value2
        elif opcode==3:
            if input_count==0:
                #print(cpu,"Ik wacht op een uniek adres")
                #print(cpu,pos1)
                nums[pos1]=cpu
                input_count+=1
                
            else:
                #print(cpu,"Input",input_count)
                #print(packages[cpu])
                if len(packages[cpu])>0:
                    nums[pos1]=packages[cpu][0][(input_count-1)%2]
                    input_count+=1
                
                    if (input_count-1)%2==0:
                        packages[cpu].remove(packages[cpu][0])
                else:
                    #print("Er staat geen packet klaar")
                    nums[pos1]=-1
                last_input[cpu]=nums[pos1]
            #print(cpu,"Input",nums[pos1])
            
        elif opcode==7: nums[pos3]=(value1<value2)
        elif opcode==8: nums[pos3]=(value1==value2)  
        elif opcode==9: 
            #print("Komen we hier?")
            #print(value1)
            base+=value1
        elif opcode==5 and value1!=0: i=value2-3 #-3 is fixed in last line of func.
        elif opcode==6 and value1==0: i=value2-3 #-3 is fixed in last line of func.
        elif opcode==4:
            output[output_count%3]=value1
            if output_count%3==2:
                if output[0]==255:
                    if len(NAT)==0:
                        print("Part 1: ",output[2])
                    NAT=output[1:]
                else:
                    packages[output[0]].append(output[1:])
            output_count+=1
    
        elif opcode not in [1,2,3,4,5,6,7,8,9]: break
    
        i+=i_op[opcode]
        
        break #Break to step all computers
    return nums,base,i,input_count,output_count,output

f = open("input.txt", "r")
line=f.readline()
nums=[int(d) for d in line.split(',')]
f.close()

memory=defaultdict(lambda: 0)
for i,instr in enumerate(nums):
    memory.update({i:instr})
    
    
n_cpus=50
network = [copy(memory) for i in range(0,n_cpus)]

packages=[list() for _ in range(0,n_cpus)]
bases=[0 for _ in range(0,n_cpus)]
input_counters=[0 for _ in range(0,n_cpus)]
output_counters=[0 for _ in range(0,n_cpus)]
output_buffer=[[0,0,0] for _ in range(0,n_cpus)]
cpu_i=[0 for _ in range(0,n_cpus)]
last_input=[0 for _ in range(0,n_cpus)]
NAT=list()
prev_NAT=0
#Synchronize all computers
counter=0
while True:
    #print("New step:",cpu_i)
    counter+=1
    for n,nums in enumerate(network):
        network[n],base_n,cpu_in,input_n,output_n,output=compute(n,nums,bases[n],cpu_i[n],input_counters[n],output_counters[n],output_buffer[n])
        output_counters[n]=output_n
        input_counters[n]=input_n
        output_buffer[n]=output
        bases[n]=base_n
        cpu_i[n]=cpu_in

    #print(cpu_i)
    #print(bases)
    #print(packages)
    #print(last_input)
    if set(last_input)=={-1} and len(NAT)>0 and packages==[list() for _ in range(0,n_cpus)]:
        #print(packages)
        #print("Stalling?",counter)
        #print("Stalling",NAT)
        #print("Injecting packet!",NAT)
        packages[0]=[NAT]
        if NAT==prev_NAT:
            print("Part 2: ",NAT[1])
            break
        prev_NAT=NAT
        #print(packages)

#print("Part 1",output)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))# -*- coding: utf-8 -*-
