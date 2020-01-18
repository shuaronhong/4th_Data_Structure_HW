# Runtime: 72 ms, faster than 93.25% of Python3 online submissions
# Memory Usage: 16.1 MB, less than 5.41% of Python3 online submissions
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x[0])
        rooms = [0]

        for itv in intervals:
            if rooms[0] <= itv[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, itv[1])

        return len(rooms)