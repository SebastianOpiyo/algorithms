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

def list_hasmap(nums:list, target:int) -> list:
    hashmap = {}
    # Check if there exists two numbers that add up to target
    for i, val in enumerate(nums):
        rem = target - val
        if rem in hashmap[val]:
            return [hashmap[val],i]
        hashmap[val] = i
    return []

print(list_hasmap([2,7,11,15], target=9))


# Previous Solution
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hashmap = {val:i for i, val  in enumerate(nums)}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hashmap and hashmap[rem] != i:
                return [hashmap[rem], i]
            else:
                hashmap[rem] =i
        return []
