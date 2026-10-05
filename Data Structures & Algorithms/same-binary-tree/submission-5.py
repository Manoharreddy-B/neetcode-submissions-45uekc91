# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # isSame = True
        # def compareSubTree(p, q):
        #     nonlocal isSame
        #     if not p and not q:
        #         return (None, None)
        #     if not q and p:
        #         isSame = False
        #         return (p, None)
        #     if q and not p:
        #         isSame = False
        #         return (None, q)

        #     p_left_node, q_left_node = compareSubTree(p.left, q.left)
        #     if p_left_node.val != q_left_node.val:
        #         isSame = False
        #     p_right_node, q_right_node = compareSubTree(p.right, p.right)
        #     if p_right_node.val != q_right_node.val:
        #         isSame = False
        #     return 

        
        # return isSame

        # p_q = deque([p])
        # q_q = deque([q])

        # while p_q and q_q:
        #     if len(p_q) != len(q_q):
        #         return False
        #     for i in range(len(p_q)):
        #         popped_p = p_q.popleft()
        #         popped_q = q_q.popleft()

        #         if not popped_p and not popped_q:
        #             continue
        #         elif (not popped_p and popped_q) or (popped_p and not popped_q):
        #             return False
        #         else:
        #             if popped_p.val == popped_q.val:
        #                 p_q.append(popped_p.left)
        #                 q_q.append(popped_q.left)
        #                 p_q.append(popped_p.right)
        #                 q_q.append(popped_q.right)
        #             else:
        #                 return False
            
        # basically for loop is not necessary even without it we will
        # go through each node, for loop is useful to track when a level is completed.
        queue = deque([(p, q)])

        while queue:
            node_p, node_q = queue.popleft()

            if not node_p and not node_q:
                continue

            if not node_p or not node_q:
                return False

            if node_p.val != node_q.val:
                return False

            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))


        return True
                


