#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 3: Write a program to read through a mail log, build a histogram 
using a dictionary to count how many messages have come from each email 
address, and print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
"""

def senders(in_file):
    count = dict()
    try:
        with open(in_file) as text:
            for line in text:
                if line.startswith("From "):
                    line = line.split()
                    count[line[1]] = count.get(line[1], 0) + 1
            print(count)
    except:
        print("Error opening", in_file)

mbox = input("Enter a file name: ")
senders(mbox)