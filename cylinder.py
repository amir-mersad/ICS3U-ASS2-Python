#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program calculates the perimeter of a cylinder

import math


def main():
    # This function calculates the perimeter of a cylinder

    # Input
    radius = int(input("Please enter the radius of the cylinder(mm): "))

    # Process
    perimeter = radius * math.pi * 2

    # Output
    print("The perimeter of the cylinder is : {0:,.2f}mm^2".format(perimeter))


if __name__ == "__main__":
    main()
