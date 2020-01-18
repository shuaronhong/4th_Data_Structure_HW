# Runtime: 104 ms, faster than 98.43% of Python3 online submissions
# Memory Usage: 17.4 MB, less than 90.00% of Python3 online submissions
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        pq = [(0, -sys.maxsize - 1, -1)]
        res = []

        for build in buildings:
            rightMost = -1
            while build[0] > -pq[0][1]:
                highestSoFar = heapq.heappop(pq)
                rightMost = max(rightMost, -highestSoFar[1])
                if -pq[0][1] > rightMost:
                    res.append([rightMost, -pq[0][0]])

            if build[2] > -pq[0][0]:
                if len(res) != 0 and build[0] == res[-1][0]:
                    res[-1][1] = build[2]
                else:
                    res.append([build[0], build[2]])

            heapq.heappush(pq, (-build[2], -build[1], build[0]))

        rightMost = -1
        while pq:
            highestSoFar = heapq.heappop(pq)
            rightMost = max(rightMost, -highestSoFar[1])
            if pq and -pq[0][1] > rightMost:
                res.append([rightMost, -pq[0][0]])
        return res