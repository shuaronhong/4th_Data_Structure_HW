# Runtime: 64 ms, faster than 99.52% of Python3 online submissions
# Memory Usage: 19.6 MB, less than 92.31% of Python3 online submissions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.push_to_stack(root)

    def push_to_stack(self, root):
        while root is not None:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        smallest = self.stack.pop(-1)
        if smallest.right is not None:
            self.push_to_stack(smallest.right)
        return smallest.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0