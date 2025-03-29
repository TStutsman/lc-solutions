from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = 0
        i = 0
        while i+2 < len(cost):
            if cost[i] + cost[i+2] > cost[i+1]:
                i += 1
            
            total += cost[i]
            i += 1

        if i == len(cost) - 2:
            total += min(cost[i], cost[i+1])
        
        return total