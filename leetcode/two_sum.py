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


# I coded this solution a while ago, need to do comparison
class SolutionOne:
    def twoSum(self, nums: list, target: int) -> list:
        existing = {}
        for i in range(len(nums)):
            required_num = target - nums[i]
            if required_num in existing:
                return [i, existing[required_num]]
            else:
                existing[nums[i]] = i
        return []
    
    
# My third Solution, using hashmap
# The solution beats 53% of the solutions, still needs optimization
'''
Algorithm
We are looking for two elems in the list, when summed equal the target.
1. Create a hashtable of the elements in the list with element as key and index as value
2. pick the first elem in the list and sub from target to get rem
3. check to see of the rem exists in the dictionary and its index is greater than current iteration
4. if its true return index of the elem

Time Complexity: O(nlog(n))
'''
def list_hasmap(lst:list, target:int) -> list:
    hashmap = {val:i for i, val  in enumerate(lst)}
    for i in range(len(lst)):
        rem = target - lst[i]
        if rem in hashmap and hashmap[rem] != i:
            return [hashmap[rem], i]
    return []

print(list_hasmap([1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1], target=11))
