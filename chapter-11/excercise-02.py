#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 2: Write a program to look for lines of the form

`New Revision: 39772`
and extract the number from each of the lines using a regular expression and 
the findall() method. Compute the average of the numbers and print out the 
average.

Enter file:mbox.txt
38549.7949721

Enter file:mbox-short.txt
39756.9259259
"""
import re

def find_and_average(in_file):
    count = 0
    total = 0
    revision = ""
    try:
        with open(in_file) as text:
            for line in text:
                revision = re.findall('^New Revision: ([0-9.]+)', line)
                if revision:
                    total += float(revision[0])
                    count += 1
        print(total/count)                
    except:
        print("Error opening", in_file)

mbox = input("Enter file:")
find_and_average(mbox)