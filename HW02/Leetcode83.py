#Runtime: 32 ms, faster than 98.92% of Python3 online submissions
#Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while curr.next is not None:
            if curr.val == curr.next.val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return dummy.next