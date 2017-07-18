#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 1: Write a simple program to simulate the operation of the grep 
command on Unix. Ask the user to enter a regular expression and count the 
number of lines that matched the regular expression:

$ python grep.py
Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

$ python grep.py
Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

$ python grep.py
Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$
"""

import re

def search_and_count(query):
    count = 0
    try:
        with open("mbox.txt") as text:
            for line in text:
                if re.search(query, line):
                    count += 1
        print("mbox.txt had", count, "lines that matched", query)
    except:
        print("Error accessing mbox.txt")

search_re = input("Enter a regular expression: ")
search_and_count(search_re)