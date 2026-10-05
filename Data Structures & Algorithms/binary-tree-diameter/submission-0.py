# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0 
        def max_depth_subtree(root):
            nonlocal max_diameter
            if not root:
                return 0
            
            left_subtree_depth = max_depth_subtree(root.left)
            right_subtree_depth = max_depth_subtree(root.right)

            diameter = left_subtree_depth + right_subtree_depth
            max_diameter = max(diameter, max_diameter)
            return 1 + max(left_subtree_depth, right_subtree_depth)
        max_depth_subtree(root)
        return max_diameter

