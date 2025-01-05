from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # recursive solution
        # maxpathsum is the greater of maxpathsum of child trees,
        # OR adding maxpathsum of children to value of root
        mps = root.val
        
        def recur_mps(root: Optional[TreeNode]) -> int:

            if not root: return 0

            left = recur_mps(root.left)
            right = recur_mps(root.right)

            thru_root = max(left, right, 0) + root.val

            nonlocal mps
            mps = max(mps, thru_root, left + right + root.val)

            return thru_root

        recur_mps(root)
        return mps