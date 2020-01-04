#Runtime: 32 ms, faster than 82.29% of Python3 online submissions
#Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = []
        queue.append(root)
        queue.append(root)
        while queue:
            node1 = queue.pop(0)
            node2 = queue.pop(0)
            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False
            else:
                queue.append(node1.left)
                queue.append(node2.right)
                queue.append(node1.right)
                queue.append(node2.left)
        return True