#!/usr/bin/env python3

import sys

def find_max(array:list) -> int:
    maximum = array[0]
    for i in array[1:]:
        if i > maximum:
            maximum = i
    return maximum

def find_min(array:list) -> int:
    minimum = array[0]
    for i in array[1:]:
        if i < minimum:
            minimum = i
    return minimum

try:
    argument = sys.argv[1]

    array = [int(i) for i in argument.split(',')]

    print([find_max(array), find_min(array)])

except IndexError:
    print('This script requires an argument in the form of a list of numbers separated by commas with no spaces.\nexample: ./maxmin.py 1,2,3,4,5,6')

except ValueError as error:
    print(f"Invalid input ({argument}). Check that you are only passing one argument.\nError: {error}")