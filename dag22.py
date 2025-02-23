# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def modinv(index,n_cards):
    return pow(index,-1,n_cards)

def reverse(index,instructions,n_cards):
    for line in instructions[::-1]:
        if 'cut' in line:
            n=int(line.split(' ')[-1])
            index+=n
        elif 'increment' in line:
            #calculate reverse increment
            inc=int(line.split(' ')[-1])
            n1=0
            while True:
                if (index+n1*n_cards)%inc==0:
                    index=(index+n1*n_cards)//inc
                    break
                n1+=1
        else:
            index=n_cards-1-index
        index=index%n_cards
    return index    


def deal_inc(cards,inc):
    new_cards=[0 for c in cards]
    for n,card in enumerate(cards):
        new_cards[(n*inc)%len(cards)]=card
    return new_cards

def deal_new(cards):
    return cards[::-1]

def cut(cards,n):
    cards=cards[n:]+cards[:n]
    return cards


f = open("input.txt", "r")
total_cut=0
total_inc=1
instructions=list()

for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    instructions.append(line)
f.close()

card_list=list()

n_cards=10007
cards=list(range(0,10007))
for i in range(0,1):
    for line in instructions:
        if 'cut' in line:
            n=int(line.split(' ')[-1])
            cards=cut(cards,n)
            total_cut+=n
            #print("cut",n)
        elif 'increment' in line:
            n=int(line.split(' ')[-1])
            cards=deal_inc(cards,n)
            total_inc*=n
            #print("increment",n)
        else:
            cards=deal_new(cards)
            total_inc*=-1
            total_cut+=1
            #print("reverse")
#Part 2
#All cuts and reverses etc result in a linear operation  x->ax+b
#Repeated ax+b %n_cards
n_cards=119315717514047
times=101741582076661
X = 2020
Y = reverse(X,instructions,n_cards)
Z = reverse(Y,instructions,n_cards)

#Find A and B in Ax+B
#Modulo inverse: pow(index,-1,modulo number)
A = (Y-Z) * pow(X-Y,-1,n_cards)
B = (Y-A*X) % n_cards

#Repeate f(f(f(f(x)))) f=ax+b
#ax+b
#a**2x+ab+b
#a**3x+a**2b+a**2b+ab+b
#....
#a^N + (a^N+a^N-1....+a^0)*b
total_p2=((pow(A,times,n_cards)*X + (pow(A, times,n_cards)-1) * pow(A-1,-1,n_cards) * B) % n_cards)
print("Part 1",cards.index(2019))
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))