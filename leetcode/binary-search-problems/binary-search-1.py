# Linear search could as well be used, with time complexity of <Log(n)>

"""
LOGIC:
Let target be x
Compare x with the middle element.
If x matches with the middle element, we return the mid index.
Else If x is greater than the mid element, then x can only lie in the right half subarray after the mid element.
So we recur for the right half.
Else (x is smaller) recur for the left half.
"""

"""
PROBLEM: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function
to search target in nums. If target exists, then return its index. Otherwise, return -1. You must write an algorithm
with O(log n) runtime complexity.
"""


# SOLUTION

def find_middle(input_list: list):
    middle = float(len(input_list)) / 2
    if middle % 2 != 0:
        return input_list[int(middle - .5)]
    else:
        return input_list[int(middle)], input_list[int(middle - 1)]


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pass


int_list = [-1, 0, 3, 5, 9, 12, 15]
print(find_middle(int_list))
