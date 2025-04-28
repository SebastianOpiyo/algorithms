'''
You are given an integer n.

Each number from 1 to n is grouped according to the sum of its digits.

Return the number of groups that have the largest size.

 

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.

Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.

 

Constraints:

    1 <= n <= 104

'''
class Solution:
    """Second Optimized Solution."""
    def countLargestGroup(self, n: int) -> int:
        pass





class SolutionOne:
    def countLargestGroup(self, n: int) -> int:
        dict_n = {}
        int_range = [i for i in range(1, n+1)]
        # print(int_range)
        
        # start adding from 1 to n
        for i in range(1, n+1):
            # split an int into a list of respective digits
            num_split = [int(x) for x in str(i)]   # this operation takes O(n)
            # print(num_split)
            
            # Check if the sum of digits exists in the number list and in the dictionary
            if sum(num_split) in int_range and sum(num_split) in dict_n:
                dict_n[sum(num_split)].append(i)
            else:
                dict_n[sum(num_split)] = [i]
        
        # Get the groups with the largest size
        sum_of_largest = 0
        total_largest = 0
        for k, v in dict_n.items():
            if len(v) > sum_of_largest:
                sum_of_largest = len(v)
                total_largest = 1
            elif len(v) == sum_of_largest:
                total_largest += 1
            else:
                pass
        return total_largest



Solution = Solution()

print(Solution.countLargestGroup(13))






