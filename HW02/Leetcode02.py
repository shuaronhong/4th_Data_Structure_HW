# Runtime: 64 ms, faster than 93.77% of Python3 online submissions
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        carry = 0
        temp = curr1.val + curr2.val
        digit = temp % 10
        carry = temp // 10
        dummy = ListNode(digit)
        curr = dummy
        while curr1.next is not None and curr2.next is not None:
            curr1 = curr1.next
            curr2 = curr2.next
            temp = curr1.val + curr2.val + carry
            digit = temp % 10
            carry = temp // 10
            curr.next = ListNode(digit)
            curr = curr.next

        while curr1.next is not None:
            curr1 = curr1.next
            temp = curr1.val + carry
            digit = temp % 10
            carry = temp // 10
            curr.next = ListNode(digit)
            curr = curr.next

        while curr2.next is not None:
            curr2 = curr2.next
            temp = curr2.val + carry
            digit = temp % 10
            carry = temp // 10
            curr.next = ListNode(digit)
            curr = curr.next

        if carry == 1:
            curr.next = ListNode(1)

        return dummy