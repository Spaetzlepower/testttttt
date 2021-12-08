# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 21:04:26 2021

@author: matth
"""

import random
start_balance=250
bet_size_original=0.2
list=[]
orange=46
black=46
zero=8
bet_size=bet_size_original
bet_size_list=[]
for i in range(10000):
    #betting next round?
    if orange<=39:
        betting_process_start='yes'
        
    elif orange > 50:
        betting_process_start='no'
    else:
         pass
    if betting_process_start == 'yes' and orange<=45 and sum(l is not 'orange' for l in list[-4:])==4:
        start_balance-=bet_size
        bet='yes'
        bet_size_list.append(bet_size)
    else:
        bet='no'
    x=random.randrange(0,15,1)
    #print(x)
    #geld rein oder raus
    if bet=='yes':
       if x>=1 and x<=7:
          start_balance+= bet_size*2
       else:
           pass
    else:
        pass
    
    if x==0:
        list.append('zero')
        current_x=('zero')
    elif x>=1 and x<=7:
        list.append('orange')
        current_x=('orange')
    else:
        list.append('black')
        current_x=('black')
        
    if current_x != 'orange' and bet_size<bet_size_original*10:
        bet_size=bet_size*2
    else:
        bet_size=bet_size_original
    list=list[-100:]
    #print(list)
    zero=list.count('zero')
    orange=list.count('orange')
    black=list.count('black')
    
print(start_balance)
print(max(bet_size_list))
#print(bet_size_list)

import matplotlib.pyplot as plt
import numpy as np


keys, counts = np.unique(bet_size_list, return_counts=True)

plt.bar(keys, counts,0.2)
plt.show()
    