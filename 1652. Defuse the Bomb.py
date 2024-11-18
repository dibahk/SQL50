class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = [0] * len(code)
        if k == 0:
            return ans
        if k > 0:
            for i in range(len(code)):
                for j in range(i+1, i + k +1):
                    ans[i] += code[j % len(code)]
        if k < 0:
            for i in range(len(code)):
                for j in range(i + k, i):
                    ans[i] += code[j % len(code)]
        
        return ans
        
