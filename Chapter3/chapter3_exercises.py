#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:28:47 2016

@author: davidrusso
"""

# 1. Write a program to calculate the volume and surface area of a sphere
#    given radius as an input

import math

def main(rad):
    
    vol = round((4/3)*math.pi*rad**3, 2)
    area = round(4*math.pi*rad**2, 2)
    
    print("Given a radius of", rad, "the volume of the sphere is", vol)
    print("and the area of the sphere is", area)

main(rad = 3)

#2. Write a program that calculates the cost per square inch of a circular 
#   pizza given its diameter and price


def main(diameter, price):
    
    radius = diameter / 2
    area = math.pi*radius**2
    cost_per_square_inch = round(price / area, 3)
    
    print("Given a diameter of",diameter,"inches and a price of $",price,"dollars")
    print("The cost per square inch of the pizza is", cost_per_square_inch)
    print("dollars per square inch.")
    
main(14, 20)

#3. Write a program that calculates the molecular weight of a hydrocarbon
#   given the number of hydrogen, oxygen, and carbon molecules.

def main(nH, nC, nO):
    
    mol_weight = round(nH*1.0079 + nC*12.011 + nO*15.9994, 4)
    print("The molecular weight of a hydrocarbon with", nH, "hydrogens")
    print("and", nC, "carbons and", nO, "oxygens is", mol_weight)
    
main(6, 2, 1)

#4. Write a program that determines the distance to a lightning strike based
#   on the time elapsed between the flash and the sound of thunder. 

def main(seconds):
    
    dist_ft = seconds*1100
    dist_miles = round(dist_ft/5280, 3)
    
    print("The lightning strike is", dist_miles, "miles away.")

main(2)

#5. The Konditorei coffee shop sells coffee at $10.50 per pound plus the cost
#   of shipping. Each order ships for $0.86 per pound + $1.50 fixed cost for 
#   overhead. Write a program that calculates the cost of an order.

def main(lbs):
    
    coffee_cost = 10.50*lbs
    shipping_cost = 0.86*lbs + 1.50
    
    total_cost = round(coffee_cost + shipping_cost, 2)

    print("Your order was", lbs, "pounds. The cost is", total_cost, "dollars.")

main(10)

#6. Write a program that calculates the slope of the line through two
#   non vertical points specified by the user.

def main(x1, y1, x2, y2):
    m = round((y2-y1)/(x2-x1), 3)
    
    print("The slope of the line through (", x1, y1, ") and (", x2, y2, ") is")
    print(m)

main(5, 10, 15, 40)

#7. Write a program that calculates the Euclidean distance between two points.

def main(x1, y1, x2, y2):
    
    dist = round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 2)
    
    print("The distance between the point (", x1, y1, ") and (", x2, y2, ")")
    print("is", dist, "units.")
    
main(5, 2, 7, 8)


    




    