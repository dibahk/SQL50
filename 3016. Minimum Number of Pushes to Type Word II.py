class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        unique = list(set(word))
        dic = {}
        tap = 0
        counter = 0
        for w in unique:
            dic[w] = word.count(w)
        sort = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        taps = 0
        l = len(unique)
        tap = 0
        for w, c in sort:   
            if counter % 8 == 0:
                tap += 1
            taps += tap * c
            counter+=1
        return taps
