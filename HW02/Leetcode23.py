# Runtime: 108 ms, faster than 76.59% of Python3 online submissions
# Memory Usage: 15.8 MB, less than 100.00% of Python3 online submissions
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def divHelp(lists, l, r):
            if l == r:
                return lists[l]
            m = (l + r) // 2
            left_head = divHelp(lists, l, m)
            right_head = divHelp(lists, m + 1, r)
            return comHelp(left_head, right_head)

        def comHelp(l1, l2):
            head = ListNode(0)
            prev = head
            curr1 = l1
            curr2 = l2
            while True:
                if curr1 is None:
                    prev.next = curr2
                    break
                if curr2 is None:
                    prev.next = curr1
                    break
                if curr1.val < curr2.val:
                    prev.next = curr1
                    prev = curr1
                    curr1 = curr1.next
                else:
                    prev.next = curr2
                    prev = curr2
                    curr2 = curr2.next

            return head.next

        if not lists or lists == []:
            return
        return divHelp(lists, 0, len(lists) - 1)