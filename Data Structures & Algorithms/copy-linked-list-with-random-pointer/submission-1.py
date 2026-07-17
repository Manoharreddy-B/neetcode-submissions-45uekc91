"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None


        random_store_1 = {}

        temp = Node(0)
        temp2 = head
        ans = temp
        while temp2:
            temp.next = Node(temp2.val)
            random_store_1[temp2] = temp.next
            temp = temp.next
            temp2 = temp2.next

        temp2 = head
        temp = ans.next
        while temp2:
            old_random = temp2.random
            if old_random:
                new_random_4_temp2 = random_store_1[old_random] 
                temp.random = new_random_4_temp2
            else:
                temp.random = None
            temp2 = temp2.next
            temp = temp.next
        return ans.next