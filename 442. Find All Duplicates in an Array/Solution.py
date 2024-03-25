class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num = []
        res = []
        for i in nums:
            if i in num:
                res.append(i)
            else:
                num.append(i)
        return res
