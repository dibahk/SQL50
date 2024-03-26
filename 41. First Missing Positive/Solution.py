class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        smallest = 1
        for i in nums:
            if i > 0 and i <= smallest:
                smallest = i
            if i == smallest:
                smallest = i + 1
        return smallest
