from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        preorder_idx = 0

        def recursive_build_tree(inorder: list[int]) -> Optional[TreeNode]:
            if not inorder: return None

            root = TreeNode()

            # get next node val from preorder
            nonlocal preorder_idx
            root.val = preorder[preorder_idx]
            preorder_idx += 1

            # find node in inorder and split inorder
            root_idx = inorder.index(root.val)
            left = inorder[0:root_idx]
            right = inorder[root_idx + 1:]

            # recur left of node inorder
            root.left = recursive_build_tree(left)

            # recur right of node inorder
            root.right = recursive_build_tree(right)

            return root
        
        return recursive_build_tree(inorder)