# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def path_corners(path_instruction):
    #Convertst instructions : URDL + number, into a list of corners
    corners=[[0,0,0]]
    dirs={'U':[-1,0],'R':[0,1],'D':[1,0],'L':[0,-1]}
    for instruction in path_instruction:
        direc=instruction[0]
        length=int(instruction[1:])
        corners.append([corners[-1][0]+dirs[direc][1]*length,corners[-1][1]+dirs[direc][0]*length,corners[-1][2]+length])
        
    return corners

def path_intersect(path1,path2):
    #For two lists of corners, return the intersections and the corresponding lengths, assuming only hor/vertical lines
    intersects=list()
    for [x1,y1,l1],[x2,y2,_] in zip(path1,path1[1:]):
        for [x3,y3,l3],[x4,y4,_] in zip(path2,path2[1:]):
            if (x1==x2 and x3==x4) or (y1==y2 and y3==y4):
                continue
            
            if ((x3>=x1 and x3<=x2) or (x3>=x2 and x3<=x1)) and ((y1<=y3 and y1>=y4) or (y1<=y4 and y1>=y3)):
                intersects.append([x3,y1,l1+abs(x3-x1),l3+abs(y3-y1)])
                continue
                
            if ((x1>=x3 and x1<=x4) or (x1>=x4 and x1<=x3)) and ((y3<=y1 and y3>=y2) or (y3<=y2 and y3>=y1)):
                intersects.append([x1,y3,l1+abs(y3-y1),l3+abs(x3-x1)])
                continue          
    return intersects
        
f = open("input.txt", "r")
path1_instructions=f.readline().replace('\n','').split(',')
path2_instructions=f.readline().replace('\n','').split(',')
f.close()

wc1=path_corners(path1_instructions) #returns list of [x,y,total l]
wc2=path_corners(path2_instructions) #returns list of [x,y,total l]
intersections = path_intersect(wc1,wc2) #return list of [x,y,l1,l2]

total_p1=10**99
total_p2=10**99
for [x,y,l1,l2] in intersections:
    
    dist1=abs(x)+abs(y)
    if dist1==0:
        continue
    
    dist2=l1+l2
    
    total_p1=min(total_p1,dist1)
    total_p2=min(total_p2,dist2)
    
print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))