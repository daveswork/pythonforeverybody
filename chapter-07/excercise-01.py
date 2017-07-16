#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 1: 
Write a program to read through a file and print the contents of 
the file (line by line) all in upper case. Executing the program will look as 
follows:
python shout.py 
Enter a file name: mbox-short.txt 
FROM STEPHEN.MARQUARD@ UCT.AC.ZA SAT JAN 5 09: 14: 16 2008 
RETURN-PATH: < POSTMASTER@ COLLAB.SAKAIPROJECT.ORG > 
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90]) 
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA; SAT, 05 JAN 2008 
09: 14: 16 -0500 
You can download the file from www.py4e.com/ code3/ mbox-short.txt

Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle 
Locations 1692-1697). Kindle Edition. 
"""

def uppercase_file(in_file):
    try:
        with open(in_file) as text:
            for line in text:
                print(line.upper())   
    except:
        print("That file is not accessible.")


mbox = input("Enter a file name: ")

uppercase_file(mbox)