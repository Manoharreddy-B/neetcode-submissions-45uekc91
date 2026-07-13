# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        temp = head
        stack_len = 0 
        while temp:
            stack.append(temp)
            temp = temp.next
            stack_len += 1
        
        curr = head
        i = 0
        for i in range (stack_len // 2):
            temp_node = stack.pop()
            curr_next = curr.next
            curr.next = temp_node
            temp_node.next = curr_next
            curr = curr_next

        curr.next = None
