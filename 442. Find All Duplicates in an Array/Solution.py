class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num = [0] * (len(nums)+1)

        res = []
        for i in nums:
            if num[i] == 1:
                res.append(i)
            else:
                num[i] = 1
        return res
