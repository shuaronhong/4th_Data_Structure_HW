# Runtime: 68 ms, faster than 71.23% of Python3 online submissions
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        extra_left = 0
        extra_right = 0
        for c in s:
            if c == "(":
                extra_left += 1
            elif c == ")":
                if extra_left > 0:
                    extra_left -= 1
                elif extra_left == 0:
                    extra_right += 1

        def dfs(s, idx, left_count, right_count, sbuilder, removed_left, removed_right):
            if idx == len(s):
                if removed_left == extra_left and removed_right == extra_right:
                    print(sbuilder)
                    res.add("".join(sbuilder))
            else:
                if s[idx] == "(" and removed_left < extra_left:
                    dfs(s, idx + 1, left_count, right_count, sbuilder, removed_left + 1,
                        removed_right)
                elif s[idx] == ")" and removed_right < extra_right:
                    dfs(s, idx + 1, left_count, right_count, sbuilder, removed_left,
                        removed_right + 1)

                sbuilder.append(s[idx])
                if s[idx] != "(" and s[idx] != ")":
                    dfs(s, idx + 1, left_count, right_count, sbuilder, removed_left,
                        removed_right)
                elif s[idx] == "(":
                    dfs(s, idx + 1, left_count + 1, right_count, sbuilder, removed_left,
                        removed_right)
                elif s[idx] == ")" and left_count > right_count:
                    dfs(s, idx + 1, left_count, right_count + 1, sbuilder, removed_left,
                        removed_right)
                sbuilder.pop(-1)

        dfs(s, 0, 0, 0, [], 0, 0)
        return res