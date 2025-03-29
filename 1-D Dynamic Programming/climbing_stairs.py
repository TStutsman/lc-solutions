class Solution:
    def climbStairs(self, n: int) -> int:
        prev = [1, 1]

        for _ in range(n-1):
            tmp = prev[1]
            prev[1] = prev[0] + prev[1]
            prev[0] = tmp
        
        return prev[1]