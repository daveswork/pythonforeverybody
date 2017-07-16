#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 2: Write another program that prompts for a list of numbers as above 
and at the end prints out both the maximum and minimum of the numbers instead 
of the average.

Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle 
Locations 1241-1242). Kindle Edition. 

"""

def excercise02():
    raw_num =  ""
    number = 0
    count = 0
    minimum = 0
    maximum = 0
    while True:
        raw_num = input("Enter a number: ")
        if raw_num == "done":
            break
        try:
            number = float(raw_num)
            if count == 0:
                minimum = number
                maximum = number
            else:
                if maximum <= number:
                    maximum = number
                if minimum >= number:
                    minimum = number                
            count += 1
        except:
            print("Invalid")
            
    print(minimum, " ", maximum,)
        

excercise02()