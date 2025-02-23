# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
import math
start_time = time.time_ns()

f = open("input.txt", "r")
moons=list()
for i,line in enumerate(f):
    x,y,z=[int(d) for d in re.findall('[-]?\d+',line)]
    moons.append([i,x,y,z,0,0,0])
f.close()

moon_start=list()
for moon in moons:
    moon_data=[int(d) for d in moon[1:4]]
    moon_start.append(moon_data)

moon1=dict()
moon2=dict()
moon3=dict()
moon4=dict()

step=0
loops=[0,0,0]
vel_step=[0,0,0]
for step in range(0,500000):
    #apply gravity

    for moon in moons:
        for to_moon in moons:
            if moon[0] == to_moon[0]:
                continue
            
            for i in range(1,4):
                moon[i+3]+=moon[i]<to_moon[i]
                moon[i+3]-=moon[i]>to_moon[i]
            

    #apply velocity
    vel=[0,0,0]
    for moon in moons:
        for i in range(1,4):
            moon[i]+=moon[i+3]
            vel[i-1]+=abs(moon[i+3])     
    
    for i in range(0,3):
        if vel[i]==0:
            loops[i]=(step-vel_step[i])
            vel_step[i]=step
    
    if step==999:
        total_p1=0
        for j,moon in enumerate(moons):
            pot=0
            kin=0
            for i in range(1,4):
                pot+=abs(moon[i])
                kin+=abs(moon[i+3])
            total_p1+=pot*kin

print("Part 1",total_p1)
print("Part 2",2*math.lcm(*loops))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))