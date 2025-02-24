class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [[]]

        def recursive_add_subset(curr_idx: int, acc: list[int]) -> None:
            nonlocal res
            res.append(acc)

            for next_idx in range(curr_idx + 1, len(nums)):
                recursive_add_subset(next_idx, acc + [nums[next_idx]])

        for idx in range(len(nums)):
            recursive_add_subset(idx, [nums[idx]])

        return res