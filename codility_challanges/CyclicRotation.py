#!/bin/python3
# Author: Sebastian Opiyo
# Date Created: Aug 20, 2020
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


def solution(a: list, k: int):
    """
        Rotate an array to the right k steps.
        :param a: an array of integers
        :param k: number of times to shift to cycle the list
        :return: an array of reverser ints after k cycles
    """
    # if not a:
    #     raise IndexError("Empty List!")

    if not len(a):
        return a

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
    return new_list


# Helper Code
array = [0, 0, 0]
iterator_num = 3
print(solution(array, iterator_num))
