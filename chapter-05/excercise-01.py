#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 1: Write a program which repeatedly reads numbers until the user 
enters "done". Once "done" is entered, print out the total, count, and average 
of the numbers. If the user enters anything other than a number, detect their 
mistake using try and except and print an error message and skip to the next 
number. 
Enter a number: 4 
Enter a number: 5 
Enter a number: bad data 
Invalid input 
Enter a number: 7 
Enter a number: done 
16 3 5.333333333333333

Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle 
Locations 1236-1240). Kindle Edition. 
"""

def excercise01():
    raw_num =  ""
    number = 0
    count = 0
    total = 0
    while True:
        raw_num = input("Enter a number: ")
        if raw_num == "done":
            break
        try:
            number = float(raw_num)
            count += 1
            total = total + number
        except:
            print("Invalid")
            
    print(total, " ", count, " ", total/count)
        

excercise01()
        