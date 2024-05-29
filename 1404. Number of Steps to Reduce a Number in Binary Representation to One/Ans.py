class Solution:
    def numSteps(self, s: str) -> int:
        s = list(s)
        step = 0
        while len(s) > 1:
            if s[-1] == "1":
                i = len(s) - 1
                while i >= 0 and s[i] == "1":
                    s[i] = "0"
                    i -= 1
                if i < 0:
                    s.insert(0, "1")
                else: 
                    s[i] = "1"
            else:
                s.pop()
            step += 1
        return step
