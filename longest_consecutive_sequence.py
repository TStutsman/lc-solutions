class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # for each element check all elements if e + 1 exists
        # O(n^2)

        # make an array of all elements and count the number of sequential elements
        # O(10^9)

        # set of existing elements O(n)
        # for each element in the set O(n)
        # check if element + 1 exists
        # check if current count is greater than max count

        unique_nums = set(nums)

        max_count = 0
        for num in list(unique_nums):
            if num - 1 in unique_nums: continue

            curr_num = num
            curr_count = 0
            while curr_num in unique_nums:
                curr_count += 1
                curr_num += 1

            max_count = max(curr_count, max_count)

        return max_count