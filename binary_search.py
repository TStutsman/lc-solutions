class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r = 0, len(nums)

        while l < r:
            m = (r + l) // 2

            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m
        
        return -1