#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 2: Write a program to prompt for a file name, and then read through 
the file and look for lines of the form: X-DSPAM-Confidence: 0.8475 
When you encounter a line that starts with "X-DSPAM-Confidence:" 
pull apart the line to extract the floating-point number on the line. 
Count these lines and then compute the total of the spam 
confidence values from these lines. When you reach the end of the file, print 
out the average spam confidence. 
Enter the file name: mbox.txt 
Average spam confidence: 0.894128046745 
Enter the file name: mbox-short.txt 
Average spam confidence: 0.750718518519 
Test your file on the mbox.txt and mbox-short.txt files.

Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle Locations 1700-1704). Kindle Edition. 
"""

def mbox_file(in_file):
    total = 0
    count = 0
    try:
        with open(in_file) as text:
            for line in text:
                if "X-DSPAM-Confidence:" in line:
                    total += float(line[line.find(":")+1:-1])
                    count += 1
        print("Average spam confidence: ", total/count)             
    except:
        print("File cannot be opened: ", in_file)


mbox = input("Enter a file name: ")
mbox_file(mbox)