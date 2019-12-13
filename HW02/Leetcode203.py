# Runtime: 64 ms, faster than 93.90% of Python3 online submissions
# Memory Usage: 15.6 MB, less than 100.00% of Python3 online submissions
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        dummy = ListNode(0)
        prev = dummy
        prev.next = head
        curr = head
        while curr.next is not None:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        if curr.val == val:
            prev.next = None

        return dummy.next