#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 4: Add code to the above program to figure out who has the most 
messages in the file.

After all the data has been read and the dictionary has been created, look 
through the dictionary using a maximum loop (see Section [maximumloop]) to 
find who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""

def senders(in_file):
    count = dict()
    maximum = 0
    user = ""
    try:
        with open(in_file) as text:
            for line in text:
                if line.startswith("From "):
                    line = line.split()
                    count[line[1]] = count.get(line[1], 0) + 1
            for key in count:
                if maximum == 0:
                    maximum = count[key]
                    user = key
                else:
                    if count[key] > maximum:
                        maximum = count[key]
                        user = key
            print(user, maximum)
    except:
        print("Error opening", in_file)

mbox = input("Enter a file name: ")
senders(mbox)