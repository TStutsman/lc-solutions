class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:

        combination = [[], 0]
        res = []

        def dfs(idx: int):
            if idx >= len(nums):
                return

            print(combination)

            if combination[1] == target:
                res.append(combination[0].copy())
                return

            elif combination[1] > target:
                return

            # add next number
            combination[0].append(nums[idx])
            combination[1] += nums[idx]
            dfs(idx)

            # go back
            combination[0].pop()
            combination[1] -= nums[idx]
            dfs(idx + 1)

        dfs(0)

        return res
