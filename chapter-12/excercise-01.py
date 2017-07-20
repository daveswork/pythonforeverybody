#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 1: 
Change the socket program socket1.py to prompt the user for the URL so it can 
read any web page. You can use split('/') to break the URL into its component 
parts so you can extract the host name for the socket connect call. Add error 
checking using try and except to handle the condition where the user enters 
an improperly formatted or non-existent URL.


"""

import socket

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
        print(data.decode())
    mysock.close()
except:
    print("Error retrieving page.")