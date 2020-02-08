#Runtime: 84 ms, faster than 89.28% of Python3 online submissions
#Memory Usage: 20.1 MB, less than 100.00% of Python3 online submissions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        def max_sum(node):
            if node is None:
                return float('-inf')
            left_sum = max_sum(node.left)
            right_sum = max_sum(node.right)
            connected_subSum = max([node.val, node.val+left_sum, node.val+right_sum])
            self.res = max([self.res,node.val+left_sum+right_sum,connected_subSum])
            return connected_subSum
        max_sum(root)
        return self.res