# Runtime: 200 ms, faster than 85.40% of Python3 online submissions
# Memory Usage: 22.2 MB, less than 9.09% of Python3 online submissions
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> ListNode
        self.head = ListNode(-2, -2)
        self.tail = ListNode(-2, -2)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, node):
        # note head and original next are two nodes which does not change reference
        original_next = self.head.next

        node.prev = self.head
        node.next = original_next

        original_next.prev = node
        self.head.next = node

    def remove_node(self, node):
        original_next = node.next
        original_prev = node.prev

        original_prev.next = original_next
        original_next.prev = original_prev

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        node = self.cache[key]
        self.remove_node(node)
        self.add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            node = self.cache[key]
            node.val = value
            self.remove_node(node)
            self.add_to_front(node)
        else:
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self.add_to_front(new_node)

            if len(self.cache) > self.capacity:
                node_to_remove = self.tail.prev
                del self.cache[node_to_remove.key]
                self.remove_node(node_to_remove)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)