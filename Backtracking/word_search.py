class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # Neighbor helper function
	def get_neighbors(x, y) -> list[tuple[int, int]]:
            res = []

            if x > 0:
                res.append((x - 1, y))
            
            if x < len(board) - 1:
                res.append((x + 1, y))

            if y > 0:
                res.append((x, y - 1))

            if y < len(board[0]) - 1:
                res.append((x, y + 1))
            
            return res
        
	# recursive dfs to find next letter of word
        def dfs(root: tuple[int, int], visited: set[tuple[int, int]]) -> bool:
            x, y = root
            if board[x][y] == word[len(visited)]:
                if len(visited) == len(word) - 1:
                    return True

                visited.add(root)

                neighbors = get_neighbors(x, y)
                for neighbor in neighbors:
                    if neighbor in visited:
                        continue
                    if dfs(neighbor, visited):
                        return True

                visited.discard(root)
            
            return False
        
	# iterate through all letters in board
        for row in range(len(board)):
            for col in range(len(board[row])):
                if dfs((row, col), set()):
                    return True
        
        return False
