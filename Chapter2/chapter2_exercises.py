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

#2. Modify the avg2.py program to find the average of three exam scores.

def main():
    print("This program comptues the average of three exam scores.")
    
    score1, score2, score3 = eval(input(
    "Enter three scores separated by a comma: "
                                        ))
    average = (score1 + score2 + score3) / 3
    
    print("The average of the scores is:", average)

main()

#3. 
    
    