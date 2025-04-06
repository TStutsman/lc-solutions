class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(idx: int) -> str:
            i, j = idx, idx
            while 0 < i and j < len(s) - 1 and s[i-1] == s[j+1]:
                i -= 1
                j += 1
            
            pal = s[i:j+1]

            i, j = idx+1, idx
            while 0 < i and j < len(s) - 1 and s[i-1] == s[j+1]:
                i -= 1
                j += 1
            
            pal2 = s[i:j+1]

            return max(pal, pal2, key=len)
        
        res = ""
        for i in range(len(s)):
            res = max(res, helper(i), key=len)
        
        return res