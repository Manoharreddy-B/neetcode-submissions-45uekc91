# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return root

        # # post order reversal
        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)

        # root.left = right
        # root.right = left

        # # pre-order reversal
        # root.left, root.right =  root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # BFS (level order traversal)
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            node.left, node.right = node.right, node.left
            

        return root
