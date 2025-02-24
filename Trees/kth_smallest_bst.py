from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        idx = 1

        def inorder(root):
            if not root: return None
            nonlocal idx

            left = inorder(root.left)
            if left: return left

            if idx == k:
                return root.val

            idx += 1

            right = inorder(root.right)
            if right: return right

        return inorder(root)