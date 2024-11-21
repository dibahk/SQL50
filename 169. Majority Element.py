class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        n = len(nums)
        for i in nums:
            if i in count:
                count[i] += 1
                
            else:
               count[i] = 1
               
            if count[i] > n/2:
                return i
