#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 5: Write a program which prompts the user for a Celsius temperature, 
convert the temperature to Fahrenheit, and print out the converted temperature.

Severance, Charles. Python for Everybody: Exploring Data in Python 3 (Kindle 
Locations 575-576). Kindle Edition. 
"""

celcius = float(input("Enter the temperature in celcius: "))
farenheit = round(celcius * 1.8 + 32, 2)
print("The temperature in Farenheit is: ", farenheit)