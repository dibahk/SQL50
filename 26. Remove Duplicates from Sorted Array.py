class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[unique-1]:
                nums[unique] = nums[j]
                unique += 1
        print(nums)
        return unique
