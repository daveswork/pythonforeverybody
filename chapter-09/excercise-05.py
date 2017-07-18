#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 5: This program records the domain name (instead of the address) 
where the message was sent from instead of who the mail came from (i.e., the 
whole email address). At the end of the program, print out the contents of 
your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
"""

def senders(in_file):
    count = dict()
    try:
        with open(in_file) as text:
            for line in text:
                if line.startswith("From "):
                    line = line.split()[1].split("@")
                    count[line[1]] = count.get(line[1], 0) + 1
            print(count)
    except:
        print("Error opening", in_file)

mbox = input("Enter a file name: ")
senders(mbox)