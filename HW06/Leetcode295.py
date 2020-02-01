class MedianFinder:
    # you may use a dictionary to do that. The dictionary holds the number and its count.
    # when you get a new number, insert it.

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        heapq.heappush(self.minHeap, -self.maxHeap[0])
        heapq.heappop(self.maxHeap)

        if len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -self.minHeap[0])
            heapq.heappop(self.minHeap)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            return -self.maxHeap[0]