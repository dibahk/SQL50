class Solution:
    def pivotInteger(self, n: int) -> int:
        sumt = n*(n+1)/2
        for i in range(1, n+1):
            sum1 = i*(i+1)/2
            sum2 = sumt-i*(i-1)/2
            if sum1 == sum2:
                return i
        return -1
        
