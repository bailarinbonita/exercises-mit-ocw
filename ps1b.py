#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 12:32:24 2019

@author: tamar
"""

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

#user-provided variables

portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04
months = 0

#portion down payment and r are fixed variables. r is the return rate on investments.
#portion down payment is a quarter of the total cost of the house. the algorithm
#ceases when current savings exceeds the portion down payment.

while portion_down_payment > current_savings:
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
    else:
        pass
    current_savings += (portion_saved * (annual_salary / 12)) + ((current_savings * r) / 12)

#basically, the only changes between ps1a and ps1b are the additions of another user-
#defined variable and the conditional in the while loop to account for the change in
#salary over time.

print('Number of months:', months)

#when using test cases, two of the calculations are a bit off, but I haven't been able 
#to locate the issue.