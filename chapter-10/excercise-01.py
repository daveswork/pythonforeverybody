#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 1: 
Revise a previous program as follows: Read and parse the "From" lines and pull 
out the addresses from the line. Count the number of messages from each person 
using a dictionary.

After all the data has been read, print the person with the most commits by 
creating a list of (count, email) tuples from the dictionary. Then sort the 
list in reverse order and print out the person who has the most commits.

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""

def sender_frequency(in_file):
    email = ""
    emails = dict()
    all_commits = []
    try:
        with open(in_file) as text:
            for line in text:
                if line.startswith("From "):
                    email = line.split()[1]
                    emails[email] = emails.get(email, 0 ) + 1
            for key in emails:
                commits = emails[key], key
                all_commits.append(commits)
            all_commits.sort()
            print(all_commits[-1][1], all_commits[-1][0])                
    except:
        print("Error accessing ", in_file)

mailbox = input("Enter a file name: ")
sender_frequency(mailbox)
                


