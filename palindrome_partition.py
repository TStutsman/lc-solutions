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
                    # partitions.append(s[left:right + 1])
                    # dfs(right + 1, right + 1) recur
                    # partitions.pop()
            # always continue to next letter
            # dfs(left, right + 1) recur
            # remove first letter and add to partitioned list
            # partitions.append(s[left])
            # dfs(left + 1, right) recur

        def dfs(l: int, r: int) -> None:
            if r > len(s) or l >= r:
                return
            
            print(partitions, s[l:r])
            if is_pali(s[l:r]):
                partitions.append(s[l:r])
                if r >= len(s):
                    res.append(partitions.copy())
                dfs(r, r + 1)
                partitions.pop()

            dfs(l + 1, r)
            dfs(l, r + 1)

        def is_pali(s: str) -> bool:
            for i in range(len(s) // 2):
                if s[i] != s[-1-i]:
                    return False
            return True

        dfs(0,1)

        return res
