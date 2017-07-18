#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 3: 
Write a program that reads a file and prints the letters in 
decreasing order of frequency. Your program should convert all the input to 
lower case and only count the letters a-z. Your program should not count 
spaces, digits, punctuation, or anything other than the letters a-z. Find text 
samples from several different languages and see how letter frequency varies 
between languages. Compare your results with the tables at 
wikipedia.org/wiki/Letter_frequencies.
"""
import string 
def letter_count(in_file):
    letter_count = dict()
    letter_list = []
    try:
        with open(in_file) as text:
            for line in text:
                line = line.lower().replace(" ", "").translate(line.maketrans("", "", string.punctuation))
                for character in line:
                    if character.isalpha():
                        letter_count[character] = letter_count.get(character, 0) + 1
        for key in letter_count:
            inverse = letter_count[key], key
            letter_list.append(inverse)
        letter_list.sort(reverse=True)
        for pair in letter_list:
            print(pair[1], pair[0])
    except:
        print("Error accessing", in_file)

manuscript = input("Enter a file name: ")
letter_count(manuscript)