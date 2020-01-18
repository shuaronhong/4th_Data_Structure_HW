# Runtime: 188 ms, faster than 52.41% of Python3 online submissions
# Memory Usage: 15.1 MB, less than 50.00% of Python3 online submissions
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if heightMap is None or heightMap == []:
            return 0
        if len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0
        m = len(heightMap)
        n = len(heightMap[0])

        visited = set()
        boundary = []

        for i in range(m):
            heapq.heappush(boundary, (heightMap[i][0], (i, 0)))
            heapq.heappush(boundary, (heightMap[i][n - 1], (i, n - 1)))
            visited.add((i, 0))
            visited.add((i, n - 1))
        for j in range(n):
            if (0, j) not in visited:
                heapq.heappush(boundary, (heightMap[0][j], (0, j)))
                visited.add((0, j))
            if (m - 1, j) not in visited:
                heapq.heappush(boundary, (heightMap[m - 1][j], (m - 1, j)))
                visited.add((m - 1, j))

        res = 0
        movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while boundary:
            height, pos = heapq.heappop(boundary)
            for move in movements:
                newPos = (pos[0] + move[0], pos[1] + move[1])
                if 0 <= newPos[0] < m and 0 <= newPos[1] < n and newPos not in visited:
                    visited.add(newPos)
                    res += max(0, height - heightMap[newPos[0]][newPos[1]])
                    heapq.heappush(boundary, (max(height, heightMap[newPos[0]][newPos[1]]), newPos))
        return res