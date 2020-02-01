class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        capacity = len(hashTable) * 2
        res = [None for i in range(capacity)]
        for node in hashTable:
            curr = node
            while curr is not None:
                idx = curr.val % capacity
                if res[idx] is None:
                    res[idx] = ListNode(curr.val)
                else:
                    newCurr = res[idx]
                    while newCurr.next is not None:
                        newCurr = newCurr.next
                    newCurr.next = ListNode(curr.val)
                curr = curr.next
        return res