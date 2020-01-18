# Runtime: 104 ms, faster than 78.27% of Python3 online submissions
# Memory Usage: 17.3 MB, less than 6.25% of Python3 online submissions
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.defaultdict(int)
        for num in nums:
            freq[num] -= 1

        hq = []
        for key in freq.keys():
            heapq.heappush(hq, (freq[key], key))

        res = []
        for i in range(k):
            elem = heapq.heappop(hq)
            res.append(elem[1])
        return res