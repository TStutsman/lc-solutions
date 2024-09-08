# class Solution:
#     def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
#         t, b = 0, len(matrix)

#         l, r = 0, len(matrix[0])

#         while not (t >= b and l >= r):
#             y = (b + t) // 2
            
#             x = (l + r) // 2

#             # print(t, b, l, r, y, x, matrix[y][x])

#             if matrix[y][x] > target:
#                 if matrix[y][0] > target:
#                     b = y - 1
#                     r = len(matrix[0])
#                 elif matrix[y][0] < target:
#                     if t != b:
#                         l = 0
#                     t, b = y, y
#                     r = x
#                 else:
#                     return True

#             elif matrix[y][x] < target:
#                 if matrix[y][-1] < target:
#                     t = y + 1
#                     l = 0
#                 elif matrix[y][-1] > target:
#                     if t != b:
#                         r = len(matrix[0])
#                     t, b = y, y
#                     l = x + 1
#                 else:
#                     return True

#             else:
#                 return True
            
#           return False

# class Solution:
#     def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

#         def searchRow(row: list[int], target: int) -> bool:
#             l, r = 0, len(row)
#             while r > l:
#                 m = (r - l) // 2
#                 if target > row[m]:
#                     l = m + 1
#                 elif target < row[m]:
#                     r = m
#                 else:
#                     return True
#             return False

#         t, b = 0, len(matrix)
#         while b > t:
#             c = (b - t) // 2
#             if matrix[c][0] > target:
#                 b = c
#             elif matrix[c][-1] < target:
#                 t = c
#             else:
#                 print(matrix[c])
#                 return searchRow(matrix[c], target)
        
#         return False

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # fold it in half
        h, w = len(matrix), len(matrix[0])
        l, r = 0, h * w

        while r > l:
            row = (r + l) // 2 // w
            col = (r + l) // 2 % w

            if target > matrix[row][col]:
                l = row * w + col + 1
            elif target < matrix[row][col]:
                r = row * w + col
            else:
                return True
        
        return False