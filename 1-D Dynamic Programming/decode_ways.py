class Solution:
    def numDecodings(self, s: str) -> int:
        # Subproblem: suffix of s[i]
        # Relation: S(i) = S(i+1) + S(i+2) if 11-19,21-26 else S(i+1)
        # Topo Ord: n, n-1, ... 0
        # Base: S(n) = 0
        # Original: S(0)
        # Time: O(n)

        if s[0] == '0':
            return 0

        opn, cls = 1, 0
        for i in range(len(s)-1, -1, -1):
            if i < len(s) - 1 and s[i+1] == '0':
                if not '0' < s[i] < '3':
                    return 0
                continue
            if i < len(s) - 2 and s[i+2] == '0':
                continue

            sub = s[i:i+2]
            if '10' < sub <= '19' or '20' < sub <= '26':
                tmp = opn
                opn = opn + cls
                cls = tmp
            else:
                opn = opn + cls
                cls = 0
        
        return opn + cls