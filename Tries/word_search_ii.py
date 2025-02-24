class TrieNode:
    def __init__(self):
        self.next = {}
        self.eow = None

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        res = set()

        # trie of words to search
        root = TrieNode()

        for word in words:
            curr = root
            for letter in word:
                if letter not in curr.next:
                    curr.next[letter] = TrieNode()
                curr = curr.next[letter]
            curr.eow = word

        # for every tile in board
        for row in range(len(board)):
            for col in range(len(board[row])):
                # dfs search word trie
                stack = [(root,row,col)]
                visited = set()

                while stack:
                    curr,r,c = stack.pop()

                    if r < 0 or c < 0 or r >= len(board) or c >= len(board[r]):
                        continue

                    if (r,c) in visited:
                        continue

                    if board[r][c] not in curr.next:
                        continue

                    curr = curr.next[board[r][c]]

                    if curr.eow:
                        res.add(curr.eow)
                    
                    if not curr.next:
                        continue
                    
                    visited.add((r,c))

                    stack.append((curr,r+1, c))
                    stack.append((curr,r-1, c))
                    stack.append((curr,r, c+1))
                    stack.append((curr,r, c-1))


        return list(res)