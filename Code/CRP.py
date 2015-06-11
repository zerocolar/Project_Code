# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 16:34:34 2015

@author: Dang
"""
import numpy as np
import matplotlib.pyplot as plt
def ChineseRestaurantProcess(n,alpha):
    if n<1:
        return None
        
    table_assignments = np.empty(n)
    next_table = 0
    
    for c in range(n):
        if np.random.random < (1.*alpha/(alpha+c)):
            table_assignments[c] = next_table
            next_table+=1
        else:
            probs=[(table_assignments[:c]==i).sum()/float(c) 
                     for i in range(next_table)]
            print probs
            table_assignments[c] = np.random.choice(range(next_table),p=probs)
    return  table_assignments

n =10
alpha = 1

def plot_crp(table_nums,ax = None):
    x = range(int(table_nums.max())+1)
    f = [(table_nums==i).sum() for i in set(table_nums)]
    if ax is None: ax=plt
    ax.bar(x,f)
fig,axes = plt.subplots(2,5,sharex=True,sharey=True,figsize=(10,6))
for ax in np.ravel(axes):
    plot_crp(ChineseRestaurantProcess(n,alpha),ax=ax)