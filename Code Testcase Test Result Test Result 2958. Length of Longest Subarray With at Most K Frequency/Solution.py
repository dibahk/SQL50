class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_n = 1
        for i in range(len(nums)):
            j = i +1
            dic = {}
            dic[nums[i]] = 1
            while max(dic.values()) <= k and j < len(nums)-1:
                if max_n < (j-i):
                    max_n = j-i
                j += 1
                if nums[j] in dic.keys():
                    nums[j] += 1
                else:
                    nums[j] = 1
        return max_n

            
        
