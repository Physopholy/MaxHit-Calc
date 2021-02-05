# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 06:27:26 2021

@author: Ferrum
"""

import numpy as np

def max_hit(bonus,level):
    term1=1.3
    term2=bonus/80
    term3=level/10
    term4=bonus*level/640
    total=term1+term2+term3+term4
    return total

range=np.arange(1,100,1)

bonus=46

previous_max=np.floor(max_hit(bonus,1))

for i in range:
    hit=max_hit(bonus,i)
    if np.floor(hit)>previous_max:
        print('level = ',i, 'hit = ',np.floor(hit))
        previous_max=np.floor(hit)
    