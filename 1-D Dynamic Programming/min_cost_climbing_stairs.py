from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two, one = cost[-1], cost[-2]

        for stair in range(len(cost) - 3, -1, -1):
            tmp = one
            one = cost[stair] + min(one, two)
            two = tmp

        return min(one, two)