#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:24:39 2019

@author: tamar
"""

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: ')) * (annual_salary / 12)
total_cost = float(input('Enter the cost of your dream home: '))
portion_down_payment = total_cost * 0.25

#These four lines require the user's input.

current_savings = 0

#r is the return on the user's investment (4%)

r = 0.04

#Used a counter to track the number of months it would take the user to reach 
#their down payment. Since the return on investments and the portion of salary
#saved are monthly calculations, the while loop operates in the same way.

months = 0
while portion_down_payment > current_savings:
        current_savings += portion_saved + ((current_savings * r) / 12)
        months += 1
print('Number of months:', months)

#Used a while loop capped at the portion down payment.