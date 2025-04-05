from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        one, two, three = nums[0], nums[1], nums[0] + nums[2]

        for house in range(3, len(nums)):
            tmp = three
            three = max(one, two) + nums[house]
            one = two
            two = tmp
        
        return max(two, three)