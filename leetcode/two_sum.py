# Problem
"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""

# My logic in words
"""Will use the two pointer approach, assuming the list is sorted, will have the first pointer at the
right and the other at the left, and we will increament or decreament those depending on the sum result
until we get the target sum and them return the indices of the integers in the list.

"""

# Code Solution
class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pnt_1 = 0
        pnt_2 = len(nums) -1
        while pnt_1 != pnt_2:
            print(pnt_1, pnt_2)
            _sum = nums[pnt_1] + nums[pnt_2]
            if _sum == target:
                return [pnt_1, pnt_2]
            elif _sum > target:
                pnt_2 = pnt_2 - 1
            else:
                pnt_1 = pnt_1 + 1
        return

#test
my_class = Solution()
my_class.twoSum([2,7,11,15], target=9)
