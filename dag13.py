# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
from collections import defaultdict

start_time = time.time_ns()

def draw_screen(screen):
    string=''
    total_blocks=0
    for cr in range(0,23):
        string+='\n' 
        for cc in range(0,37):
            key=str(cr)+','+str(cc)
            if key in screen:
                if screen[key]==2:
                    total_blocks+=1
                    string+='X'
                elif screen[key]==1:
                    string+='\u2588'
                elif screen[key]==0:
                    string+=' '
                elif screen[key]==4:
                    string+='0'
                elif screen[key]==3:
                    string+='_'
                else:
                    string+=str(screen[key])
            else:
                string+=' '
    if '0,-1' in screen:
        print("Score: ",screen['0,-1'])
    print(string)
    return total_blocks


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
    output_count=0
    cur_output=[0,0,0]

    balx=0
    balkx=0
    while i<len(nums):
        mode_op=str(nums[i]).zfill(5)
        modes=[int(d) for d in list(mode_op[0:3])]
        opcode=int(mode_op[3:])
        [pos1,pos3,value1,value2]=get_modevalues(i,nums,modes,base)
        if opcode==1: nums[pos3]=value1+value2
        elif opcode==2: nums[pos3]=value1*value2
        elif opcode==3:
            if balkx>balx:
                nums[pos1]=-1
            elif balkx<balx:
                nums[pos1]=1

        elif opcode==7: nums[pos3]=(value1<value2)
        elif opcode==8: nums[pos3]=(value1==value2)  
        elif opcode==9: base+=value1
        elif opcode==5 and value1!=0: i=value2-3 #-3 is fixed in last line of func.
        elif opcode==6 and value1==0: i=value2-3 #-3 is fixed in last line of func.
        elif opcode==4:
            cur_output[output_count%3]=value1
            if output_count%3==2:
                screen[str(cur_output[1])+','+str(cur_output[0])]=cur_output[2]
                if cur_output[2]==4:
                    #print(i,mode_op,"changed the ball")
                    a=draw_screen(screen)
                    balx=cur_output[0]
                if cur_output[2]==3:
                    #print(i,mode_op,"changed the ball")
                    balkx=cur_output[0]
            output_count+=1
        elif opcode not in [1,2,3,4,5,6,7,8,9]: break
        i+=i_op[opcode]
        #a = draw_screen(screen)
    return screen

f = open("input.txt", "r")
line=f.readline()
nums=[int(d) for d in line.split(',')]
f.close()

memory=defaultdict(lambda: 0)
for i,instr in enumerate(nums):
    memory.update({i:instr})

screen=compute(memory)
total_p1=draw_screen(screen)
memory[0]=2
screen=compute(memory)
total_p2=screen['0,-1']

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))