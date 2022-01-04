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
# - This problem can be solved either recursively or iteratively.



class Solution:
    """A Binary Search class with recursive and iterative solutions."""

    def __init__(self, nums:list[int], target:int):
        self.nums = nums
        self.target = target

    # Recursive solution.
    def recursive_solution(self, right:int, left:int):
        # left should always be less or equal to the right
        if left > right:
            return False
        # We find the mid
        else:
            mid = (left + right)/2
            if self.target == self.nums[mid]:
                return mid
            else:
                # check if in the left or right half
                pass

    # Iterative solution.
    def iterative_solution(self):
        pass

    def find_middle(input_list: list):
        middle = float(len(input_list)) / 2
        if middle % 2 != 0:
            return input_list[int(middle - .5)]
        else:
            return input_list[int(middle)], input_list[int(middle - 1)]

    def search(self, nums: list[int], target: int) -> int:
        pass


# TEST RUN
# int_list = [-1, 0, 3, 5, 9, 12, 15]
# print(find_middle(int_list))
