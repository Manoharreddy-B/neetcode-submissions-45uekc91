# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        if not root:
            return output

        queue = deque()
        queue.append(root)
        
        while queue:
            len_q = len(queue)
            temp_out = []
            for _ in range(len_q):
                popped = queue.popleft()
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
                temp_out.append(popped.val)
            output.append(temp_out)
        return output