# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        # left_depth = self.maxDepth(root.left)
        # right_depth = self.maxDepth(root.right)

        # return max(left_depth+1, right_depth+1)

        stack = [[root, 1]]
        max_depth = 0
        while stack:
            item = stack.pop()
            node, depth = item[0], item[1]
            if node.left:
                stack.append([node.left, depth+1])
            if node.right:
                stack.append([node.right, depth+1])
            max_depth = max(max_depth, depth)
        return max_depth
