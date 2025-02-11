class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        partitions = []

        # dfs(window_pointers) to keep/remove first letter in window
            # base case -> if left >= len(s) (window exits string indeces)
                # res.append(partitions)
                # return

            # check if substring is palindrome
                # if pali, add to partitions list -> shift left to right
                    # partitions.append(s[left:right])
                    # dfs(right, right + 1) recur to next character after pali
                    # partitions.pop()

            # dfs(left, right + 1) recur

        def dfs(l: int, r: int) -> None:
            if l >= len(s):
                res.append(partitions.copy())
                return
            if r > len(s):
                return
            
            if is_pali(s[l:r]):
                partitions.append(s[l:r])
                dfs(r, r + 1)
                partitions.pop()

            dfs(l, r + 1)

        def is_pali(s: str) -> bool:
            for i in range(len(s) // 2):
                if s[i] != s[-1-i]:
                    return False
            return True

        dfs(0,1)

        return res
