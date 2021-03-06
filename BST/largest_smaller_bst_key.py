#!/bin/python3
# Author: Sebastian Opiyo
# Date Created: August 26, 2020
# Date Modified: August 26, 2020
# Description: bst challenge, Python3 Version.

"""
Problem: Given an int value, find smaller values of it from the bst,
from the smaller values, find the largest. If non exists, return -1

algo:
- start from root node
- s = -1
- repeat -- until leaf while (node):
    - if num > node.key:
        - s = node.key
        - go to left // node = node.right 
    - else:
        - go to the left // node = node.left
- return s
"""

from samples.commons.python import bst


def largest_smaller_key(tree: bst, num):
    node = tree.root
    print(node.key)
    print(f'Confirm {node.key} is root: {node.is_root()}')
    smaller = -1

    while node:
        if num > node.key:
            smaller = node.key
            node = node.right_child
        else:
            node = node.left_child
    return smaller

    # print(node)


# Helper code for tests.
let_arr = [20, 9, 25, 5, 12, 11, 14, 18, 19]
my_bst = bst.BST()
my_bst.create_bst_from_list(let_arr)
# test if the bst works ok.
# print(my_bst.__contains__(5))
# print(my_bst[0])
# print(my_bst[5])
# print(my_bst.postorder())
# largest = largest_smaller_key(my_bst, 20)  # 19
# largest = largest_smaller_key(my_bst, 5)  # -1
# largest = largest_smaller_key(my_bst, 17)  # 14
largest = largest_smaller_key(my_bst, 23)  # 20
# largest = largest_smaller_key(my_bst, 30)  # 25
print(f'The largest of the smallest is: {largest}')

"""
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

max_length = 1000000

def solution(a: list):
    # write your code in Python 3.6
    # checking whether a is an array of integers.
    if not len(a):
        raise ValueError("Empty list, need a list with odd number of elements")

    if len(a) > max_length:
        raise ValueError("Error, length beyond required threshold!")

    if not isinstance(a, list):
        raise TypeError("Input must be a list of integers")

    for i in a:
        if not isinstance(i, int):
            raise TypeError("Error, only integer values accepted!")

    elements_dict = {}

    for elem in a:
        if elements_dict[elem]:
            del elements_dict[elem]
        raise KeyError("Error, Element doesn't exist!")
        elements_dict[elem] = True

    if len(unmatched) == 1:
        return unmatched.keys()[0]
"""
