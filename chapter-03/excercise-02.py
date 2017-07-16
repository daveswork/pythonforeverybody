#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 2: Rewrite your pay program using try and except so that your program 
handles non-numeric input gracefully by printing a message and exiting the 
program. The following shows two executions of the program: 
Enter Hours: 20 
Enter Rate: nine 

Error, please enter numeric input 

Enter Hours: forty 
Error, please enter numeric input

Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle 
Locations 784-789). Kindle Edition. 
"""

hinp = input("Enter Hours: ")
try:
    hours = float(hinp)
    rinp = input("Enter rate: ")
    try:
        rate = float(rinp)
        pay = round(hours * rate, 2)
        print("Pay: ", pay )
    except:
        print("Error, please enter numeric input")
except:
    print("Error, please enter numeric input")