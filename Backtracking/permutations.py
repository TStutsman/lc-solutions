class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # O(n! * n) space
        res = []

        # O(n! * n)
        # dfs is called n! times to produce all perms
        def dfs(idx: int, curr: List[int]) -> None:
            if idx == len(nums):
                res.append(curr)
                return
            
            # O(1)
            curr.append(nums[idx])

            # recur original order
            dfs(idx + 1, curr.copy())

            # O(n) time for iteration
            # swap position with every element in curr
            for i in range(idx):
                # swap
                curr[i], curr[-1] = curr[-1], curr[i]
                # recur
                dfs(idx + 1, curr.copy())
                # swap back
                curr[i], curr[-1] = curr[-1], curr[i]
        
        dfs(0, [])

        return res
