# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from datetime import date


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        level = 0
        covered = {None}

        def postOrder(node, parent, level):
            if node is None:
                return
            postOrder(node.left, node, level + 1)
            postOrder(node.right, node, level + 1)

            if (parent is None and node not in covered) or (node.left not in covered or node.right not in covered):
                self.res += 1
                covered.update({node, parent, node.left, node.right})

        postOrder(root, None, 0)
        return self.res