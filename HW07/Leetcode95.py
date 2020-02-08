class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def form_bst(low, high):
            if low > high:
                return [None]
            BSTs = []
            for i in range(low, high+1):
                left_trees = form_bst(low, i-1)
                right_trees = form_bst(i+1, high)
                for left_tree in left_trees:
                    for right_tree in right_trees:
                        head = TreeNode(i)
                        head.left = left_tree
                        head.right = right_tree
                        BSTs.append(head)
            return BSTs
        if n == 0:
            return []
        return form_bst(1, n)