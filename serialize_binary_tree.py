from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # post-order traversal
        post_order = []

        def dfs(root):
            if not root:
                post_order.append('x')
                return

            dfs(root.left)
            dfs(root.right)
            post_order.append(str(root.val))
        
        dfs(root)
        return ",".join(post_order)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        post_order = data.split(',')
        children = []

        for val in post_order:
            if val == 'x':
                children.append(None)
                continue

            right = children.pop()
            left = children.pop()

            new_node = TreeNode(int(val), left, right)
            children.append(new_node)
            
        return children[0]