#Runtime: 44 ms, faster than 97.13% of Python3 online submissions
#Memory Usage: 16 MB, less than 100.00% of Python3 online submissions
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycleExistance(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return

    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return

        meet_node = self.detectCycleExistance(head)

        if meet_node is None:
            return None

        curr1 = head
        curr2 = meet_node
        while curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next
        return curr1
