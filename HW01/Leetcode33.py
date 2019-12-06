# Runtime: 32 ms, faster than 95.41% of Python3 online submissions
# Memory Usage: 13.2 MB, less than 65.11% of Python3 online submissions
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[start] and nums[mid] < nums[end]:
                if nums[mid] > target:
                    end = mid
                else:
                    start = mid
            elif nums[mid] < nums[start] and nums[mid] < nums[end]:
                if nums[mid] > target:
                    end = mid
                elif nums[mid] < target and target >= nums[start]:
                    end = mid
                elif nums[mid] < target and target < nums[start]:
                    start = mid
            elif nums[mid] > nums[start] and nums[mid] > nums[end]:
                if nums[mid] < target:
                    start = mid
                elif nums[mid] > target and target >= nums[start]:
                    end = mid
                elif nums[mid] > target and target < nums[start]:
                    start = mid
            else:
                print("impossible")

        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        print(start, end)
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1