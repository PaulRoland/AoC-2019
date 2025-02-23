# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import math
start_time = time.time_ns()

f = open("input.txt", "r")
asteroids=dict()
for row,line in enumerate(f):
    for col,s in enumerate(line):
        if s=='#':
            asteroids.update({str(row)+','+str(col):1})
f.close()

for ast in asteroids:
    [r,c]=[int(d) for d in ast.split(',')]
    los=set()
    ast_list=list()
    for new_ast in asteroids:
        if ast==new_ast:
            continue
        rr,cc=[int(d) for d in new_ast.split(',')]
        
        div=math.gcd(rr-r,cc-c)
        los.add(str((rr-r)/div)+str((cc-c)/div))

        #ast_list.append([(math.atan2(rr-r,cc-c)+math.pi/2)%(2*math.pi),((rr-r)**2+(cc-c)**2)**0.5,rr,cc])
                   
    asteroids[ast]=[los,ast_list]

total_p1=0
for ast in asteroids:
    if len(asteroids[ast][0])>total_p1:
        total_p1=len(asteroids[ast][0])
        max_ast=ast

ast_list=list()
[r,c]=[int(d) for d in max_ast.split(',')]
for ast in asteroids:
    if ast==max_ast:
        continue
    rr,cc=[int(d) for d in ast.split(',')]
    ast_list.append([(math.atan2(rr-r,cc-c)+math.pi/2)%(2*math.pi),((rr-r)**2+(cc-c)**2)**0.5,rr,cc])
        

print(ast_list)
ast_list.sort()

i=0
angle_prev=-1
counter=0
index_had=list()
while counter<200:
    i=i%len(ast_list)
    if i in index_had:
        i+=1
        #print("new round")
        continue
    if ast_list[i][0]==angle_prev:
        i+=1
        continue
    print(counter+1,"asteroid at:",ast_list[i][3],ast_list[i][2],"i=",i)
    index_had.append(i)
    angle_prev=ast_list[i][0]
    counter+=1
    
   
    
print("Part 1",total_p1)
print("Part 2",ast_list[i][3]*100+ast_list[i][2])
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))