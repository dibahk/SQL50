class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num = {}
        for i in nums:
            if i in num.keys():
                return i
            else:
                num[i] = 1
            

        
