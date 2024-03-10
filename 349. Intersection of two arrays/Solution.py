class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        i = 0 #the indicator of num1
        j = 0 #indicator of num2
        l1 = len(nums1)
        l2 = len(nums2)

        dic = {}
        while i < l1 and j < l2:
            if nums1[i] == nums2[j]:
                dic[nums1[i]] = 1
                i += 1 
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return dic
