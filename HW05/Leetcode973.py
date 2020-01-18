# Runtime: 720 ms, faster than 51.98% of Python3 online submissions
# Memory Usage: 18.1 MB, less than 5.80% of Python3 online submissions
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(p):
            return p[0] ** 2 + p[1] ** 2

        hq = []
        for point in points:
            heapq.heappush(hq, (dist(point), point))

        res = []
        for i in range(K):
            elem = heapq.heappop(hq)
            point = elem[1]
            res.append(point)
        return res