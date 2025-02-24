from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return None, None, True
            
            l_min, l_max, l_valid = dfs(root.left)
            if not l_valid or (l_max and root.val <= l_max):
                return None, None, False

            r_min, r_max, r_valid = dfs(root.right)
            if not r_valid or (r_min and root.val >= r_min):
                return None, None, False

            min = l_min if l_min else root.val
            max = r_max if r_max else root.val

            return min, max, True

        return dfs(root)[2]
