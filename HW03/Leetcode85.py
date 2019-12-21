# Runtime: 204 ms, faster than 90.33% of Python3 online submissions for Maximal Rectangle.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0

        consec_h = [0] * (n + 1)
        res = 0
        for i in range(m):
            for j in range(n):
                consec_h[j] = consec_h[j] + 1 if matrix[i][j] == "1" else 0
            stack = [-1]
            for j in range(n + 1):
                while consec_h[j] < consec_h[stack[-1]]:
                    res = max(res, consec_h[stack.pop(-1)] * (j - (stack[-1] + 1)))
                stack.append(j)
        return res 