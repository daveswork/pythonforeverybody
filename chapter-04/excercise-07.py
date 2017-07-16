#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 7: Rewrite the grade program from the previous chapter using a 
function called computegrade that takes a score as its parameter and returns a 
grade as a string. 
Score Grade 
> 0.9 A 
> 0.8 B 
> 0.7 C 
> 0.6 D 
< = 0.6 F
Program Execution: 
Enter score: 0.95 
A
 
Enter score: perfect 
Bad score 

Enter score: 10.0 
Bad score 

Enter score: 0.75 
C 

Enter score: 0.5 
F 

Run the program repeatedly to test the various different values for input.


Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle 
Locations 1037-1041). Kindle Edition. 
"""

def computegrade(sinp):
    error_message = "Bad score"
    try:
        score = float(sinp)
        if score > 1.0:
            print(error_message)
        elif score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")        
    except:
        print(error_message)
    


sinp = input("Enter score: ")
computegrade(sinp)