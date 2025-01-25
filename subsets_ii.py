class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def dfs(idx: int, curr: List[int]) -> None:
            if idx >= len(nums):
                res.append(curr)
                return

            dfs(idx + 1, curr + [nums[idx]])
            if curr and nums[idx] == curr[-1]:
                return
            dfs(idx + 1, curr.copy())
        
        dfs(0, [])

        return res
