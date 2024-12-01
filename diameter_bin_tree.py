from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth_dia(root:Optional[TreeNode]) -> tuple[int,int]:
            if not root: return 0, 0

            l_dep, l_dia = depth_dia(root.left)
            r_dep, r_dia = depth_dia(root.right)

            return 1 + max(l_dep, r_dep), max(l_dep + r_dep, l_dia, r_dia)

        return depth_dia(root)[1]