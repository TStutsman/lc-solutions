from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_copies = {}

        def dfs(node:Optional['Node']) -> Optional['Node']:
            if not node:
                return None

            copy = Node(node.val, [])
            node_copies[node] = copy

            for neighbor in node.neighbors:
                if neighbor in node_copies:
                    copy.neighbors.append(node_copies[neighbor])
                else:
                    nb_copy = dfs(neighbor)
                    copy.neighbors.append(nb_copy)

            return copy
        
        copy = dfs(node)

        return copy