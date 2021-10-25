# Problem
"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""

# My logic in words
"""I will use binary tree approach, and that will improve time complexity
from O(n^2) to log(n)
- Create a tree using the list and then recursively do the addition,
until the target is hit, at that point we stop and return the value of 
the two variables as a list of ints
"""

# Code Solution
class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # create a binary tree from the list
        # traverse the tree adding up numbers from the root
        # on hitting the target stop
        # return the two operands as a list
        pass
