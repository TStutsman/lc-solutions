class Solution:
    def isValid(self, s: str) -> bool:
        # stack of opening, pop when closed
        # if closed doesn't match pop, return false
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack or pairs[char] != stack.pop():
                    return False

        return not stack