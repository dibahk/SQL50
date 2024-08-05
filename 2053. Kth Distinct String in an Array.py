class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        distinct = []
        repeated = []
        for i in arr:
            if i in distinct:
                distinct.remove(i)

            elif i not in repeated:
                distinct.append(i)
                repeated.append(i)
        if len(distinct) < k:
            return ""
        return distinct[k-1]
