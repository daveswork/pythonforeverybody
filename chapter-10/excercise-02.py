#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 2: 
This program counts the distribution of the hour of the day for 
each of the messages. You can pull the hour from the "From" line by finding 
the time string and then splitting that string into parts using the colon 
character. Once you have accumulated the counts for each hour, print out the 
counts, one per line, sorted by hour as shown below.

Sample Execution:

python timeofday.py
Enter a file name: mbox-short.txt
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""

def sender_frequency(in_file):
    hour = ""
    emails = dict()
    all_hours = []
    try:
        with open(in_file) as text:
            for line in text:
                if line.startswith("From "):
                    hour = line.split()[5].split(":")[0]
                    emails[hour] = emails.get(hour, 0 ) + 1
            for key in emails:
                commits = key, emails[key]
                all_hours.append(commits)
            all_hours.sort()
            for key in all_hours:
                print(key[0], key[1])
    except:
        print("Error accessing ", in_file)

mailbox = input("Enter a file name: ")
sender_frequency(mailbox)
                


