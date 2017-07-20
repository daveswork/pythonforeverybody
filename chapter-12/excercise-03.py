#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 3: 
Use urllib to replicate the previous exercise of (1) retrieving 
the document from a URL, (2) displaying up to 3000 characters, and (3) 
counting the overall number of characters in the document. Don't worry about 
the headers for this exercise, simply show the first 3000 characters of the 
document contents.

"""
import urllib.request

contents = ""
requested_url = input("Enter url: ")

try:
    page = urllib.request.urlopen(requested_url)
    for line in page:
        line = line.decode()
        contents = contents + line
    if len(contents) < 3000:
        print(contents)
    else:
        print(contents[:2999])
except:
    print("Error accessing page")

