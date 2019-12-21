#Runtime: 48 ms, faster than 93.66% of Python3 online submissions
#Memory Usage: 13.4 MB, less than 97.67% of Python3 online submissions
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        res = 0
        stack = []
        for i in range(len(height)):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                top_idx = stack.pop(-1)
                if len(stack) == 0:
                    break
                res += (min(height[i], height[stack[-1]])-height[top_idx])*(i-(stack[-1]+1))
            stack.append(i)
        return res