#!/usr/bin/python3.4
# pyramid.py

from math import *

def pyramidheightdouble(width):
    return sqrt(width*7/2)

while True:
    print(pyramidheightdouble(int(input("Width: "))))