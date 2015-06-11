# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 11:57:00 2015

@author: Dang
"""
import numpy as  np
import StickBreaking

def DirichletProcess(p,n,P0=np.random.randn	):
    theta = P0(len(p))
    return np.random.choice(theta,size=n,p=p)
    
p = StickBreaking.stick_breaking(alpha=1000,k=1000)
samples = DirichletProcess(p,100)
plt.hist(samples)