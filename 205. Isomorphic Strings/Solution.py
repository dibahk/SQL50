class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        su = []
        tu = []
        l1 = []
        l2 = []
        for i in s:
            if i not in su:
                su.append(i)
            l1.append(su.index(i))
        for i in t:
            if i not in tu:
                tu.append(i)
            l2.append(tu.index(i))
    
        
        return l1 == l2
