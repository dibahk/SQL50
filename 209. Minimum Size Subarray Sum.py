class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 0
        min_len = 1000000
        s = 0
        ans = 0
        for end in range(len(nums)):
            s += nums[end]
            while s >= target:
                min_len = min(min_len, end - start+1)
                s -= nums[start]
                start += 1
        return min_len if min_len != 1000000 else 0
