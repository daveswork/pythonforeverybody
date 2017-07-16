#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the 
hourly rate for hours worked above 40 hours. 
Enter Hours: 45 
Enter Rate: 10 
Pay: 475.0

Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle 
Locations 782-784). Kindle Edition. 
"""

hours = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))

if hours <= 40:
    pay = round(hours * rate, 2)
else:
    pay = round(40 * rate + (hours - 40) * rate * 1.5 , 2)

print("Pay: ", pay )