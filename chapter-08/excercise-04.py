#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 4: Download a copy of the file from www.py4e.com/ code3/ romeo.txt 
Write a program to open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split function. 
For each word, check to see if the word is already in a list. 
If the word is not in the list, add it to the list. 
When the program completes, sort and print the resulting words in alphabetical 
order. 
Enter file: romeo.txt [' Arise', 'But', 'It', 'Juliet', 'Who', 'already', 
'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 
'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 
'with', 'yonder']

Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle 
Locations 2054-2062). Kindle Edition. 
"""

def word_count(in_file):
    words_list = []
    try:
        with open(in_file) as text:
            for line in text:
                words = line.split()
                for word in words:
                    if word not in words_list:
                        words_list.append(word)
        words_list.sort()
        print(words_list)
    except:
        print("Error accessing", in_file)

text_file = input("Enter file name: ")

word_count(text_file)