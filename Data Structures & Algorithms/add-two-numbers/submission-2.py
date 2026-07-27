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
        # return curr, len_l

        # rev_l1, len_l1 = revLl(l1)
        # rev_l2, len_l2 = revLl(l2)
        # one_or_zero = 0
        # dummy = ListNode(0)
        # ans = dummy
        # while l1 or l2:
        #     if l1 and l2:
        #         if l1.val + l2.val > 9:
        #             if dummy.next:
        #                 dummy.next = ListNode((l1.val + l2.val)%10 + dummy.next.val) 
        #             else:
        #                 dummy.next = ListNode((l1.val + l2.val)%10) 
        #             # one_or_zero = (l1.val + l1.val)//10
        #             one_or_zero  = dummy.next.val//10
        #         else:
        #             dummy.next = ListNode((l1.val + l2.val))
        #     elif l1:
        #         dummy.next = ListNode((l1.val + dummy.next.val))
        #     else:
        #         dummy.next = ListNode((l2.val + dummy.next.val))
        #     one_or_zero  = dummy.next.val//10
        #     if one_or_zero == 1:
        #         dummy.next.next = ListNode(1)
        #         one_or_zero = 0
        #     dummy = dummy.next
        #     l1 = l1.next
        #     l2 = l2.next
        # return ans.next

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



