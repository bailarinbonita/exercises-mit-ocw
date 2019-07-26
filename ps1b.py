#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 14:37:29 2019

@author: tamar
"""

annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04
months = 0

while portion_down_payment > current_savings:

    for i in range(1):
        months += 1

        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
        else:
            pass

    current_savings += (portion_saved * (annual_salary / 12)) + ((current_savings * r) / 12)

print('Number of months:', months)