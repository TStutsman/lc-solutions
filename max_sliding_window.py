class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # ordered list of window
        # insertion sort each new number O(k)
        # remove number leaving window O(k)

        # O(n^2)
        # grab max O(1)
        # slide window O(1)
        # - remove left O(k)
        # - add right O(k)

        # O(nk - k^2) good for bigger k
        # find max O(k)
        # store max and max_index O(1)
        # looping over array O(n)
        # check if new value is greater than max O(1)
        # if max_index passes out of range O(n-k)
        # - find new max O(k)

        def find_new_max(nums, l, r):
            new_max = -1001
            new_idx = 0
            for idx in range(l, r):
                if nums[idx] > new_max:
                    new_max = nums[idx]
                    new_idx = idx
            return new_max, new_idx

        max_num, max_idx = find_new_max(nums, 0, k)
        res = [max_num]
        
        for idx in range(k, len(nums)):
            # Check if new num is max
            if nums[idx] > max_num:
                max_num = nums[idx]
                max_idx = idx

            # If old max is out of range, find new max
            if max_idx == idx - k:
                max_num, max_idx = find_new_max(nums, idx - k + 1, idx + 1)
            
            res.append(max_num)
        
        return res

        # O(n^2) optimized for larger k
        # sort whole array descending O(nlogn)
        # replace nums with original indeces
        # for i < n - k + 1 O(n - k)
        # - for index in sorted_indeces O(n - k)
        # - - if i - k < index < i + k