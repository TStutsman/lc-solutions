from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 4:
            return max(nums)

        m1 = [0,nums[0]]
        m2 = [0,0]

        for house in range(1, len(nums)):
            tmp = max(m1[0] + nums[house], m1[1])
            m1[0] = m1[1]
            m1[1] = tmp

            tmp = max(m2[0] + nums[house], m2[1])
            m2[0] = m2[1]
            m2[1] = tmp

        return max(m1[0], m2[1])