# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # def revLl(l):
        #     prev = None
        #     curr = l
        #     len_l = 0
        #     while curr:
        #         curr_next = curr.next
        #         curr.next = prev
        #         prev = curr
        #         curr = curr_next
        #         len_l += 1
        # return prev, len_l

        carry = 0
        dummy = ListNode(0)
        ans = dummy
        while l1 or l2:
            total = (l1.val if l1 else 0)  + (l2.val if l2 else 0) + carry
            dummy.next = ListNode(total%10)
            carry = 0 
            carry = total//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            dummy = dummy.next
        if carry == 1:
            dummy.next = ListNode(carry)
        return ans.next



