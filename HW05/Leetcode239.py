# Runtime: 164 ms, faster than 66.46% of Python3 online submissions
# Memory Usage: 24.9 MB, less than 7.69% of Python3 online submissions
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k == 0:
            return []
        if k == 1:
            return nums

        hq = []
        for i in range(k):
            heapq.heappush(hq, (-nums[i], i))
        res = [max(nums[:k])]

        for i in range(k, len(nums)):
            heapq.heappush(hq, (-nums[i], i))
            while hq[0][1] < i - k + 1:
                heapq.heappop(hq)
            res.append(-hq[0][0])
        return res