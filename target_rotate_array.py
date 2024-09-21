class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] < target:
                # check to the right
                if nums[r] >= target or nums[m] > nums[r]:
                    # right subarray
                    l = m + 1
                else:
                    # left subarray
                    r = m - 1
            elif nums[m] > target:
                # check to the left
                if nums[l] <= target or nums[m] < nums[l]:
                    # left subarray
                    r = m - 1
                else:
                    # right subarray
                    l = m + 1
            else:
                return m

        return l if nums[l] == target else -1
