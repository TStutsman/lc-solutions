class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # left, middle, right pointers at 0, 1, n-1
        # while left < right - 1
            # for each middle between left and right
                # check if zero
            # increment left
                # repeat above
            # decrement right
                # repeat above

        left = 0
        triplets = {}

        def checkZero(left, right):
            target = 0 - (nums[left] + nums[right])
            for i in range(left + 1, right):
                if nums[i] == target:
                    t_sort = sorted([nums[left], nums[i], nums[right]])
                    t_str = ','.join([str(n) for n in t_sort])
                    triplets[t_str] = [nums[left], target, nums[right]]

        
        while left < len(nums) - 2:
            right = left + 2
            while right < len(nums):
                checkZero(left, right)
                right += 1
            left += 1
        
        return list(triplets.values())