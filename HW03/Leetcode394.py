#Runtime: 28 ms, faster than 83.78% of Python3 online submissions
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        prev_num = ""
        for i in range(len(s)):
            if s[i].isnumeric():
                prev_num += s[i]
            elif s[i] == "[":
                stack.append([prev_num, ""])
                prev_num = ""
            elif s[i] == "]":
                elem = stack.pop(-1)
                tmp = ""
                for j in range(int(elem[0])):
                    tmp += elem[1]
                if len(stack) != 0:
                    stack[-1][1] += tmp
                else:
                    res += tmp
            else:
                if len(stack) != 0:
                    stack[-1][1] += s[i]
                else:
                    res += s[i]
        return res