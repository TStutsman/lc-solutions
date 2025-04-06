class Solution:
    def numDecodings(self, s: str) -> int:
        # Subproblem: suffix of s[i]
        # Relation: S(i) = S(i+1) OR S(i+1) + 1
        # Topo Ord: n, n-1, ... 0
        # Base: S(n) = 0
        # Original: S(0)
        # Time: O(n)

        if s[0] == '0':
            return 0

        # [1,0,1,2] = if i + 2 >= 4

        count = 0 if s[-1] == '0' else 1
        for i in range(len(s)-2, -1, -1):
            if s[i] == '0':
                count -= 1
            if i + 2 >= len(s) or s[i+2] != '0':
                if s[i] == '1' or 20 <= int(s[i:i+2]) <= 26:
                    count += 1
        
        return count