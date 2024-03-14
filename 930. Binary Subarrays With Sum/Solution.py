class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        start = 0
        end = 0
        count = 0
        suma = nums[start]
        while start < len(nums):
            if suma == goal:
                count += 1
                # start += 1
                end += 1
            while suma < goal:
                end += 1
                suma += nums[end]
            if suma > goal or end == len(nums):
                start += 1
                end = start

        return count
