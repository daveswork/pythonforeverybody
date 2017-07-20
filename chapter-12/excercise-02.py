#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 2: Change your socket program so that it counts the number of 
characters it has received and stops displaying any text after it has shown 
3000 characters. The program should retrieve the entire document and count the 
total number of characters and display the count of the number of characters 
at the end of the document.
"""

import socket

completed = ""
dirty_url = input("Enter url to retrieve: ")
url = dirty_url.split("/")[2]
try: 
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((url, 80))
    format_cmd = "GET " + dirty_url + " HTTP/1.0\r\n\r\n"
    cmd = format_cmd.encode()
    mysock.send(cmd)
    
    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        completed = completed + data.decode()
    mysock.close()
    print("Total length: ", len(completed))
    if len(completed) < 3000:
        print(completed)
    else:
        print(completed[:2999])
    
except:
    print("Error retrieving page.")