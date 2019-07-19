#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:08:42 2019

@author: tamar
"""

import math

while True:
    try:
        x = float(input('Enter a number x: ')); 
    except ValueError:
        continue
    else:
        break
    
while True:
    try:
        y = float(input('Enter a number y: '))
    except ValueError:
        continue
    else:
        break

print('x**y: ', 
      x**y);

print('log(x): ', 
      math.log2(x))

#the longer blocks prompt the user to enter a number
#used a while loop to account for the possibility
#that the user might type something other than a 
#number