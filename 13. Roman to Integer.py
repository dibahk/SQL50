class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        rom = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        i = 0
        flag = True
        print(len(s))
        while i < len(s)-1:
            left = rom[s[i]]
            right = rom[s[i + 1]]
            if left >= right:
                ans += left
                i += 1
                flag = True
            else:
                ans += (right - left)
                i += 2
                flag = False
            # print(ans)
        print(flag)
        if flag or i == len(s) - 1:
            ans += rom[s[i]]
        return ans
