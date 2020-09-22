#!/bin/python3
# Author: Sebastian Opiyo
# Date Created: Aug 20, 2020
# Date Modified: Aug 20, 2020
# Description: Algorithm challenges Lesson 2: Arrays.

"""
--> Algorithm Attempt flow
def solution(a):
    Validate for a non-empty list with a max length of 1000000
    validate for int values only

"""

max_length = 1000000


def solution(a: list):
    # write your code in Python 3.6
    # checking whether a is an array of integers.
    if not len(a) > 1:
        raise IndexError("Empty list, need a list with odd number of elements")

    if len(a) > max_length:
        raise ValueError("Error, length beyond required threshold!")
    # We don't need this because the list is checked at the parameter entry level.
    # if not isinstance(a, list):
    #     raise TypeError("Input must be a list of integers")

    for i in a:
        if not isinstance(i, int):
            raise TypeError("Error, only integer values accepted!")
        if i not in range(1000000):
            raise ValueError("Error, value out of range!")

    odd_elem_counter = {}

    for elem in a:
        if elem in odd_elem_counter:
            del odd_elem_counter[elem]
        else:
            odd_elem_counter[elem] = True
    # returns a list, but that is not really needed ...just the value.
    return [print(key, value) for key, value in odd_elem_counter.items()]


array = [9, 3, 9, 3, 9, 7, 9]
solution(array)
