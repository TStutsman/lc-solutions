# class Solution:
#     def generateParenthesis(self, n: int) -> list[str]:
#         res = []
#         stack = ['()']
#         visited = set()
#         while stack:
#             curr = stack.pop()
#             if len(curr) < 2 * n:
#                 outside = '(' + curr + ')'
#                 stack.append(outside)
#                 visited.add(outside)

#                 right = curr + '()'
#                 stack.append(right)
#                 visited.add(right)

#                 left = '()' + curr
#                 if left not in visited:
#                     stack.append(left)
#                     visited.add(left)
#             else:
#                 res.append(curr)
        
#         return res

from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # while queue
        # pop first in queue
        # if first is 2n length return queue as list
        # if open count is less than n
        # - push curr + (
        # if open count is greater than closed count
        # - push closed + )

        queue = deque([('(', 1, 0)])

        while queue:
            if len(queue[0][0]) == 2 * n:
                break

            curr, open_count, closed_count = queue.popleft()
            
            if open_count < n:
                queue.append((curr + '(', open_count + 1, closed_count))

            if open_count > closed_count:
                queue.append((curr+')', open_count, closed_count + 1))


        return [string for string, _, _ in list(queue)]