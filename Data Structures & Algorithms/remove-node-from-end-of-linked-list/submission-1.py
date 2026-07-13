# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = dummy
        length = 0
        while curr: 
            curr = curr.next
            length += 1

        curr = dummy
        for i in range(length-n-1):
            curr = curr.next
            
        curr.next = curr.next.next
        return dummy.next