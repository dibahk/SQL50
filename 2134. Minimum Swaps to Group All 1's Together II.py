class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones = sum(nums)
        count = nums[0]
        min_s = float("inf")
        end = 0
        for start in range(len(nums)):
            if start != 0:
                count -= nums[start - 1]
            while end- start + 1 < ones:
                end += 1
                count += nums[end % len(nums)]
            min_s = min(min_s, ones - count)
        return min_s
