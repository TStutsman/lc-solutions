class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        t, b = 0, len(matrix)

        l, r = 0, len(matrix[0])

        while not (t >= b and l >= r):
            y = (b + t) // 2
            
            x = (l + r) // 2

            # print(t, b, l, r, y, x, matrix[y][x])

            if matrix[y][x] > target:
                if matrix[y][0] > target:
                    b = y - 1
                    r = len(matrix[0])
                elif matrix[y][0] < target:
                    if t != b:
                        l = 0
                    t, b = y, y
                    r = x
                else:
                    return True

            elif matrix[y][x] < target:
                if matrix[y][-1] < target:
                    t = y + 1
                    l = 0
                elif matrix[y][-1] > target:
                    if t != b:
                        r = len(matrix[0])
                    t, b = y, y
                    l = x + 1
                else:
                    return True

            else:
                return True
            
        return False