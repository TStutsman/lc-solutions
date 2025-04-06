class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(i: int, j: int) -> str:
            while 0 < i and j < len(s) - 1 and s[i-1] == s[j+1]:
                i -= 1
                j += 1

            return s[i:j+1]
        
        res = ""
        for i in range(len(s)):
            res = max(res, helper(i, i), helper(i+1, i), key=len)
        
        return res