# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balancedFlag = True
        def calLength(root):
            nonlocal balancedFlag
            if not root:
                return 0 

            left_length = calLength(root.left)
            right_length = calLength(root.right)  

            if abs(left_length - right_length) > 1:
                balancedFlag = False

            return max(1 + left_length, 1 + right_length)
        calLength(root)
        return balancedFlag

    