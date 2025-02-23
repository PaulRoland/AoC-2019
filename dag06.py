# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def find_orbits(mass,depth,path):
    total=depth
    path.append(mass)
    if mass == 'YOU':
        global path_YOU
        path_YOU=set(path)
    if mass == 'SAN':
        global path_SAN
        path_SAN=set(path)
    
    if mass not in orbits:
        return depth
    
    for new_mass in orbits[mass]:
        total+=find_orbits(new_mass,depth+1,list(path))

    return total

f = open("input.txt", "r")
orbits=dict()
for i,line in enumerate(f):
    a,b=line.replace('\n','').split(')')
    if a in orbits:
        orbits[a].append(b)
        continue
    orbits.update({a:[b]})
f.close()

path_YOU=set()
path_SAN=set()

total_p1=find_orbits('COM',0,list())
total_p2=len(path_YOU ^ path_SAN)-2


print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))