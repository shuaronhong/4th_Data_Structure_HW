#Runtime: 28 ms, faster than 67.07% of Python3 online submissions
#Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        def postOrder(node):
            if node is None:
                return
            postOrder(node.left)
            postOrder(node.right)
            self.res.append(node.val)
        postOrder(root)
        return self.res