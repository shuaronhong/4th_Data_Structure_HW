class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        for i in range(len(nums1)):
            if nums1[i] in dict1:
                dict1[nums1[i]] += 1
            else:
                dict1[nums1[i]] = 1

        list1 = []
        for i in range(len(nums2)):
            if nums2[i] in dict1:
                if dict1[nums2[i]] > 1:
                    dict1[nums2[i]] -= 1
                else:
                    del dict1[nums2[i]]
                list1.append(nums2[i])

        return list1