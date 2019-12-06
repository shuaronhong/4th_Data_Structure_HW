# Runtime: 76 ms, faster than 5.41% of Python3 online submissions
# Memory Usage: 17.4 MB, less than 95.00% of Python3 online submissions
# Try two pointer solution later
class Solution:
    def searchMatrix(self, matrix, target):
        def helper(matrix, target, row_start, row_end, col_start, col_end, is_row):
            row_mid = (row_start + row_end) // 2
            col_mid = (col_start + col_end) // 2
            res1 = res2 = False
            if (row_start < row_end and is_row) or (col_start < col_end and not is_row):
                if matrix[row_mid][col_mid] == target:
                    return True
                if matrix[row_mid][col_mid] < target:
                    res1 = helper(matrix, target, row_mid + 1, row_end, col_start, col_end, True)
                    res2 = helper(matrix, target, row_start, row_end, col_mid + 1, col_end, False)
                else:
                    res1 = helper(matrix, target, row_start, row_mid, col_start, col_end, True)
                    res2 = helper(matrix, target, row_start, row_end, col_start, col_mid, False)
            return res1 or res2

        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        return helper(matrix, target, 0, m, 0, n, True) or helper(matrix, target, 0, m, 0, n, False)