class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = Counter()
        ans = 0
        i = -1
        for j in range(len(nums)):
            freq[nums[j]] += 1
            while freq[nums[j]] >k:
                i += 1
                freq[nums[i]] -= 1
            ans = max(ans, j-i)
        return ans
