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

#3. Modify the convert.py program with a loop so that it executes 5 times
#   before quitting. 

def main():

    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32  
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    
main()

#4. Modify the convert.py program so that it computes and prints a table of
#   Celsius temperatures and the Fahrenheit equivalents every 10 degrees 
#   from 0C to 100C.

def main():

    for i in range(11):
        celsius = i*10
        fahrenheit = 9/5 * celsius + 32  
        print("Celsius: ", celsius, " Fahrenheit: ", fahrenheit)
    
main()

#5. Modify the futval.py program so that the number of years for the investment
#   is also a user input. 

def main():
    print(
    "This program calculates the future value of an investment given time"
    )
    
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years for the investment: "))
    
    for i in range(years):
        principal = principal * (1+apr)
        
    print("The value in ", years, " years is:", principal)
    
main()
    

#6. Modify futval.py to account for adding a fixed amount to be invested each
#   year. Inputs will be amount to invest each year, interest rate, and time.

def main():
    print(
    "This program calculates the future value of an investment given time")
    print("and fixed contributions.")
    
    yearly_amt = eval(input("Enter the yearly contributions: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years for the investment: "))
    investment_amt = 0
    
    for i in range(years):
        investment_amt = (investment_amt+yearly_amt) * (1+apr)
        
    print("The value in ", years, " years is:", investment_amt)
    
main()

#7. Modify the futval.py program to use compounding periods. 
    
    

    
    