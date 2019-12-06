# Runtime: 1116 ms, faster than 8.54% of Python3 online submissions
# Memory Usage: 13.3 MB, less than 42.63% of Python3
class Solution:
    # I did not use dictionary so it is slow. But this is how you do this with
    # just array manipulation, and back tracking. Very easy to understand.
    def solveSudoku(self, board: List[List[str]]) -> None:
        emptyIdx = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    emptyIdx.append((row, col))

        def isUsed(row, col, num):
            return usedInRow(row, num) or usedInCol(col, num) or usedInBox(row, col, num)

        def usedInRow(rowIdx, num):
            for col in range(9):
                if board[rowIdx][col] == str(num):
                    return True
            return False

        def usedInCol(colIdx, num):
            for row in range(9):
                if board[row][colIdx] == str(num):
                    return True
            return False

        def usedInBox(rowIdx, colIdx, num):
            leftRowIdx = rowIdx - rowIdx % 3
            topColIdx = colIdx - colIdx % 3
            for row in range(leftRowIdx, leftRowIdx + 3):
                for col in range(topColIdx, topColIdx + 3):
                    if board[row][col] == str(num):
                        return True
            return False

        def allFilled():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        return False
            return True

        def solve(i):
            if allFilled() and i <= len(emptyIdx):
                return True
            for num in range(1, 10):
                row = emptyIdx[i][0]
                col = emptyIdx[i][1]
                if not isUsed(row, col, num):
                    board[row][col] = str(num)
                    if not solve(i + 1):
                        board[row][col] = '.'
                    else:
                        # to make the bottom most base transfer upward
                        return True
            return False

        solve(0)

# 416 ms, faster than 42.50% of Python3 online submissions
# Memory Usage: 12.9 MB, less than 96.43% of Python3 online submissions
class Solution:
    # Using Dictionary and set is faster. The rationale is you don't need to care about the
    # order of the 9 numbers, you just need to know that if a number is already in a set
    def solveSudoku(self, board: List[List[str]]) -> None:
        emptyIdx = []
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        def addNum(row, col, num):
            rows[row].add(num)
            cols[col].add(num)
            boxes[(row // 3) * 3 + col // 3].add(num)

        def removeNum(row, col, num):
            rows[row].remove(num)
            cols[col].remove(num)
            boxes[(row // 3) * 3 + col // 3].remove(num)

        def isUsed(row, col, num):
            return usedInRow(row, num) or usedInCol(col, num) or usedInBox(row, col, num)

        def usedInRow(row, num):
            return num in rows[row]

        def usedInCol(col, num):
            return num in cols[col]

        def usedInBox(row, col, num):
            return num in boxes[(row // 3) * 3 + col // 3]

        def allFilled():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        return False
            return True

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    emptyIdx.append((row, col))
                else:
                    num = int(board[row][col])
                    addNum(row, col, num)

        def solve(i):
            if allFilled() and i <= len(emptyIdx):
                return True
            for num in range(1, 10):
                row = emptyIdx[i][0]
                col = emptyIdx[i][1]
                if not isUsed(row, col, num):
                    board[row][col] = str(num)
                    addNum(row, col, num)
                    if not solve(i + 1):
                        board[row][col] = '.'
                        removeNum(row, col, num)
                    else:
                        # to make the bottom most base transfer upward
                        return True
            return False

        solve(0)
