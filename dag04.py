# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()
    
def n_options(start,rl,rh,n):
    if n==0:
        if int(start)>=rl and int(start)<=rh and len(set(start))<6:
            counts=list()
            for num in set(start):
                counts.append(start.count(num))
            if 2 in counts:
                return [1,1]
            return [1,0]
        return [0,0]
    
    total1,total2=[0,0]
    if start=='':
        start_n=0
    else:
        start_n=int(start[-1])
    
    for new_digit in range(start_n,10):
        [new1,new2]=n_options(start+str(new_digit),rl,rh,n-1)
        [total1,total2]=[total1+new1,total2+new2]
    
    return total1,total2   


ranges=[347312,805915]
total_p1,total_p2=n_options('',ranges[0],ranges[1],6)
print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))