class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = dict()
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        index = [key for key, value in freq.items() if value == max(freq.values())]
        sum = 0
        for i in index:
            sum += freq[i]
        return sum
