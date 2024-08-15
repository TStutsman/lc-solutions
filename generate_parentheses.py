class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = ['()']
        visited = set()
        while stack:
            curr = stack.pop()
            if len(curr) < 2 * n:
                outside = '(' + curr + ')'
                stack.append(outside)
                visited.add(outside)

                right = curr + '()'
                stack.append(right)
                visited.add(right)

                left = '()' + curr
                if left not in visited:
                    stack.append(left)
                    visited.add(left)
            else:
                res.append(curr)
        
        return res