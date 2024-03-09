class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        i = 0 #the indicator of num1
        j = 0 #indicator of num2
        l1 = len(nums1)
        l2 = len(nums2)
        while i < l1 and j < l2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
