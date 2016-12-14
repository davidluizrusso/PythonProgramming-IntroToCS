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




    