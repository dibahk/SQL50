class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        out = ''
        for char in order:
            if char in s:
                for i in range(s.count(char)):
                    out = out + char
                s = s.replace(char,'')
            
        out = out + s
        return out
