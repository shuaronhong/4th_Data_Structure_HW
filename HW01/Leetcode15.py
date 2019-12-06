#Runtime: 1044 ms, faster than 45.27% of Python3 online submissions for 3Sum.
#Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for 3Sum.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        #idx1 is the index of 1st element, idx2 is 2nd, idx3 3rd.
        idx1 = 0
        while idx1 < len(nums)-2:
            compliment = 0 - nums[idx1]
            idx2 = idx1 + 1
            idx3 = len(nums) - 1
            while idx2 < idx3:
                if nums[idx2] + nums[idx3] == compliment:
                    res.append([nums[idx1],nums[idx2],nums[idx3]])
                    idx2 += 1
                    idx3 -= 1
                    while idx2 < idx3 and nums[idx2]==nums[idx2-1]:
                        idx2 += 1
                    while idx2 < idx3 and nums[idx3]==nums[idx3+1]:
                        idx3 -= 1
                elif nums[idx2] + nums[idx3] < compliment:
                    idx2 += 1
                else:
                    idx3 -= 1
            idx1 += 1
            while idx1 < len(nums)-2 and nums[idx1]==nums[idx1-1]:
                idx1 += 1
        return res