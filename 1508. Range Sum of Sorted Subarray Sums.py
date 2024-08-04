class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        sums = []
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l+1):
                sums.append(sum(nums[i:j]))
        sums = sorted(sums)
        mod = 10**9 + 7
        return sum(sums[left-1:right]) % mod
        
