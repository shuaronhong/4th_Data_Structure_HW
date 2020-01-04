# Runtime: 480 ms, faster than 93.75% of Python3 online submissions
# Memory Usage: 14.4 MB, less than 92.31% of Python3 online submissions
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pqueue = [(0, K)]
        distances = {}

        while pqueue:
            elem = heapq.heappop(pqueue)
            node = elem[1]
            dist = elem[0]
            if node in distances:
                continue
            else:
                distances[node] = dist
                for v, w in graph[node]:
                    if v not in distances:
                        heapq.heappush(pqueue, (dist + w, v))
        if len(distances) != N:
            return -1
        else:
            return max(distances.values())