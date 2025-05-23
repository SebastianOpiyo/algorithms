"""Given an integer x, return true if x is a

, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

 

Constraints:

    -231 <= x <= 231 - 1

 
Follow up: Could you solve it without converting the integer to a string?"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        n % 10 == 0 → number ends with zero.

        Numbers ending with zero cannot be palindromes (unless the number is exactly zero).
        This is because reversing them would produce a number with leading zeros, which are dropped in integers.
        So the check is a quick early exit to improve correctness and efficiency.
        '''
        if x < 0 or (x % 10 == 0 and x !=0):
            return False
        return True if str(x) == str(x)[::-1] else False
    
    
    # Solution 2 (No string conversion)
    def isPalindrome2(self, x: int) -> bool:
        '''Second best solution.'''
        # Check if a number is negative
        
        if x < 0 or (x % 10==0 and x != 0):
            return False
        
        reversed_num = None
        original_num = x
        while x > 0:
            num_digits = x % 10
            x //= 10
            reversed_num = (reversed_num or 0) * 10 + num_digits
        if reversed_num == original_num:
            return True
        return False
    
    
    
    
def digits(x: int) -> int:
    """Count the number of digits in an int"""
    reversed_num = None
    digits_count = 0
    while x > 0:
        num_digits = x % 10
        x //= 10
        digits_count +=1
    return digits_count


if __name__ == "__main__":
    # print(digits(1234567890))
    x = 121
    print(Solution().isPalindrome2(x))
    # print(Solution().isPalindrome(x))
    # x = -121
    # print(Solution().isPalindrome2(x))
    # print(Solution().isPalindrome(x))
    # x = 10
    # print(Solution().isPalindrome2(x))
    # print(Solution().isPalindrome(x))
    