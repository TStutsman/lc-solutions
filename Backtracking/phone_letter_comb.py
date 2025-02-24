class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

        res, comb = [], []

        def dfs(digit_idx: int) -> None:
            if digit_idx >= len(digits):
                res.append("".join(comb))
                return
            
            for l in letters[digits[digit_idx]]:
                comb.append(l)
                dfs(digit_idx + 1)
                comb.pop()
        
        if digits:
            dfs(0)
        return res
