# Runtime: 68 ms, faster than 78.94% of Python3 online submissions
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Since you don't need to change tree structure, you are only dealing with val
        # so, you will just do it when traversing, no need to reconnect TreeNodes, this is important observation
        # So, just find the two nodes that needs swapping while in order traversing, and then swap their values
        # remember for BST in order traverse should return a list in ascending order.
        stack = []
        small = None
        large = None
        prev = None
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop(-1)
            if prev is not None and node.val < prev.val:
                small = node
                if large is None:
                    large = prev
            prev = node
            node = node.right
        small.val, large.val = large.val, small.val