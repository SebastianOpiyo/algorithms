class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        pnt_1 = 0
        pnt_2 = 0

        while pnt_2 < len(s):
            if s[pnt_2] not in s[pnt_1:pnt_2]:
                pnt_2 += 1
                temp_max = len(s[pnt_1:pnt_2])
                max_size = max(max_size, temp_max)
                print(s[pnt_1:pnt_2])
            else:
                pnt_1 += 1
        return max_size
        
new_string = Solution()
print(new_string.lengthOfLongestSubstring("abcabcbb"))
