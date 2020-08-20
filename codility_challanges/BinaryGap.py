#!/bin/python3
# Author: Sebastian Opiyo
# Date Created: Aug 19, 2020
# Date Modified: Aug 20, 2020
# Description: Algorithm challenges Lesson 1: Iterations.
"""
--> Algorithm flow
def solution(n):
    Validate for the correct value of n
    Convert the +v int into binary
    determine max zero_counter
    Check the max num of zeros within 1's by splitting the binary
    return the max num if existing otherwise return 0
"""


# Solution 1: Best solution with 100% correctness.
def solution(n):
    """
        Determines the maximal 'binary gap' in an integer
        :param n: a positive integer (between 1 and 2147483647)
        :return: a count of the longest sequence of zeros in the binary representation of the integer
    """
    bin_limit = 2147483647
    if not isinstance(n, int):
        raise TypeError("Only positive integer values accepted!")

    if 1 > n:
        raise ValueError("Only positive values less than 2,147,483,647 are accepted!")

    if n > bin_limit:
        raise ValueError("Integer beyond limit!")

    binary_num = f'{n:b}'.strip('0')
    list_of_zeros = binary_num.split('1')
    max_value = len(max(list_of_zeros))
    if max_value == '':
        return 0
    else:
        return max_value


# Helper code:
print(solution(12098))
