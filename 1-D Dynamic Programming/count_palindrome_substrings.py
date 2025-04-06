class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(i: int, j: int) -> int:
            count = 0
            while -1 < i and j < len(s) and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1

            return count
        
        res = 0
        for i in range(len(s)):
            res += helper(i,i) + helper(i, i+1)
        
        return res