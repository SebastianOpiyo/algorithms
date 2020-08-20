#!/bin/python3
# Author: Sebastian Opiyo
# Date Created: Aug 19, 2020
# Date Modified: Aug 20, 2020
# Description: Algorithm challenges Lesson 1: Arrays.
"""
--> Algorithm Attempt flow
def solution(a, k):
    Validate len a and k values: should be integers from 0..100
    pop the last element in the array and insert as the first
    do that k times
    return final array after k iterations.
"""


class EmptyArray(Exception):
    pass


def solution(a: list, k: int):
    """
        Shift index position of integers in cyclic rotation
        :param a: an array of integers
        :param k: number of times to shift to cycle the list
        :return: an array of reverser ints after k cycles
    """
    if not a:
        raise EmptyArray

    if len(a) > 100:
        raise ValueError("Length beyond required limit!")

    if k < 0:
        raise ValueError("Value range of k is between 0..100")

    if k > 100:
        raise ValueError("Value range of k is between 0..100")

    new_list = a[:]
    for i in range(k):
        last_value = new_list.pop()
        new_list.insert(0, last_value)
    print(new_list)


# Helper Code
array = [1, 3, 4, 6]
iterator_num = 3
solution(array, iterator_num)
