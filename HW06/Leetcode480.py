class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        maxHeap = []
        minHeap = []
        invalid = collections.defaultdict(int)

        for i in range(k):
            heapq.heappush(maxHeap, -nums[i])
        for j in range(k // 2):
            heapq.heappush(minHeap, -maxHeap[0])
            heapq.heappop(maxHeap)

        i = k
        while i <= len(nums):
            res.append(-maxHeap[0] if k % 2 == 1 else (minHeap[0] - maxHeap[0]) / 2)
            if i == len(nums):
                break
            gone = nums[i - k]
            invalid[gone] += 1
            come = nums[i]
            i += 1
            balance = 0  # the number of elements that maxHeap ilegally more than minHeap
            if gone <= -maxHeap[0]:
                balance -= 1
            else:
                balance += 1

            if come <= -maxHeap[0]:
                heapq.heappush(maxHeap, -come)
                balance += 1
            else:
                heapq.heappush(minHeap, come)
                balance -= 1

            if balance == -2:
                heapq.heappush(maxHeap, -minHeap[0])
                heapq.heappop(minHeap)
            elif balance == 2:
                heapq.heappush(minHeap, -maxHeap[0])
                heapq.heappop(maxHeap)

            while invalid[-maxHeap[0]] > 0:
                invalid[-maxHeap[0]] -= 1
                heapq.heappop(maxHeap)

            while len(minHeap) > 0 and invalid[minHeap[0]] > 0:
                invalid[minHeap[0]] -= 1
                heapq.heappop(minHeap)
        return res