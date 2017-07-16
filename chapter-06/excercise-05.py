#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 5: 
Take the following Python code that stores a string: 
 ` str = 'X-DSPAM-Confidence: 0.8475' 
 Use find and string slicing to extract the portion of the string after the 
 colon character and then use the float function to convert the extracted 
 string into a floating point number.

Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle 
Locations 1482-1486). Kindle Edition. 
"""

def find_float(to_parse):
    found_float = float(to_parse[to_parse.find(":")+1:-1])
    print(found_float)


this_string = 'X-DSPAM-Confidence: 0.8475'
find_float(this_string)