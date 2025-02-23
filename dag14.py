# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import math
start_time = time.time_ns()

def get_cost(resource,needed):
    if resource=='ORE':
        return needed

    #Hoevaak moeten we dit recept nog maken
    nrecipes=math.ceil((needed-storage[resource])/recipes[resource][0])
    #Wat houden we over
    storage[resource]+=nrecipes*recipes[resource][0]-needed
    
    if nrecipes<=0:
        return 0
    
    ore_cost=0
    for [ncost,keycost] in recipes[resource][1]:
            ore_cost+=get_cost(keycost,nrecipes*ncost)
    return ore_cost
    


f = open("input.txt", "r")
recipes=dict()
storage=dict()
for i,line in enumerate(f):
    line=line.replace('\n','')
    prod=line.split(' => ')[1]
    key=prod.split(' ')[1]
    nkey=int(prod.split(' ')[0])
    costs=line.split(' => ')[0].split(', ')
    total_cost=list()
    for cost in costs:
        key_cost=cost.split(' ')[1]
        ncost=int(cost.split(' ')[0])
        total_cost.append([ncost,key_cost])  
    recipes[key]=[nkey,total_cost]
    storage[key]=0 
f.close()
storage['ORE']=0


print("Part 1",get_cost('FUEL',1),)
print("Part 2",int(10**12//(get_cost('FUEL',10000000)/10000000)))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))