'''
3550. Smallest Index With Digit Sum Equal to Index
Difficulty: Easy

You are given an integer array nums.

Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

If no such index exists, return -1.'''



class Solution:
    
    def smallestIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if sum(int(x) for x in str(nums[i])) == i:
                return i
        return -1
            
