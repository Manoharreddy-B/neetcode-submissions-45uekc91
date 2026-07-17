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

        old_to_new = {}

        dummy = Node(0)
        copy_tail = dummy
        current = head
        while current:
            copy_tail.next = Node(current.val)
            old_to_new[current] = copy_tail.next
            copy_tail = copy_tail.next
            current = current.next

        current = head
        copy_current = dummy.next
        while current:
            current_random = current.random
            if current_random:
                copy_current.random = old_to_new[current_random] 
            else:
                copy_current.random = None
            current = current.next
            copy_current = copy_current.next
        return dummy.next