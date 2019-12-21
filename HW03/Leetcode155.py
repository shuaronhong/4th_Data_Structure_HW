# Runtime: 52 ms, faster than 99.05% of Python3 online submissions for Min Stack.
# Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.stack_min) == 0:
            self.stack_min.append(x)
        else:
            self.stack_min.append(min(self.stack_min[-1], x))

    def pop(self) -> None:
        if len(self.stack) == 0:
            return

        self.stack.pop(-1)
        self.stack_min.pop(-1)

    def top(self) -> int:
        if len(self.stack) == 0:
            return
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]