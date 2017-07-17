#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 5: Write a program to read through the mail box data and when you 
find line that starts with "From", you will split the line into words using 
the split function. We are interested
in who sent the message, which is the second word on the From line. 
From stephen.marquard@ uct.ac.za Sat Jan 5 09: 14: 16 2008 
You will parse the From line and print out the second word for each From line, 
then you will also count the number of From (not From:) lines and print out a 
count at the end. This is a good sample output with a few lines removed: 
    
python fromcount.py 
Enter a file name: mbox-short.txt 
stephen.marquard@ uct.ac.za 
louis@ media.berkeley.edu 
zqian@ umich.edu [... 
some output removed...] 
ray@ media.berkeley.edu 
cwen@ iupui.edu 
cwen@ iupui.edu
cwen@ iupui.edu 
There were 27 lines in the file with From as the first word

Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle 
Locations 2062-2064). Kindle Edition. 
"""


def sender_list(in_file):
    senders = []
    words = []
    total_senders = 0
    try:
        with open(in_file) as mailbox:
            for line in mailbox:
                if line.startswith("From "):
                    words = line.split()
                    senders.append(words[1])
                    total_senders += 1
            if len(senders)>0:
                for sender in senders:
                    print(sender)
            print("There were", total_senders, "lines in the file with From \
as the first word")
    except:
        print("Error accessing", in_file)

mailfile = input("Enter a filename: ")
sender_list(mailfile)
        

