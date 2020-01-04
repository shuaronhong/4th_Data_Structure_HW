class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        P = [0]
        for a in A:
            P.append(P[-1] + a)

        queue = []
        res = len(A) + 1
        for i in range(len(P)):
            while queue and P[i] <= P[queue[-1]]:
                queue.pop(-1)

            while queue and P[i] - P[queue[0]] >= K:
                res = min(res, i - queue.pop(0))
            queue.append(i)

        return res if res != len(A) + 1 else -1