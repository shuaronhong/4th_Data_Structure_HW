# Runtime: 96 ms, faster than 90.10% of Python3 online submissions
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(A: List[int], B: List[int], k: int, aStart: int, aEnd: int, bStart: int, bEnd: int):
            aLen = aEnd - aStart + 1
            bLen = bEnd - bStart + 1
            # base cases
            if aLen == 0:
                return B[bStart + k]
            if bLen == 0:
                return A[aStart + k]
            if k == 0:
                return A[aStart] if A[aStart] < B[bStart] else B[bStart]

            # relationship i+j == k-1. i, j, k are zero-based indices
            aMid = math.floor(aLen * k / (aLen + bLen))
            bMid = k - aMid - 1
            aMidIndex = aMid + aStart
            bMidIndex = bMid + bStart

            if A[aMidIndex] > B[bMidIndex]:
                k = k - (bMid + 1)
                aEnd = aMid + aStart
                bStart = bMid + bStart + 1
            else:
                k = k - (aMidIndex - aStart + 1)
                bEnd = bMidIndex
                aStart = aMidIndex + 1
            return findKth(A, B, k, aStart, aEnd, bStart, bEnd)

        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 != 0:
            k = math.floor((m + n) / 2)
            return float(findKth(nums1, nums2, k, 0, m - 1, 0, n - 1))
        else:
            k = math.floor((m + n) / 2)
            return float(
                (findKth(nums1, nums2, k - 1, 0, m - 1, 0, n - 1) + findKth(nums1, nums2, k, 0, m - 1, 0, n - 1)) / 2.0)