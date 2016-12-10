# -*- coding: utf-8 -*-
"""
Solutions to Programming Exercises for Chapter 2
"""

# 1. Modify the convert.py program to print an introduction

def main():
    print("This program will convert Celsius to Fahrenheit.")
    print("You will be prompted to enter the temperature in Celsius.")
    print("Type in the temperature and press enter.")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()

