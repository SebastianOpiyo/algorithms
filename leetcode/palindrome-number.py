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
    def ispalindrome2(self, x: int) -> bool:
        # Check if a number is negative
        if x < 0 or (x % 10 and x != 0):
            return False
        
        return
    

def digits(x: int) -> int:
    """Count the number of digits in an int"""
    
    while x > 0:
        num_digits = x % 10
        num_digits = x // 10
        return len(str(num_digits))



if __name__ == "__main__":
    print(digits(1234567890))
    # x = 121
    # print(Solution().isPalindrome(x))
    # x = -121
    # print(Solution().isPalindrome(x))
    # x = 10
    # print(Solution().isPalindrome(x))