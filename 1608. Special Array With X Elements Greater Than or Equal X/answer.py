class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l1 = [0]*(len(range(max(nums)))+1)
        if len(l1) == 1:
            return -1
        for i in nums:
            l1[i]+=1
        for i in reversed(range(len(l1))):
            s = sum(l1[i:])
            if i == s:
                return i
            
        return -1

        
