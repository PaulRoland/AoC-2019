# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

def req_fuel(n):
    fuel=max((n//3)-2,0)
    if fuel>0:
        fuel+=req_fuel(fuel)
    return fuel

import time
start_time = time.time_ns()
total_p1=0
total_p2=0
f = open("input.txt", "r")

for i,line in enumerate(f):
    n=int(line)
    total_p1+=n//3-2
    total_p2+=req_fuel(n)
f.close()



print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))