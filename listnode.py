# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# if l1 よりもif l1 is not Noneのほうが早い

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        current   = dummyHead
        carry     = 0
        while (l1 is not None or l2 is not None):
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            
            #divmodでcarry(商)とdigit(余)を一気に計算
            carry, digit = divmod(carry + v1 + v2, 10)
            current.next = current = ListNode(digit)
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            
        if carry > 0:
            current.next = ListNode(carry)
        return dummyHead.next
