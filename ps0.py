#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:08:42 2019

@author: tamar
"""

import math

while True:
    try:
        x = int(input('Enter a number x: ')); 
    except ValueError:
        continue
    else:
        break
    
while True:
    try:
        y = int(input('Enter a number y: '))
    except ValueError:
        continue
    else:
        break

print('x**y: ', 
      x**y);

print('log(x): ', 
      math.log2(x))
