class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # nums = list(set(nums))
        nums.sort()        
        count = 0
        observed = []
        n = len(nums)

        for i in range(n):
            pro = nums[i]
            j = i
            if nums[i] in observed:
                count -= 1
            observed.append(nums[i])
            while pro < k and j < n:
                pro = pro * nums[j]
                j += 1
                count += 1

        return count

