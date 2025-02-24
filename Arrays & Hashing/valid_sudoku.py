class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        # O(n) time and space complexity

        for i, row in enumerate(board):
            for j, square in enumerate(row):
                if square == ".":
                    continue

                box = j // 3 + (i // 3) * 3
                
                # check row, column, box
                if square in rows[i] or square in cols[j] or square in boxes[box]:
                    return False
                
                rows[i].add(square)
                cols[j].add(square)
                boxes[box].add(square)
                    

        return True